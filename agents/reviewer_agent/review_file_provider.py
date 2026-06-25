from pathlib import Path

from agents.generator_agent.generation_manifest import (
    GenerationManifest
)


class ReviewFileProvider:

    @staticmethod
    def get_generated_test_files():

        manifest = (
            GenerationManifest.load()
        )

        files = []

        for file_name in manifest.get(
            "generated_tests",
            []
        ):

            file_path = (
                Path(
                    "generated_framework/tests"
                )
                / file_name
            )

            if file_path.exists():

                files.append(
                    file_path
                )

        return files

    @staticmethod
    def get_generated_page_files():

        manifest = (
            GenerationManifest.load()
        )

        files = []

        for file_name in manifest.get(
            "generated_pages",
            []
        ):

            file_path = (
                Path(
                    "generated_framework/pages"
                )
                / file_name
            )

            if file_path.exists():

                files.append(
                    file_path
                )

        return files