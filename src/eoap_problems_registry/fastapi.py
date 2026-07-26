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

from . import *
from fastapi import HTTPException

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
                | ValidationError
    ) -> None:
        self.status_code = problem.status
        self.detail = problem.model_dump_json(exclude_none=True)
        self.headers = {"Content-Type": "application/problem+json"}
