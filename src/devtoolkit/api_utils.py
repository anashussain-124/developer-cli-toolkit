
import json

import requests


def api_get(url, timeout=10):
    """Send an HTTP GET request and display the response."""

    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"Accept": "application/json"},
        )

        print(f"URL: {response.url}")
        print(f"Status: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'unknown')}")

        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")

        if "json" in content_type.lower():
            try:
                data = response.json()
                print("\nResponse body:")
                print(json.dumps(data, indent=4, ensure_ascii=False))
            except requests.exceptions.JSONDecodeError:
                print("\nError: Server returned invalid JSON.")
        else:
            print("\nResponse body:")
            print(response.text[:5000])

    except requests.exceptions.Timeout:
        print(f"Error: Request timed out after {timeout} seconds.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
