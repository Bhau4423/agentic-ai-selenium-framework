import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    MODEL_NAME = os.getenv("MODEL_NAME")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    MAX_REVIEW_CYCLES = 5

    TEMPERATURE = 0.1