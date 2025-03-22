from pydantic import BaseModel

class CallRequest(BaseModel):
    user_id: str
    query: str
