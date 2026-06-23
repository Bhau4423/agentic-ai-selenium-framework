import json
from pathlib import Path

from models.scenario_mapping_model import (
    ScenarioMapping
)

from models.semantic_element_model import (
    SemanticElement
)

from agents.generator_agent.semantic_dictionary import (
    SemanticDictionary
)

class ScenarioMapper:

    PAGE_NAME_WEIGHT = 10
    URL_WEIGHT = 8
    ELEMENT_NAME_WEIGHT = 5
    VISIBLE_TEXT_WEIGHT = 5
    LABEL_WEIGHT = 4
    PLACEHOLDER_WEIGHT = 4
    FORM_WEIGHT = 3
    LINK_WEIGHT = 2
    TABLE_WEIGHT = 2

    @staticmethod
    def tokenize(text: str):

        if not text:
            return set()

        text = (
            text.lower()
            .replace("_", " ")
            .replace("-", " ")
            .replace("/", " ")
        )

        return {

            word.strip()

            for word in text.split()

            if len(word.strip()) > 2
        }

    @staticmethod
    def load_requirements():

        with open(
            "data/intermediate/requirement_analysis.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def load_inventory():

        with open(
            "output/page_inventory.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def get_all_scenarios():

        data = (
            ScenarioMapper
            .load_requirements()
        )

        scenarios = []

        scenarios.extend(
            data.get(
                "positive_scenarios",
                []
            )
        )

        scenarios.extend(
            data.get(
                "negative_scenarios",
                []
            )
        )

        scenarios.extend(
            data.get(
                "boundary_scenarios",
                []
            )
        )

        return scenarios

    @staticmethod
    def calculate_element_score(
        scenario_keywords,
        element
    ):

        score = 0

        text_parts = [

            str(
                element.get(
                    "element_name",
                    ""
                )
            ),

            str(
                element.get(
                    "visible_text",
                    ""
                )
            ),

            str(
                element.get(
                    "label",
                    ""
                )
            ),

            str(
                element.get(
                    "placeholder",
                    ""
                )
            ),

            str(
                element.get(
                    "aria_label",
                    ""
                )
            )
        ]

        element_text = (
            " ".join(
                text_parts
            )
        )

        element_keywords = (
            ScenarioMapper.tokenize(
                element_text
            )
        )

        common = (
            scenario_keywords.intersection(
                element_keywords
            )
        )

        if not common:

            return 0

        score += (
            len(common)
            * ScenarioMapper.ELEMENT_NAME_WEIGHT
        )

        return score

    @staticmethod
    def calculate_page_score(
        scenario_keywords,
        page
    ):

        score = 0

        matched_elements = []

        page_name = (
            page.get(
                "page_name",
                ""
            )
        )

        page_keywords = (
            ScenarioMapper.tokenize(
                page_name
            )
        )

        common = (
            scenario_keywords.intersection(
                page_keywords
            )
        )

        score += (
            len(common)
            * ScenarioMapper.PAGE_NAME_WEIGHT
        )

        page_url = (
            page.get(
                "url",
                ""
            )
        )

        url_keywords = (
            ScenarioMapper.tokenize(
                page_url
            )
        )

        common = (
            scenario_keywords.intersection(
                url_keywords
            )
        )

        score += (
            len(common)
            * ScenarioMapper.URL_WEIGHT
        )

        for element in page.get(
            "elements",
            []
        ):

            element_score = (
                ScenarioMapper
                .calculate_element_score(
                    scenario_keywords,
                    element
                )
            )

            if element_score > 0:

                score += (
                    element_score
                )

                confidence = min(
                    100.0,
                    float(
                        element_score
                        * 10
                    )
                )

                matched_elements.append(

                    SemanticElement(

                        element_name=
                        element.get(
                            "element_name",
                            ""
                        ),

                        element_type=
                        element.get(
                            "element_type",
                            ""
                        ),

                        locator=
                        element.get(
                            "locator",
                            {}
                        ),

                        confidence_score=
                        confidence
                    )
                )

        for form in page.get(
            "forms",
            []
        ):

            form_name = (
                form.get(
                    "form_name",
                    ""
                )
            )

            form_keywords = (
                ScenarioMapper.tokenize(
                    form_name
                )
            )

            common = (
                scenario_keywords.intersection(
                    form_keywords
                )
            )

            score += (
                len(common)
                * ScenarioMapper.FORM_WEIGHT
            )

        for link in page.get(
            "links",
            []
        ):

            link_text = (
                link.get(
                    "text",
                    ""
                )
            )

            link_keywords = (
                ScenarioMapper.tokenize(
                    link_text
                )
            )

            common = (
                scenario_keywords.intersection(
                    link_keywords
                )
            )

            score += (
                len(common)
                * ScenarioMapper.LINK_WEIGHT
            )

        for table in page.get(
            "tables",
            []
        ):

            for header in table.get(
                "headers",
                []
            ):

                header_keywords = (
                    ScenarioMapper.tokenize(
                        header
                    )
                )

                common = (
                    scenario_keywords.intersection(
                        header_keywords
                    )
                )

                score += (
                    len(common)
                    * ScenarioMapper.TABLE_WEIGHT
                )

        return (
            score,
            matched_elements
        )

    @staticmethod
    def map_scenarios():

        inventory = (
            ScenarioMapper
            .load_inventory()
        )

        pages = (
            inventory.get(
                "pages",
                []
            )
        )

        scenarios = (
            ScenarioMapper
            .get_all_scenarios()
        )

        mappings = []

        for scenario in scenarios:

            scenario_text = (

                scenario.get(
                    "title",
                    ""
                )

                + " "

                + " ".join(

                    scenario.get(
                        "steps",
                        []
                    )

                )

            )

            scenario_keywords = (
                ScenarioMapper.tokenize(
                    scenario_text
                )
            )

            scenario_keywords = (
                SemanticDictionary.expand_keywords(
                    scenario_keywords
                )
            )

            best_page = None

            best_score = 0

            best_elements = []

            for page in pages:

                (
                    page_score,
                    page_elements
                ) = (

                    ScenarioMapper
                    .calculate_page_score(
                        scenario_keywords,
                        page
                    )

                )

                if page_score > best_score:

                    best_score = (
                        page_score
                    )

                    best_page = page

                    best_elements = (
                        page_elements
                    )

            if (
                best_page
                and
                best_score > 0
            ):


                    element_count = len(
                        best_elements
                   )

# --------------------------------
# PAGE CONFIDENCE
# --------------------------------

                    page_confidence = min(
                        round(
                            best_score / 20,
                            2
                        ),
                        1.0
                    )

# --------------------------------
# ELEMENT CONFIDENCE
# --------------------------------

                    element_confidence = min(
                        round(
                            element_count / 3,
                            2
                        ),
                        1.0
                    )

# --------------------------------
# FINAL CONFIDENCE
# --------------------------------

                    confidence_score = round(
                        (
                            page_confidence * 0.6
                            +
                            element_confidence * 0.4
                        ),
                        2
                    )

                    if confidence_score >= 0.85:

                        mapping_quality = (
                            "HIGH"
                        )

                    elif confidence_score >= 0.50:

                        mapping_quality = (
                            "MEDIUM"
                        )

                    else:

                        mapping_quality = (
                            "LOW"
                        )

                    mappings.append(

                        ScenarioMapping(

                            scenario_id=
                            scenario.get(
                                "id",
                                ""
                            ),

                            scenario_title=
                            scenario.get(
                                "title",
                                ""
                           ),

                            scenario_type=
                            scenario.get(
                                "scenario_type",
                                ""
                            ),

                            page_name=
                            best_page.get(
                                "page_name",
                                ""
                            ),

                            page_url=
                            best_page.get(
                                "url",
                                ""
                            ),

                            confidence_score=
                            confidence_score,

                            mapping_quality=
                            mapping_quality,

                            matched_elements=
                            best_elements
                        )
                    )
                

            else:

                print(
                    f"No mapping found: "
                    f"{scenario.get('id')} "
                    f"{scenario.get('title')}"
                )

        return mappings

    @staticmethod
    def save_mappings(
        mappings
    ):

        output_file = Path(
            "data/intermediate/scenario_mapping.json"
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
                [
                    mapping.model_dump()
                    for mapping
                    in mappings
                ],
                file,
                indent=4
            )

        print(
            f"\nScenario Mapping saved: "
            f"{output_file}"
        )

        return str(
            output_file
        )