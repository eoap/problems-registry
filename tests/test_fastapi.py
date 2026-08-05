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

import inspect
import json
import unittest

from fastapi import HTTPException

import eoap_problems_registry as registry
import eoap_problems_registry.fastapi as fastapi_registry
from eoap_problems_registry.fastapi import ProblemRegistryException


class ProblemRegistryExceptionTest(unittest.TestCase):
    def setUp(self):
        self.problem = registry.MissingRequestParameter(
            instance="https://api.example.test/problems/abc123",
            code="400-03",
            errors=[
                registry.ErrorDetail(
                    detail="The query parameter limit is required.",
                    parameter="limit",
                )
            ],
        )

        self.exception = ProblemRegistryException(problem=self.problem)

    def test_is_an_http_exception_with_the_problem_status(self):
        self.assertIsInstance(self.exception, HTTPException)
        self.assertEqual(self.exception.status_code, self.problem.status)

    def test_serializes_the_problem_as_the_exception_detail(self):
        self.assertIsInstance(self.exception.detail, str)
        self.assertEqual(
            json.loads(self.exception.detail),
            self.problem.model_dump(mode="json", exclude_none=True),
        )

    def test_uses_the_problem_json_content_type(self):
        self.assertEqual(
            self.exception.headers,
            {"Content-Type": "application/problem+json"},
        )


class DeclaredProblemRegistryExceptionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exception_types = [
            exception_type
            for _, exception_type in inspect.getmembers(
                fastapi_registry,
                inspect.isclass,
            )
            if exception_type.__module__ == fastapi_registry.__name__
            and exception_type is not ProblemRegistryException
            and issubclass(exception_type, ProblemRegistryException)
            and exception_type.__name__.endswith("Exception")
        ]

    def test_each_declared_exception_reflects_its_related_problem_model(self):
        self.assertGreater(len(self.exception_types), 0)

        for exception_type in self.exception_types:
            with self.subTest(exception=exception_type.__name__):
                problem_model_name = exception_type.__name__.removesuffix("Exception")
                problem_model_type = getattr(registry, problem_model_name)

                problem = problem_model_type()
                exception = exception_type()

                self.assertIsInstance(exception, HTTPException)
                self.assertEqual(exception.status_code, problem.status)
                self.assertEqual(
                    json.loads(exception.detail),
                    problem.model_dump(mode="json", exclude_none=True),
                )
                self.assertEqual(
                    exception.headers,
                    {"Content-Type": "application/problem+json"},
                )

    def test_each_declared_exception_sets_a_single_error(self):
        error = registry.ErrorDetail(
            detail="The supplied value is invalid.",
            parameter="limit",
        )
        expected_errors = [error.model_dump(mode="json", exclude_none=True)]

        for exception_type in self.exception_types:
            with self.subTest(exception=exception_type.__name__):
                exception = exception_type(errors=error)
                detail = json.loads(exception.detail)

                self.assertEqual(detail["errors"], expected_errors)

    def test_each_declared_exception_sets_multiple_errors(self):
        errors = [
            registry.ErrorDetail(
                detail="The supplied value is invalid.",
                parameter="limit",
            ),
            registry.ErrorDetail(
                detail="The supplied header is invalid.",
                header="X-Request-ID",
            ),
        ]
        expected_errors = [
            error.model_dump(mode="json", exclude_none=True) for error in errors
        ]

        for exception_type in self.exception_types:
            with self.subTest(exception=exception_type.__name__):
                exception = exception_type(errors=errors)
                detail = json.loads(exception.detail)

                self.assertEqual(detail["errors"], expected_errors)

    def test_each_declared_exception_merges_custom_headers(self):
        headers = {
            "X-Request-ID": "abc123",
            "Content-Type": "text/plain",
        }

        for exception_type in self.exception_types:
            with self.subTest(exception=exception_type.__name__):
                exception = exception_type(headers=headers)

                self.assertEqual(
                    exception.headers,
                    {
                        "X-Request-ID": "abc123",
                        "Content-Type": "application/problem+json",
                    },
                )
                self.assertEqual(
                    headers,
                    {
                        "X-Request-ID": "abc123",
                        "Content-Type": "text/plain",
                    },
                )


if __name__ == "__main__":
    unittest.main()
