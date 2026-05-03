from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()

@router.get('/health')
def health():
    return {'status': 'ok', 'service': 'Guardian AI Accountant API', 'timestamp': datetime.now(timezone.utc).isoformat(), 'phase': '1'}
