from fastapi import APIRouter, UploadFile, File
from app.services.document_service import document_service

router = APIRouter(prefix='/api/documents', tags=['documents'])

@router.post('/upload')
async def upload_document(file: UploadFile = File(...)):
    return await document_service.save_upload(file)
