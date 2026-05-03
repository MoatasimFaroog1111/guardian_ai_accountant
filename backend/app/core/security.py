def mask_secret(value: str | None) -> str:
    if not value:
        return "not_configured"
    return "configured"
