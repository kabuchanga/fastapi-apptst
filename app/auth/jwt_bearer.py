from base64 import decode
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import  decodeJWT

class jwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(jwtBearer,self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials : HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.schema == "Bearer":
                raise HTTPException(status_code=403, detail="Invalide or Expired Token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid or Expired Token!")                
     

def verify_jwt(self, jwtoken :str):
    isTokenValid : bool = False
    payload = decodeJWT(jwtoken)
    if payload:
        isTokenValid =True
    return isTokenValid
    