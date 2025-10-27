"""
FastAPI application for digittwin-config
"""

from fastapi import FastAPI

VERSION = "0.1.0"

app = FastAPI(
    title="Digittwin Config API",
    description="Configuration management API for Digital Twin",
    version=VERSION
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Digittwin Config API",
        "version": VERSION
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
