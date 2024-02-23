import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from settings import base as settings

from admin import init_admin_panel
from api import routers
from settings.db import Base, engine


def create_app() -> FastAPI:
    app = FastAPI(
        title='Wordle',
        docs_url='/docs',
        swagger_ui_parameters={'deepLinking': False, 'persistAuthorization': True},
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOW_ORIGINS,
        allow_credentials=settings.ALLOW_CREDENTIALS,
        allow_methods=settings.ALLOW_METHODS,
        allow_headers=settings.ALLOW_HEADERS,
        expose_headers=settings.EXPOSE_HEADERS,
    )

    for router in routers:
        app.include_router(router)

    init_admin_panel(app=app, engine=engine)

    @app.on_event('startup')
    async def startup() -> None:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    return app


app_ = create_app()


if __name__ == '__main__':
    uvicorn.run('app:app_', reload=True, port=8000)
