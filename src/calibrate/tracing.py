"""Send a production agent turn to Calibrate without blocking the caller.

Handwritten, not generated. Listed in .fernignore so `fern generate` leaves it
in place.

The generated `Calibrate` client waits for the HTTP response, which is the
wrong trade in a request path: a slow or unreachable Calibrate would slow down
the agent it is only meant to observe. `log()` hands the POST to a background
thread and returns straight away, and a failed send is logged and dropped
rather than raised.

    from calibrate.tracing import log

    log(
        agent_id="...",
        input=[{"role": "user", "content": "where is my order?"}],
        output={"response": "Let me check that for you."},
    )
"""

import logging
import os
from concurrent.futures import Future, ThreadPoolExecutor
from typing import Any, Dict, List, Optional

import httpx

from .environment import CalibrateEnvironment

logger = logging.getLogger(__name__)

# Bounded so a burst of turns cannot spawn a thread per turn. Sends queue
# instead, which is the right trade for data nobody is waiting on.
_executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="calibrate-trace")


def log(
    *,
    agent_id: str,
    input: List[Dict[str, Any]],
    output: Dict[str, Any],
    message_id: Optional[str] = None,
    conversation_id: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
    timeout: float = 10.0,
) -> "Future[None]":
    """Store one agent turn in Calibrate, in the background.

    Parameters
    ----------
    agent_id : str
        UUID of the agent that produced the turn. Must be an agent in the
        workspace the API key belongs to.

    input : List[Dict[str, Any]]
        Conversation history up to the reported output, oldest turn first, in
        OpenAI chat format.

    output : Dict[str, Any]
        What the agent produced: `{"response": "..."}`, or
        `{"tool_calls": [{"tool": "...", "arguments": {...}}]}`, or both.

    message_id : Optional[str]
        Your own ID for the last user message, stored for reference only.

    conversation_id : Optional[str]
        Your own ID for the conversation this turn belongs to, stored for
        reference only.

    metadata : Optional[Dict[str, str]]
        Extra key-value pairs to store with the trace.

    api_key : Optional[str]
        Calibrate API key. Defaults to the CALIBRATE_API_KEY environment
        variable.

    base_url : Optional[str]
        Calibrate API base URL. Defaults to the CALIBRATE_BASE_URL environment
        variable, then to the hosted API.

    timeout : float
        Seconds to wait on the send before giving up.

    Returns
    -------
    Future[None]
        Resolves once the send finishes. Ignore it unless you want to wait.
    """
    key = api_key or os.environ.get("CALIBRATE_API_KEY")
    if not key:
        raise ValueError(
            "No Calibrate API key. Pass api_key= or set CALIBRATE_API_KEY."
        )

    url = (
        base_url
        or os.environ.get("CALIBRATE_BASE_URL")
        or CalibrateEnvironment.DEFAULT.value
    ).rstrip("/") + "/traces"

    payload: Dict[str, Any] = {
        "agent_id": agent_id,
        "input": input,
        "output": output,
    }
    if message_id is not None:
        payload["message_id"] = message_id
    if conversation_id is not None:
        payload["conversation_id"] = conversation_id
    if metadata:
        payload["metadata"] = [{"key": k, "value": v} for k, v in metadata.items()]

    return _executor.submit(_send, url, key, payload, timeout)


def _send(url: str, api_key: str, payload: Dict[str, Any], timeout: float) -> None:
    try:
        response = httpx.post(
            url,
            json=payload,
            headers={"X-API-Key": api_key},
            timeout=timeout,
        )
        if response.status_code >= 400:
            logger.warning(
                "Calibrate trace rejected (%s): %s",
                response.status_code,
                response.text[:500],
            )
    except Exception:
        logger.warning("Calibrate trace failed to send", exc_info=True)
