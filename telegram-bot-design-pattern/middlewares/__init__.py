"""middlewares are object that processes a message. The message will be then returned
   and processed by the normal functions.
"""

from ._example_middleware import ExampleMiddleware

__all__ = ['ExampleMiddleware']

