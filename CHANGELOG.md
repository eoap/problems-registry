# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

- Stronger code chekers with Ruff+McCabe & Bandit

### Deprecated

### Removed

### Fixed

### Security

[1.2.0] - 2026-07-26

### Added

- New _Common Problem_ details and reponses:
  - `405` Method Not Allowed
  - `406` Not Acceptable
  - `408` Request Timeout
  - `409` Conflict
  - `422` Unprocessable Content
  - `424` Failed Dependency
  - `451` Unavailable For Legal Reasons
  - `501` Not Implemented
  - `507` Insufficient
- [FastAPI](https://fastapi.tiangolo.com/) integration.

[1.1.0] - 2026-07-23

### Added

- `Gone` as new problem detail and reponse.

[1.0.1] - 2026-07-20

### Fixed

- Generated models solve Pydantic/Pylance [issue](https://github.com/pydantic/pydantic/discussions/7379)

[1.0.0] - 2026-07-17

### Added

- Initial version

[Unreleased]: https://github.com/eoap/problems-registry/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/eoap/problems-registry/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/eoap/problems-registry/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/eoap/problems-registry/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/eoap/problems-registry/releases/tag/v1.0.0
