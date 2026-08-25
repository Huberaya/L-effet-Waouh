import secrets, hashlib

def hash_pw(pw: str) -> str:
    salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, 120_000)
    return salt.hex() + "$" + dk.hex()

def check_pw(pw: str, stored: str) -> bool:
    try:
        salt, dk = stored.split("$")
        return hashlib.pbkdf2_hmac("sha256", pw.encode(), bytes.fromhex(salt), 120_000).hex() == dk
    except Exception:
        return False

def generate_token() -> str:
    return secrets.token_urlsafe(32)
