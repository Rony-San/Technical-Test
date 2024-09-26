class CustomError(Exception):
    """Base exception for custom errors."""
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

class ServiceError(CustomError):
    """Exception for service errors."""
    def __init__(self, message, status_code=500):
        super().__init__(message, status_code)

class RouteError(CustomError):
    """Exception for route errors."""
    def __init__(self, message, status_code=400):
        super().__init__(message, status_code)
