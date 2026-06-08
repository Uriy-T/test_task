from enum import StrEnum

"""
Классы тегов для построения иерархии в allure отчете.
System - название тестируемой системы
FunctionalityModule - название модуля/домена тестирования
Suite - название конкретного тестового набора в рамках функционального модуля/домена
"""


class System(StrEnum):
    TASK_MANAGER = 'Task manager'


class FunctionalityModule(StrEnum):
    AUTHORIZATION = 'Authentication'


class Suite(StrEnum):
    BASE_VALIDATION = 'Base validation'
