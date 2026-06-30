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

import unittest

from pydantic import ValidationError as PydanticValidationError

import eoap_problems_registry as registry


PROBLEM_MODEL_NAMES = {
    "AlreadyExists",
    "BadRequest",
    "BusinessRuleViolation",
    "Forbidden",
    "InvalidBodyPropertyFormat",
    "InvalidBodyPropertyValue",
    "InvalidParameters",
    "InvalidRequestHeaderFormat",
    "InvalidRequestParameterFormat",
    "InvalidRequestParameterValue",
    "LicenseCancelled",
    "LicenseExpired",
    "MissingBodyProperty",
    "MissingRequestHeader",
    "MissingRequestParameter",
    "NotFound",
    "ServerError",
    "ServiceUnavailable",
    "Unauthorized",
    "ValidationError",
}


class ProblemDetailsModelsTest(unittest.TestCase):
    def test_all_registry_problem_models_have_default_problem_fields(self):
        problem_models = {
            model.__name__: model for model in registry.ProblemDetails.__subclasses__()
        }

        self.assertEqual(set(problem_models), PROBLEM_MODEL_NAMES)

        for model_name, model_type in problem_models.items():
            with self.subTest(model=model_name):
                payload = model_type().model_dump(mode="json")

                self.assertTrue(
                    payload["type"].startswith(
                        "https://eoap.github.io/problems-registry/"
                    )
                )
                self.assertIsInstance(payload["status"], int)
                self.assertGreaterEqual(payload["status"], 400)
                self.assertLess(payload["status"], 600)
                self.assertIsInstance(payload["title"], str)
                self.assertGreater(len(payload["title"]), 0)
                self.assertIsInstance(payload["detail"], str)
                self.assertGreater(len(payload["detail"]), 0)

    def test_problem_model_serializes_context_errors_and_extension_fields(self):
        problem = registry.MissingRequestParameter(
            instance="https://api.example.test/problems/abc123",
            code="400-03",
            errors=[
                registry.ErrorDetail(
                    detail="The query parameter limit is required.",
                    parameter="limit",
                    provider_hint="Use limit=100 or less.",
                )
            ],
            correlation_id="req-123",
        )

        self.assertEqual(
            problem.model_dump(mode="json", exclude_none=True),
            {
                "instance": "https://api.example.test/problems/abc123",
                "code": "400-03",
                "errors": [
                    {
                        "detail": "The query parameter limit is required.",
                        "parameter": "limit",
                        "provider_hint": "Use limit=100 or less.",
                    }
                ],
                "type": "https://eoap.github.io/problems-registry/"
                "missing-request-parameter",
                "status": 400,
                "title": "Missing request parameter",
                "detail": "The request is missing an expected query or path parameter.",
                "correlation_id": "req-123",
            },
        )

    def test_problem_model_rejects_changed_literal_fields(self):
        with self.assertRaises(PydanticValidationError) as captured:
            registry.MissingBodyProperty(status=422)

        self.assertEqual(captured.exception.errors()[0]["loc"], ("status",))


if __name__ == "__main__":
    unittest.main()
