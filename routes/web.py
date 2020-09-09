"""Web Routes."""

from masonite.routes import Get, Post
from app.resources.UserResource import UserResource
from masonite.api.routes import JWTRoutes

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),
    Get('/api/test', 'ApiTestController@show'),
    Post('/api/test', 'ApiTestController@store'),
    UserResource('/api/users').routes(),
    JWTRoutes('/token'),
]

from masonite.auth import Auth 
ROUTES += Auth.routes()
