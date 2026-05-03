from decimal import Decimal
from pydantic import BaseModel, Field

class JournalLine(BaseModel):
    account_code: str
    account_name: str
    debit: Decimal = Field(default=Decimal("0"), ge=0)
    credit: Decimal = Field(default=Decimal("0"), ge=0)
    memo: str | None = None

class JournalDraft(BaseModel):
    company_id: str | None
    currency: str | None
    journal: str | None = None
    status: str = "draft"
    requires_approval: bool = True
    lines: list[JournalLine]

class ValidationResult(BaseModel):
    is_valid: bool
    status: str
    errors: list[str] = []
    debit_total: Decimal
    credit_total: Decimal
