TOKENS = {"admin": "securetoken123"}

def authenticate(token: str) -> bool:
    return token in TOKENS.values()
