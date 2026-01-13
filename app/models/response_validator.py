def validate_response(response, allowed_statuses=(200,)):
    # Convert int → tuple automatically
    if isinstance(allowed_statuses, int):
        allowed_statuses = (allowed_statuses,)

    if response.status_code not in allowed_statuses:
        raise ValueError(
            f"Expected {allowed_statuses}, got {response.status_code}"
        )

    try:
        data = response.json()
    except Exception:
        raise ValueError("Response is not valid JSON")

    if not data.get("success", False):
        raise ValueError(f"API returned failure: {data.get('errors')}")
