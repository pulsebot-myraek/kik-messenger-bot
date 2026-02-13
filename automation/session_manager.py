sessions = {}

def get_session(user_id: str):
    return sessions.setdefault(user_id, {})
