from pathlib import Path


class FrameworkStructureGenerator:

    @staticmethod
    def create():

        folders = [

            "generated_framework/base",

            "generated_framework/pages",

            "generated_framework/tests",

            "generated_framework/config",

            "generated_framework/utils",

            "generated_framework/data",

            "generated_framework/reports",

            "generated_framework/traceability"
        ]

        for folder in folders:

            Path(
                folder
            ).mkdir(
                parents=True,
                exist_ok=True
            )

        return folders