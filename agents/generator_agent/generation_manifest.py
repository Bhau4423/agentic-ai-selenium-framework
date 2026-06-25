import json

from pathlib import Path
from datetime import datetime


class GenerationManifest:

    _manifest = {

        "generated_pages": [],

        "generated_tests": [],

        "generated_at": "",

        "generator_version": "1.0"
    }

    @staticmethod
    def create():

        GenerationManifest._manifest = {

            "generated_pages": [],

            "generated_tests": [],

            "generated_at": datetime.now().isoformat(),

            "generator_version": "1.0"
        }

    @staticmethod
    def add_page(
        page_name: str
    ):

        if (
            page_name
            not in
            GenerationManifest._manifest[
                "generated_pages"
            ]
        ):

            GenerationManifest._manifest[
                "generated_pages"
            ].append(
                page_name
            )

    @staticmethod
    def add_test(
        test_name: str
    ):

        if (
            test_name
            not in
            GenerationManifest._manifest[
                "generated_tests"
            ]
        ):

            GenerationManifest._manifest[
                "generated_tests"
            ].append(
                test_name
            )

    @staticmethod
    def save():

        output_file = Path(
            "generated_framework/generation_manifest.json"
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(

                GenerationManifest._manifest,

                file,

                indent=4,

                ensure_ascii=False
            )

        return str(
            output_file
        )

    @staticmethod
    def load():

        manifest_file = Path(
            "generated_framework/generation_manifest.json"
        )

        if not manifest_file.exists():

            return {

                "generated_pages": [],

                "generated_tests": []
            }

        with open(
            manifest_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )