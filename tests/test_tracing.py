"""Handwritten, not generated. Listed in .fernignore alongside tracing.py."""

import httpx
import pytest

from calibrate import tracing


def test_log_posts_in_the_background(monkeypatch):
    sent = {}

    def fake_post(url, json, headers, timeout):
        sent["url"] = url
        sent["json"] = json
        sent["headers"] = headers
        return httpx.Response(200, json={"uuid": "x"})

    monkeypatch.setattr(tracing.httpx, "post", fake_post)

    tracing.log(
        agent_id="agent-1",
        input=[{"role": "user", "content": "hi"}],
        output={"response": "hello"},
        metadata={"env": "prod"},
        api_key="sk_test",
        base_url="https://example.test/",
    ).result(timeout=5)

    assert sent["url"] == "https://example.test/traces"
    assert sent["headers"]["X-API-Key"] == "sk_test"
    assert sent["json"]["metadata"] == [{"key": "env", "value": "prod"}]
    # Unset optional fields are omitted, not sent as null.
    assert "message_id" not in sent["json"]


def test_a_failed_send_does_not_reach_the_caller(monkeypatch):
    def boom(*args, **kwargs):
        raise httpx.ConnectError("down")

    monkeypatch.setattr(tracing.httpx, "post", boom)

    tracing.log(
        agent_id="agent-1",
        input=[{"role": "user", "content": "hi"}],
        output={"response": "hello"},
        api_key="sk_test",
    ).result(timeout=5)


def test_a_missing_api_key_raises_at_call_time(monkeypatch):
    monkeypatch.delenv("CALIBRATE_API_KEY", raising=False)

    with pytest.raises(ValueError):
        tracing.log(
            agent_id="agent-1",
            input=[{"role": "user", "content": "hi"}],
            output={"response": "hello"},
        )
