from langchain_google_genai import ChatGoogleGenerativeAI

from configs.settings import Settings


class LLMService:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=Settings.MODEL_NAME,
            google_api_key=Settings.GEMINI_API_KEY,
            temperature=Settings.TEMPERATURE
        )

    def invoke(self, prompt: str):

        response = self.llm.invoke(prompt)

        content = response.content

        # Gemini returning content blocks
        if isinstance(content, list):

            text_parts = []

            for block in content:

                if isinstance(block, dict):
                    text_parts.append(block.get("text", ""))

            return "\n".join(text_parts)

        return str(content)