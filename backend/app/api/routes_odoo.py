from fastapi import APIRouter
from app.services.odoo_service import odoo_service

router = APIRouter(prefix='/api/odoo', tags=['odoo'])

@router.get('/status')
def odoo_status():
    return odoo_service.status()
