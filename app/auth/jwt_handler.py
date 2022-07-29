#This file is responsible for signing, encoding and returning JWTs.
import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# This function returns the generated Tokens (JWTs)
def token_response(token:str):
    return{
        "acess token": token
    }

def signJWT(userID:str):
    payload = {
        "uesrID": userID,
        "expiry":time.time() +600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        {}
   