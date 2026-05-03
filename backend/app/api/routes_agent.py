from fastapi import APIRouter, HTTPException
from app.core.config import settings
from app.schemas.document import AnalyzeDocumentRequest
from app.services.document_service import document_service
from app.services.extraction_service import extraction_service
from app.services.accounting_validation_service import accounting_validation_service
from app.services.audit_log_service import audit_log_service

router = APIRouter(prefix='/api/agent', tags=['agent'])

@router.post('/analyze-document')
def analyze_document(request: AnalyzeDocumentRequest):
    path = document_service.find_document(request.document_id)
    if path is None:
        raise HTTPException(status_code=404, detail='Document not found')
    draft = extraction_service.build_draft_from_document_reference(request.document_id, settings.odoo_company_id)
    validation = accounting_validation_service.validate(draft)
    response = {'document_id': request.document_id, 'document_status': 'analyzed', 'draft': draft.model_dump(), 'validation': validation.model_dump()}
    audit_log_service.record('document_analyzed', {'document_id': request.document_id, 'validation_status': validation.status})
    return response
