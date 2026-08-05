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
        headers: dict[str, str] | None = None,
    ) -> None:
        self.status_code = problem.status

        if errors:
            if isinstance(errors, list):
                problem.errors = errors
            else:
                problem.errors = [errors]
        self.detail = problem.model_dump_json(exclude_none=True)

        headers = (headers or {}).copy()
        headers["Content-Type"] = "application/problem+json"
        self.headers = headers


class AlreadyExistsException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=AlreadyExists(), errors=errors, headers=headers)


class BadRequestException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=BadRequest(), errors=errors, headers=headers)


class BusinessRuleViolationException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            problem=BusinessRuleViolation(), errors=errors, headers=headers
        )


class ConflictException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=Conflict(), errors=errors, headers=headers)


class FailedDependencyException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=FailedDependency(), errors=errors, headers=headers)


class ForbiddenException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=Forbidden(), errors=errors, headers=headers)


class GoneException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=Gone(), errors=errors, headers=headers)


class InsufficientStorageException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=InsufficientStorage(), errors=errors, headers=headers)


class InvalidBodyPropertyFormatException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            problem=InvalidBodyPropertyFormat(), errors=errors, headers=headers
        )


class InvalidBodyPropertyValueException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            problem=InvalidBodyPropertyValue(), errors=errors, headers=headers
        )


class InvalidParametersException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=InvalidParameters(), errors=errors, headers=headers)


class InvalidRequestHeaderFormatException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            problem=InvalidRequestHeaderFormat(), errors=errors, headers=headers
        )


class InvalidRequestParameterFormatException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            problem=InvalidRequestParameterFormat(), errors=errors, headers=headers
        )


class InvalidRequestParameterValueException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            problem=InvalidRequestParameterValue(), errors=errors, headers=headers
        )


class InvalidStateTransitionException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            problem=InvalidStateTransition(), errors=errors, headers=headers
        )


class LicenseCancelledException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=LicenseCancelled(), errors=errors, headers=headers)


class LicenseExpiredException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=LicenseExpired(), errors=errors, headers=headers)


class MissingBodyPropertyException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=MissingBodyProperty(), errors=errors, headers=headers)


class MissingRequestHeaderException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=MissingRequestHeader(), errors=errors, headers=headers)


class MissingRequestParameterException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            problem=MissingRequestParameter(), errors=errors, headers=headers
        )


class MethodNotAllowedException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=MethodNotAllowed(), errors=errors, headers=headers)


class NotAcceptableException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=NotAcceptable(), errors=errors, headers=headers)


class NotFoundException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=NotFound(), errors=errors, headers=headers)


class NotImplementedException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=NotImplemented(), errors=errors, headers=headers)


class RequestTimeoutException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=RequestTimeout(), errors=errors, headers=headers)


class ServerErrorException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=ServerError(), errors=errors, headers=headers)


class ServiceUnavailableException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=ServiceUnavailable(), errors=errors, headers=headers)


class UnauthorizedException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=Unauthorized(), errors=errors, headers=headers)


class UnavailableForLegalReasonsException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            problem=UnavailableForLegalReasons(), errors=errors, headers=headers
        )


class UnprocessableContentException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=UnprocessableContent(), errors=errors, headers=headers)


class ValidationErrorException(ProblemRegistryException):
    def __init__(
        self,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=ValidationError(), errors=errors, headers=headers)
