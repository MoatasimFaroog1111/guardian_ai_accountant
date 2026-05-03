from app.schemas.accounting import JournalDraft, JournalLine

class ExtractionService:
    def build_draft_from_document_reference(self, document_id: str, company_id: str | None) -> JournalDraft:
        return JournalDraft(
            company_id=company_id,
            currency="SAR",
            journal="Vendor Bills / Manual Review",
            status="draft",
            requires_approval=True,
            lines=[
                JournalLine(account_code="UNKNOWN_DR", account_name="Pending expense classification", debit=0, credit=0, memo=f"Document {document_id} requires extraction configuration"),
                JournalLine(account_code="UNKNOWN_CR", account_name="Pending payable classification", debit=0, credit=0, memo="No real posting in Phase 1"),
            ],
        )

extraction_service = ExtractionService()
