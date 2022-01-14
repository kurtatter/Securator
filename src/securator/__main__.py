import uvicorn

from .settings import settings

uvicorn.run(
    'securator.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
