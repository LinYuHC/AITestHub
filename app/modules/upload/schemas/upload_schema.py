from pydantic import BaseModel

class UploadData(BaseModel):
    url: str
    filename: str