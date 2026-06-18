from pathlib import Path


class ConfigGenerator:

    @staticmethod
    def generate():

        lines = []

        lines.append(
            "browser=chrome"
        )

        lines.append("")

        lines.append(
            "baseUrl=https://practicetestautomation.com/practice-test-login/"
        )

        lines.append("")

        lines.append(
            "timeout=10"
        )

        return "\n".join(lines)

    @staticmethod
    def save():

        output_dir = Path(
            "generated_framework/config"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = (
            output_dir
            / "config.properties"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                ConfigGenerator.generate()
            )

        return str(file_path)