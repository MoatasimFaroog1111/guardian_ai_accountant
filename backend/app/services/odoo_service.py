from app.core.config import settings
from app.core.security import mask_secret

class OdooService:
    def status(self) -> dict:
        required = {
            "ODOO_URL": settings.odoo_url,
            "ODOO_DB": settings.odoo_db,
            "ODOO_USERNAME": settings.odoo_username,
            "ODOO_PASSWORD": settings.odoo_password,
            "ODOO_COMPANY_ID": settings.odoo_company_id,
        }
        missing = [name for name, value in required.items() if not value]
        return {
            "status": "configured" if not missing else "odoo_not_configured",
            "configured": not missing,
            "missing": missing,
            "secrets": {name: mask_secret(value) for name, value in required.items()},
            "posting_enabled": False,
            "phase": "Phase 1 - status only, no Odoo posting",
        }

odoo_service = OdooService()
