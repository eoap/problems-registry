# Copyright 2026 EOAP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from fastapi import HTTPException

from . import (
    AlreadyExists,
    BadRequest,
    BusinessRuleViolation,
    Conflict,
    ErrorDetail,
    FailedDependency,
    Forbidden,
    Gone,
    InsufficientStorage,
    InvalidBodyPropertyFormat,
    InvalidBodyPropertyValue,
    InvalidParameters,
    InvalidRequestHeaderFormat,
    InvalidRequestParameterFormat,
    InvalidRequestParameterValue,
    InvalidStateTransition,
    LicenseCancelled,
    LicenseExpired,
    MethodNotAllowed,
    MissingBodyProperty,
    MissingRequestHeader,
    MissingRequestParameter,
    NotAcceptable,
    NotFound,
    NotImplemented,
    RequestTimeout,
    ServerError,
    ServiceUnavailable,
    Unauthorized,
    UnavailableForLegalReasons,
    UnprocessableContent,
    ValidationError,
)


class ProblemRegistryException(HTTPException):
    def __init__(
        self,
        *,
        problem: AlreadyExists
        | BadRequest
        | BusinessRuleViolation
        | Conflict
        | FailedDependency
        | Forbidden
        | Gone
        | InsufficientStorage
        | InvalidBodyPropertyFormat
        | InvalidBodyPropertyValue
        | InvalidParameters
        | InvalidRequestHeaderFormat
        | InvalidRequestParameterFormat
        | InvalidRequestParameterValue
        | InvalidStateTransition
        | LicenseCancelled
        | LicenseExpired
        | MissingBodyProperty
        | MissingRequestHeader
        | MissingRequestParameter
        | MethodNotAllowed
        | NotAcceptable
        | NotFound
        | NotImplemented
        | RequestTimeout
        | ServerError
        | ServiceUnavailable
        | Unauthorized
        | UnavailableForLegalReasons
        | UnprocessableContent
        | ValidationError,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
    ) -> None:
        self.status_code = problem.status

        if errors:
            if isinstance(errors, list):
                problem.errors = errors
            else:
                problem.errors = [errors]
        self.detail = problem.model_dump_json(exclude_none=True)

        self.headers = {"Content-Type": "application/problem+json"}


class AlreadyExistsException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=AlreadyExists(), errors=errors)


class BadRequestException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=BadRequest(), errors=errors)


class BusinessRuleViolationException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=BusinessRuleViolation(), errors=errors)


class ConflictException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=Conflict(), errors=errors)


class FailedDependencyException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=FailedDependency(), errors=errors)


class ForbiddenException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=Forbidden(), errors=errors)


class GoneException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=Gone(), errors=errors)


class InsufficientStorageException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=InsufficientStorage(), errors=errors)


class InvalidBodyPropertyFormatException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=InvalidBodyPropertyFormat(), errors=errors)


class InvalidBodyPropertyValueException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=InvalidBodyPropertyValue(), errors=errors)


class InvalidParametersException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=InvalidParameters(), errors=errors)


class InvalidRequestHeaderFormatException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=InvalidRequestHeaderFormat(), errors=errors)


class InvalidRequestParameterFormatException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=InvalidRequestParameterFormat(), errors=errors)


class InvalidRequestParameterValueException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=InvalidRequestParameterValue(), errors=errors)


class InvalidStateTransitionException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=InvalidStateTransition(), errors=errors)


class LicenseCancelledException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=LicenseCancelled(), errors=errors)


class LicenseExpiredException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=LicenseExpired(), errors=errors)


class MissingBodyPropertyException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=MissingBodyProperty(), errors=errors)


class MissingRequestHeaderException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=MissingRequestHeader(), errors=errors)


class MissingRequestParameterException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=MissingRequestParameter(), errors=errors)


class MethodNotAllowedException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=MethodNotAllowed(), errors=errors)


class NotAcceptableException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=NotAcceptable(), errors=errors)


class NotFoundException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=NotFound(), errors=errors)


class NotImplementedException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=NotImplemented(), errors=errors)


class RequestTimeoutException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=RequestTimeout(), errors=errors)


class ServerErrorException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=ServerError(), errors=errors)


class ServiceUnavailableException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=ServiceUnavailable(), errors=errors)


class UnauthorizedException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=Unauthorized(), errors=errors)


class UnavailableForLegalReasonsException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=UnavailableForLegalReasons(), errors=errors)


class UnprocessableContentException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=UnprocessableContent(), errors=errors)


class ValidationErrorException(ProblemRegistryException):
    def __init__(self, errors: ErrorDetail | list[ErrorDetail] | None = None) -> None:
        super().__init__(problem=ValidationError(), errors=errors)
