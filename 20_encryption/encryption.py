def generate_keys():
    # Take 2 prime numbers
    p = 3461
    q = 3557

    # Calculate the product of 2 primes
    n = p * q
    
    # Public (e)
    # gcd(n, e) = 1
    e = 17

    # Private (d)
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    print(d)

    return (e, n), (d, n) # (public), (private)

def encrypt(msg, public_key):
    e, n = public_key
    return pow(msg, e, n)

def decrypt(msg, private_key):
    d, n = private_key
    return pow(msg, d, n)

msg = 1111
public_key, private_key = generate_keys()
print(f"Public key (e, n)", public_key)
print(f"Private key (d, n)", private_key)

ciphertext = encrypt(msg, public_key)
plaintext = decrypt(ciphertext, private_key)
print(f"Original: {msg}, Ciphertext: {ciphertext}, Decrypted: {plaintext}")