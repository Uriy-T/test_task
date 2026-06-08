from enum import StrEnum

"""
Теги базовой классификации тестов
"""


class ModuleForTesting(StrEnum):
    AUTHORIZATION = 'AUTHORIZATION_TESTS'


class SeverityTest(StrEnum):
    BLOCKER = 'BLOCKER'
    CRITICAL = 'CRITICAL'
    MAJOR = 'MAJOR'
    MINOR = 'MINOR'
    TRIVIAL = 'TRIVIAL'


class TypeTest(StrEnum):
    NEGATIVE = 'NEGATIVE_TEST'
    POSITIVE = 'POSITIVE_TEST'
