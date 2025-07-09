import hmac
import hashlib
import time
import struct
import base64
import requests
import json

def generate_totp(secret, digits=10, time_step=30, t0=0):
    counter = int((int(time.time()) - t0) / time_step)
    key = secret.encode()
    msg = struct.pack(">Q", counter)
    hmac_digest = hmac.new(key, msg, hashlib.sha512).digest()
    offset = hmac_digest[-1] & 0x0F
    binary = struct.unpack(">I", hmac_digest[offset:offset+4])[0] & 0x7FFFFFFF
    otp = binary % (10 ** digits)
    return str(otp).zfill(digits)

def main():
    email = "ardusingh28@gmail.com"
    secret = email + "HENNGECHALLENGE004"
    totp = generate_totp(secret)
    
    # Prepare auth header
    user_pass = f"{email}:{totp}"
    auth_token = base64.b64encode(user_pass.encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_token}",
        "Content-Type": "application/json"
    }

    # Prepare payload
    payload = {
        "github_url": "https://gist.github.com/Ardusingh7/357ecc6cc3b1743a073d67ded485cce1",
        "contact_email": email,
        "solution_language": "python"
    }

    # Send POST request
    url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print("Status Code:", response.status_code)
    try:
        print("Response:", response.json())
    except Exception:
        print("Raw Response:", response.text)

if __name__ == "__main__":
    main()

