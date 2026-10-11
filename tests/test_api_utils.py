
from unittest.mock import Mock, patch

import requests

from devtoolkit.api_utils import api_get


@patch("devtoolkit.api_utils.requests.get")
def test_api_get_prints_successful_json(mock_get, capsys):
    response = Mock()
    response.url = "https://example.com/todos/1"
    response.status_code = 200
    response.headers = {
        "Content-Type": "application/json"
    }
    response.json.return_value = {
        "id": 1,
        "title": "Learn Python",
        "completed": False,
    }
    response.raise_for_status.return_value = None

    mock_get.return_value = response

    api_get("https://example.com/todos/1")

    output = capsys.readouterr().out

    assert "Status: 200" in output
    assert "Learn Python" in output
    mock_get.assert_called_once()


@patch("devtoolkit.api_utils.requests.get")
def test_api_get_handles_timeout(mock_get, capsys):
    mock_get.side_effect = requests.exceptions.Timeout

    api_get("https://example.com/todos/1")

    output = capsys.readouterr().out

    assert "Request timed out" in output


@patch("devtoolkit.api_utils.requests.get")
def test_api_get_handles_http_error(mock_get, capsys):
    response = Mock()
    response.url = "https://example.com/missing"
    response.status_code = 404
    response.headers = {
        "Content-Type": "application/json"
    }
    response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError("404 Client Error")
    )

    mock_get.return_value = response

    api_get("https://example.com/missing")

    output = capsys.readouterr().out

    assert "Status: 404" in output
    assert "HTTP error" in output
