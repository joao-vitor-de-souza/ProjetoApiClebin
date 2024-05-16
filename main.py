from fastapi import FastAPI
from CORE.configs import settings
from API.v1.api import api_router

app = FastAPI(title='API de Cursos da ETS')
app.include_router(api_router, prefix=settings.AP1_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level='info', reload=True)