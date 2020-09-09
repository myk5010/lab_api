"""User Model."""

from config.database import Model


class User(Model):
    """User Model."""

    __table__ = 'user'

    __fillable__ = ['name', 'email', 'password']

    __auth__ = 'email'
