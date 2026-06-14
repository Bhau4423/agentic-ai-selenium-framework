from pathlib import Path


class PromptBuilder:

    @staticmethod
    def build_prompt(requirement_document: str):

        prompt_path = (
            Path("prompts")
            / "requirement_analysis_prompt.txt"
        )

        template = prompt_path.read_text(
            encoding="utf-8"
        )

        return template.replace(
            "{requirement_document}",
            requirement_document
        )