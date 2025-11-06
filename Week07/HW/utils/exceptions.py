class AppError(Exception):
    pass

class InvalidDateError(AppError):
    pass

class InvalidIdError(AppError):
    pass

class NotFoundError(AppError):
    pass

class PermissionDeniedError(AppError):
    pass

class SeatNotAvailableError(AppError):
    pass

class CapacityConflictError(AppError):
    pass

class PaymentFailedError(AppError):
    pass
