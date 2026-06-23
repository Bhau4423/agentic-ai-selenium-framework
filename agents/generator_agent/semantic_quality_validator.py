import json
from pathlib import Path

from models.semantic_validation_model import (
    SemanticValidationFinding
)


class SemanticQualityValidator:

    @staticmethod
    def load_scenario_mappings():

        mapping_file = Path(
            "data/intermediate/scenario_mapping.json"
        )

        with open(
            mapping_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )

    @staticmethod
    def validate():

        mappings = (
            SemanticQualityValidator
            .load_scenario_mappings()
        )

        findings = []

        for mapping in mappings:

            scenario_id = (
                mapping.get(
                    "scenario_id",
                    ""
                )
            )

            scenario_title = (
                mapping.get(
                    "scenario_title",
                    ""
                )
            )

            confidence_score = (
                mapping.get(
                    "confidence_score",
                    0
                )
            )

            mapping_quality = (
                mapping.get(
                    "mapping_quality",
                    ""
                )
            )

            matched_elements = (
                mapping.get(
                    "matched_elements",
                    []
                )
            )

            # -------------------------
            # RULE 1
            # No Element Coverage
            # -------------------------

            if len(
                matched_elements
            ) == 0:

                findings.append(

                    SemanticValidationFinding(

                        scenario_id=
                        scenario_id,

                        scenario_title=
                        scenario_title,

                        severity=
                        "HIGH",

                        finding=
                        "No matched elements found",

                        recommendation=
                        "Review page mapping manually"
                    )
                )

            # -------------------------
            # RULE 2
            # Low Confidence
            # -------------------------

            if (
                confidence_score
                < 0.50
            ):

                findings.append(

                    SemanticValidationFinding(

                        scenario_id=
                        scenario_id,

                        scenario_title=
                        scenario_title,

                        severity=
                        "MEDIUM",

                        finding=
                        "Low confidence mapping",

                        recommendation=
                        "Improve semantic matching"
                    )
                )

            # -------------------------
            # RULE 3
            # High Confidence But Weak Coverage
            # -------------------------

            if (

                mapping_quality
                == "HIGH"

                and

                len(
                    matched_elements
                ) <= 1

            ):

                findings.append(

                    SemanticValidationFinding(

                        scenario_id=
                        scenario_id,

                        scenario_title=
                        scenario_title,

                        severity=
                        "MEDIUM",

                        finding=
                        "High confidence with weak element coverage",

                        recommendation=
                        "Verify mapping quality"
                    )
                )

        return findings

    @staticmethod
    def save_report(
        findings
    ):

        output_file = Path(
            "data/intermediate/semantic_validation_report.json"
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
                    finding.model_dump()

                    for finding
                    in findings
                ],

                file,

                indent=4
            )

        return str(
            output_file
        )