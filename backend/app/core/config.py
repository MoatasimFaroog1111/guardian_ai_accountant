from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "development"
    app_secret_key: str = "change-me"
    odoo_url: str | None = None
    odoo_db: str | None = None
    odoo_username: str | None = None
    odoo_password: str | None = None
    odoo_company_id: str | None = None
    azure_document_intelligence_endpoint: str | None = None
    azure_document_intelligence_key: str | None = None
    openai_api_key: str | None = None

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
