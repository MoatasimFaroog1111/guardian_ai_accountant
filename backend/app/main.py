from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_health import router as health_router
from app.api.routes_documents import router as documents_router
from app.api.routes_agent import router as agent_router
from app.api.routes_odoo import router as odoo_router

app = FastAPI(title='Guardian AI Accountant', version='0.1.0')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(health_router)
app.include_router(documents_router)
app.include_router(agent_router)
app.include_router(odoo_router)
