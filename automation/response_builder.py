RESPONSES = {
    "welcome": "Hello! Welcome to our Kik bot.",
    "help": "Send a message and I will try to assist you.",
    "fallback": "Sorry, I didn't understand that message."
}

def build_response(key: str) -> str:
    return RESPONSES.get(key, RESPONSES["fallback"])
