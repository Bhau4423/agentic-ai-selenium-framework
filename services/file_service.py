import json
from pathlib import Path


class FileService:

    @staticmethod
    def save_json(file_path, data):

        path = Path(file_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )