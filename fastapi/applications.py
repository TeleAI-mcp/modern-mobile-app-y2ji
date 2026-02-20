"""
FastAPI applications.
"""

from typing import Any, AsyncGenerator, AsyncIterator, Dict, List, Sequence

from fastapi import routing
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.middleware import Middleware
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.openapi.utils import get_openapi
from fastapi.params import Depends
from fastapi.types import ASGIApp, IncEx


class FastAPI:
    """
    The main **FastAPI** class.

    You would usually create an instance of this class as the main entry point
    for your application.

    ## Example

    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    ```
    """

    def __init__(
        self,
        *,
        debug: bool = False,
        routes: List[routing.BaseRoute] = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: str = "/openapi.json",
        openapi_tags: List[Dict[str, Any]] = None,
        servers: List[Dict[str, str | Any]] = None,
        dependencies: Sequence[Depends] = None,
        default_response_class: type = Default(JSONResponse),
        docs_url: str | None = "/docs",
        redoc_url: str | None = "/redoc",
        swagger_ui_oauth2_redirect_url: str | None = "/docs/oauth2-redirect",
        swagger_ui_init_oauth: Dict[str, Any] | None = None,
        middleware: Sequence[Middleware] = None,
        exception_handlers: Dict[Any, Any] | None = None,
        on_startup: List[Callable[[], Any]] = None,
        on_shutdown: List[Callable[[], Any]] = None,
        terms_of_service: str | None = None,
        contact: Dict[str, Any] | None = None,
        license_info: Dict[str, Any] | None = None,
        openapi_prefix: str = "",
        root_path: str = "",
        root_path_in_servers: bool = True,
        responses: Dict[int | str, Dict[str, Any]] = None,
        callbacks: List[Dict[str, Any]] = None,
        webhooks: Dict[str, Any] = None,
        deprecated: bool | None = None,
        include_in_schema: bool = True,
        swagger_ui_parameters: Dict[str, Any] | None = None,
        asyncio_mode: str | None = None,
    ) -> None:
        # ... implementation details ...
        pass

    def add_middleware(
        self,
        middleware_class: type,
        **options: Any,
    ) -> None:
        """
        Add middleware to the application.
        """
        pass

    def include_router(
        self,
        router: routing.APIRouter,
        *,
        prefix: str = "",
        tags: List[str] = None,
        dependencies: Sequence[Depends] = None,
        responses: Dict[int | str, Dict[str, Any]] = None,
        deprecated: bool | None = None,
        include_in_schema: bool = True,
        default_response_class: type = Default(JSONResponse),
        callbacks: List[Dict[str, Any]] = None,
        generate_unique_id_function: Callable[[routing.APIRoute], str] = Default(
            default_generate_unique_id
        ),
    ) -> None:
        """
        Include an APIRouter in the application.
        """
        pass

    def mount(
        self,
        path: str,
        app: ASGIApp,
        name: str = None,
    ) -> None:
        """
        Mount an ASGI application at a specific path.
        """
        pass

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        The main ASGI callable.
        """
        pass
