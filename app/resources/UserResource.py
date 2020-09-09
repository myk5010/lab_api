from masonite.api.resources import Resource
from app.User import User
from masonite.api.serializers import JSONSerializer
# jwt身份验证
from masonite.api.authentication import JWTAuthentication


class UserResource(Resource, JSONSerializer, JWTAuthentication):
  model = User
  # 定义要创建的路由
  methods = ['create', 'index', 'show']
  # 排除不想返回的字段
  without = ['id', 'email', 'password']
