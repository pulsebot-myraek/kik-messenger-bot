def route_message(text: str) -> str:
    text = (text or "").lower().strip()
    if text in ("hi", "hello"):
        return "welcome"
    if "help" in text:
        return "help"
    return "fallback"
