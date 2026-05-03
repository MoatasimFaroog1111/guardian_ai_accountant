from decimal import Decimal
from app.schemas.accounting import JournalDraft, ValidationResult

class AccountingValidationService:
    def validate(self, draft: JournalDraft) -> ValidationResult:
        errors: list[str] = []
        debit_total = sum((line.debit for line in draft.lines), Decimal("0"))
        credit_total = sum((line.credit for line in draft.lines), Decimal("0"))
        if debit_total != credit_total:
            errors.append("Debit total must equal credit total.")
        if not draft.currency:
            errors.append("Currency is required.")
        if not draft.company_id:
            errors.append("Company is required.")
        if not draft.requires_approval:
            errors.append("Journal entry cannot bypass human approval in Phase 1.")
        status = "ready_for_approval" if not errors else "validation_failed"
        return ValidationResult(is_valid=not errors, status=status, errors=errors, debit_total=debit_total, credit_total=credit_total)

accounting_validation_service = AccountingValidationService()
