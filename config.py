from enum import StrEnum
from typing import Self

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(StrEnum):
    WEBKIT = 'webkit'
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow',
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    headless: bool = False
    browsers: list[Browser]
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath


    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath('./videos')
        tracing_dir = DirectoryPath('./tracing')
        allure_results_dir = DirectoryPath('./allure-results')

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir
        )


settings = Settings.initialize()
