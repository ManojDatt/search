from fastapi import FastAPI, Request
app = FastAPI()

@app.on_event("startup")
async def startup():
    """Connect to the database storage"""
    pass

@app.api_route('/api/search', include_in_schema=True)
async def searching(request: Request, search: str = None):
    return {'search': search}