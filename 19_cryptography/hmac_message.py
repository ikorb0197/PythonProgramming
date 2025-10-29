import hmac # hash-based message authentification code
import hashlib

def calc_hash(key: str, msg: str):
    b_key = key.encode()
    b_msg = msg.encode()
    hash_value = hmac.new(b_key, b_msg, hashlib.sha256) # Generates hash based on key and message
    return hash_value.hexdigest()

key = "123456789"
hash1 = calc_hash(key, "Pay me $100")
hash2 = calc_hash(key, "Pay me $1000")
hash3 = calc_hash(key, "Pay me $100")

print(hash1 == hash2)
print(hash1 == hash3)

# TODO
# Implement the below functions
def send_msg(msg_text: str) -> dict:
    hash_value = calc_hash(key, msg_text)
    return {"text": msg_text, "hash": hash_value}

def receive_message(msg: dict):
    text = msg.get("text")
    hash_value = msg.get("hash")
    return text, hash_value

print(send_msg("Hello, World!"))
print(receive_message(send_msg("Hello, World!")))