from pydantic import BaseModel

class UploadedDocument(BaseModel):
    document_id: str
    filename: str
    content_type: str | None
    size_bytes: int
    status: str

class AnalyzeDocumentRequest(BaseModel):
    document_id: str
