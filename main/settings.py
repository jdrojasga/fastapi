"""Module with the settings for the Apis application."""
from pydantic import Field
from pydantic_settings import BaseSettings

class ApisSettings(BaseSettings):
    """Settings for the Apis application."""
    
    class Config:
        """Configuration for the settings."""
        env_file = ".env"
        env_file_encoding = "utf-8"


# settings for OpenAI API
class OpenAISettings(ApisSettings):
    """Settings for the OpenAI API.
    
    Attributes:
        api_key (str): The API key for OpenAI.
    """

    api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")