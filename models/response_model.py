from pydantic import BaseModel

class ResponseModel( BaseModel ):
    ok : bool
    msg : str
