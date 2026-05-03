import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

LOG_PATH = Path(__file__).resolve().parents[1] / "storage" / "audit_log.jsonl"

class AuditLogService:
    def record(self, event_type: str, payload: dict[str, Any]) -> None:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        entry = {"timestamp": datetime.now(timezone.utc).isoformat(), "event_type": event_type, "payload": payload}
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

audit_log_service = AuditLogService()
