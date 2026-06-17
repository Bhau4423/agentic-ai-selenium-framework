from pathlib import Path
import json

from models.page_mapping_model import (
    PageMapping
)


class RequirementMapper:

    @staticmethod
    def tokenize(text: str):

        if not text:
            return set()

        return {
            word.lower()
            for word in text.replace(
                "_",
                " "
            ).replace(
                "-",
                " "
            ).split()
            if len(word.strip()) > 2
        }

    @staticmethod
    def build_page_keywords(page):

        keywords = set()

        page_name = page.get(
            "page_name",
            ""
        )

        keywords.update(
            RequirementMapper.tokenize(
                page_name
            )
        )

        elements = page.get(
            "elements",
            []
        )

        for element in elements:

            keywords.update(
                RequirementMapper.tokenize(
                    element.get(
                        "element_name",
                        ""
                    )
                )
            )

            keywords.update(
                RequirementMapper.tokenize(
                    element.get(
                        "visible_text",
                        ""
                    )
                )
            )

            input_type = element.get(
                "input_type"
            )

            if input_type:

                keywords.add(
                    input_type.lower()
                )

        return keywords

    @staticmethod
    def create_mappings():

        requirement_file = Path(
            "data/intermediate/requirement_analysis.json"
        )

        inventory_file = Path(
            "output/page_inventory.json"
        )

        with open(
            requirement_file,
            "r",
            encoding="utf-8"
        ) as file:

            requirements_data = (
                json.load(file)
            )

        with open(
            inventory_file,
            "r",
            encoding="utf-8"
        ) as file:

            inventory_data = (
                json.load(file)
            )

        requirements = (
            requirements_data.get(
                "requirements",
                []
            )
        )

        pages = (
            inventory_data.get(
                "pages",
                []
            )
        )

        mappings = []

        for requirement in requirements:

            requirement_id = (
                requirement.get(
                    "id",
                    ""
                )
            )

            requirement_title = (
                requirement.get(
                    "title",
                    ""
                )
            )

            requirement_description = (
                requirement.get(
                    "description",
                    ""
                )
            )

            requirement_keywords = (
                RequirementMapper.tokenize(
                    requirement_title
                    + " "
                    + requirement_description
                )
            )

            best_page = None

            best_score = 0

            best_matches = []

            for page in pages:

                page_keywords = (
                    RequirementMapper.build_page_keywords(
                        page
                    )
                )

                matched_words = list(
                    requirement_keywords.intersection(
                        page_keywords
                    )
                )

                score = len(
                    matched_words
                )

                if score > best_score:

                    best_score = score

                    best_page = page

                    best_matches = matched_words

            if best_page:

                mappings.append(
                    PageMapping(
                        requirement_id=requirement_id,
                        requirement_title=requirement_title,
                        page_name=best_page.get(
                            "page_name",
                            ""
                        ),
                        page_url=best_page.get(
                            "url",
                            ""
                        ),
                        matched_elements=best_matches,
                        match_score=float(
                            best_score
                        )
                    )
                )

        return mappings