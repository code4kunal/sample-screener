from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from prometheus_client import make_asgi_app
import os

# Create FastAPI app
app = FastAPI(
    title="Stocksift API",
    description="Professional Stock Screener API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],  # Frontend and Grafana
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add trusted host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]  # In production, replace with specific hosts
)

# Add prometheus metrics
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

# Import and include routers
from src.auth.routes import router as auth_router
from src.users.routes import router as users_router
from src.screeners.routes import router as screeners_router
from src.analytics.routes import router as analytics_router
from src.cases.routes import router as cases_router
from src.payments.routes import router as payments_router
from src.admin.routes import router as admin_router

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(screeners_router, prefix="/screeners", tags=["Screeners"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
app.include_router(cases_router, prefix="/cases", tags=["Case Studies"])
app.include_router(payments_router, prefix="/payments", tags=["Payments"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Stocksift API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 