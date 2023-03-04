from app.configuration.routes.routes import Routes
from app.internal.routes import objects

__routes__ = Routes(routers=(objects.router, ))