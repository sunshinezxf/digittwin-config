"""
FastAPI application for digittwin-config
"""

from fastapi import FastAPI

app = FastAPI(
    title="Digittwin Config API",
    description="Configuration management API for Digital Twin",
    version="0.1.0"
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Digittwin Config API",
        "version": "0.1.0"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
