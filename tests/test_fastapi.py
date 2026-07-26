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

import json
import unittest

from fastapi import HTTPException

import eoap_problems_registry as registry
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


if __name__ == "__main__":
    unittest.main()
