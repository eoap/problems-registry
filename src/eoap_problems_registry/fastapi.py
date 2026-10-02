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

"""Expose registry problems as FastAPI exceptions and HTTP responses."""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import HTTPException
from fastapi.responses import Response

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

if TYPE_CHECKING:
    from fastapi.requests import Request


_PROBLEM_JSON_CONTENT_TYPE_: str = "Content-Type"


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
        headers[_PROBLEM_JSON_CONTENT_TYPE_] = "application/problem+json"
        self.headers = headers


class AlreadyExistsException(ProblemRegistryException):
    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(problem=AlreadyExists(instance=instance), errors=errors, headers=headers)


class BadRequestException(ProblemRegistryException):
    """Expose the BadRequest problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=BadRequest(instance=instance), errors=errors, headers=headers)


class BusinessRuleViolationException(ProblemRegistryException):
    """Expose the BusinessRuleViolation problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=BusinessRuleViolation(instance=instance), errors=errors, headers=headers
        )


class ConflictException(ProblemRegistryException):
    """Expose the Conflict problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=Conflict(instance=instance), errors=errors, headers=headers)


class FailedDependencyException(ProblemRegistryException):
    """Expose the FailedDependency problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=FailedDependency(instance=instance), errors=errors, headers=headers
        )


class ForbiddenException(ProblemRegistryException):
    """Expose the Forbidden problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=Forbidden(instance=instance), errors=errors, headers=headers)


class GoneException(ProblemRegistryException):
    """Expose the Gone problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=Gone(instance=instance), errors=errors, headers=headers)


class InsufficientStorageException(ProblemRegistryException):
    """Expose the InsufficientStorage problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=InsufficientStorage(instance=instance), errors=errors, headers=headers
        )


class InvalidBodyPropertyFormatException(ProblemRegistryException):
    """Expose the InvalidBodyPropertyFormat problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=InvalidBodyPropertyFormat(instance=instance), errors=errors, headers=headers
        )


class InvalidBodyPropertyValueException(ProblemRegistryException):
    """Expose the InvalidBodyPropertyValue problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=InvalidBodyPropertyValue(instance=instance), errors=errors, headers=headers
        )


class InvalidParametersException(ProblemRegistryException):
    """Expose the InvalidParameters problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=InvalidParameters(instance=instance), errors=errors, headers=headers
        )


class InvalidRequestHeaderFormatException(ProblemRegistryException):
    """Expose the InvalidRequestHeaderFormat problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=InvalidRequestHeaderFormat(instance=instance), errors=errors, headers=headers
        )


class InvalidRequestParameterFormatException(ProblemRegistryException):
    """Expose the InvalidRequestParameterFormat problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=InvalidRequestParameterFormat(instance=instance), errors=errors, headers=headers
        )


class InvalidRequestParameterValueException(ProblemRegistryException):
    """Expose the InvalidRequestParameterValue problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=InvalidRequestParameterValue(instance=instance), errors=errors, headers=headers
        )


class InvalidStateTransitionException(ProblemRegistryException):
    """Expose the InvalidStateTransition problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=InvalidStateTransition(instance=instance), errors=errors, headers=headers
        )


class LicenseCancelledException(ProblemRegistryException):
    """Expose the LicenseCancelled problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=LicenseCancelled(instance=instance), errors=errors, headers=headers
        )


class LicenseExpiredException(ProblemRegistryException):
    """Expose the LicenseExpired problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=LicenseExpired(instance=instance), errors=errors, headers=headers)


class MissingBodyPropertyException(ProblemRegistryException):
    """Expose the MissingBodyProperty problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=MissingBodyProperty(instance=instance), errors=errors, headers=headers
        )


class MissingRequestHeaderException(ProblemRegistryException):
    """Expose the MissingRequestHeader problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=MissingRequestHeader(instance=instance), errors=errors, headers=headers
        )


class MissingRequestParameterException(ProblemRegistryException):
    """Expose the MissingRequestParameter problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=MissingRequestParameter(instance=instance), errors=errors, headers=headers
        )


class MethodNotAllowedException(ProblemRegistryException):
    """Expose the MethodNotAllowed problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=MethodNotAllowed(instance=instance), errors=errors, headers=headers
        )


class NotAcceptableException(ProblemRegistryException):
    """Expose the NotAcceptable problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=NotAcceptable(instance=instance), errors=errors, headers=headers)


class NotFoundException(ProblemRegistryException):
    """Expose the NotFound problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=NotFound(instance=instance), errors=errors, headers=headers)


class NotImplementedException(ProblemRegistryException):
    """Expose the NotImplemented problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=NotImplemented(instance=instance), errors=errors, headers=headers)


class RequestTimeoutException(ProblemRegistryException):
    """Expose the RequestTimeout problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=RequestTimeout(instance=instance), errors=errors, headers=headers)


class ServerErrorException(ProblemRegistryException):
    """Expose the ServerError problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=ServerError(instance=instance), errors=errors, headers=headers)


class ServiceUnavailableException(ProblemRegistryException):
    """Expose the ServiceUnavailable problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=ServiceUnavailable(instance=instance), errors=errors, headers=headers
        )


class UnauthorizedException(ProblemRegistryException):
    """Expose the Unauthorized problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=Unauthorized(instance=instance), errors=errors, headers=headers)


class UnavailableForLegalReasonsException(ProblemRegistryException):
    """Expose the UnavailableForLegalReasons problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=UnavailableForLegalReasons(instance=instance), errors=errors, headers=headers
        )


class UnprocessableContentException(ProblemRegistryException):
    """Expose the UnprocessableContent problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(
            problem=UnprocessableContent(instance=instance), errors=errors, headers=headers
        )


class ValidationErrorException(ProblemRegistryException):
    """Expose the ValidationError problem as an HTTP exception."""

    def __init__(
        self,
        instance: str | None,
        errors: ErrorDetail | list[ErrorDetail] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            instance: URI reference identifying this occurrence, or ``None`` to omit it.
        """
        super().__init__(problem=ValidationError(instance=instance), errors=errors, headers=headers)


async def problem_registry_exception_handler(
    request: Request,
    exc: ProblemRegistryException,
) -> Response:
    """Return the serialized problem with its HTTP status and custom headers."""
    return Response(
        status_code=exc.status_code,
        content=exc.detail,
        media_type="application/problem+json",
        headers=exc.headers,
    )
