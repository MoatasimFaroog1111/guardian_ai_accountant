from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
from app.schemas.document import UploadedDocument
from app.services.audit_log_service import audit_log_service

UPLOAD_DIR = Path(__file__).resolve().parents[1] / "storage" / "uploads"

class DocumentService:
    async def save_upload(self, file: UploadFile) -> UploadedDocument:
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        document_id = str(uuid4())
        safe_name = Path(file.filename or "document.bin").name
        target = UPLOAD_DIR / f"{document_id}_{safe_name}"
        data = await file.read()
        target.write_bytes(data)
        result = UploadedDocument(document_id=document_id, filename=safe_name, content_type=file.content_type, size_bytes=len(data), status="uploaded")
        audit_log_service.record("document_uploaded", result.model_dump())
        return result

    def find_document(self, document_id: str) -> Path | None:
        matches = list(UPLOAD_DIR.glob(f"{document_id}_*"))
        return matches[0] if matches else None

document_service = DocumentService()
