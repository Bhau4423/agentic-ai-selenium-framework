from models.review_finding_model import (
    ReviewFinding
)

from models.requirement_analysis_result import (
    RequirementAnalysisResult
)


class CoverageValidator:

    @staticmethod
    def validate(
        result: RequirementAnalysisResult
    ):

        findings = []

        requirement_ids = {

            requirement.id

            for requirement

            in result.requirements
        }

        # -----------------------------
        # ACCEPTANCE CRITERIA COVERAGE
        # -----------------------------

        ac_requirement_ids = {

            ac.requirement_id

            for ac

            in result.acceptance_criteria
        }

        for requirement_id in requirement_ids:

            if requirement_id not in ac_requirement_ids:

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"COV-AC-{requirement_id}",

                        severity=
                        "HIGH",

                        category=
                        "COVERAGE",

                        file_name=
                        "requirement_analysis.json",

                        description=
                        f"Requirement {requirement_id} "
                        f"has no Acceptance Criteria.",

                        recommendation=
                        "Generate at least one "
                        "Acceptance Criteria.",

                        requirement_id=
                        requirement_id,

                        auto_fixable=
                        True
                    )
                )

        # -----------------------------
        # POSITIVE SCENARIO COVERAGE
        # -----------------------------

        positive_requirement_ids = {

            scenario.requirement_id

            for scenario

            in result.positive_scenarios
        }

        for requirement_id in requirement_ids:

            if (

                requirement_id

                not in

                positive_requirement_ids

            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"COV-POS-{requirement_id}",

                        severity=
                        "HIGH",

                        category=
                        "COVERAGE",

                        file_name=
                        "requirement_analysis.json",

                        description=
                        f"Requirement {requirement_id} "
                        f"has no Positive Scenario.",

                        recommendation=
                        "Generate positive coverage.",

                        requirement_id=
                        requirement_id,

                        auto_fixable=
                        True
                    )
                )

        # -----------------------------
        # NEGATIVE SCENARIO COVERAGE
        # -----------------------------

        negative_requirement_ids = {

            scenario.requirement_id

            for scenario

            in result.negative_scenarios
        }

        for requirement_id in requirement_ids:

            if (

                requirement_id

                not in

                negative_requirement_ids

            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"COV-NEG-{requirement_id}",

                        severity=
                        "MEDIUM",

                        category=
                        "COVERAGE",

                        file_name=
                        "requirement_analysis.json",

                        description=
                        f"Requirement {requirement_id} "
                        f"has no Negative Scenario.",

                        recommendation=
                        "Generate negative coverage.",

                        requirement_id=
                        requirement_id,

                        auto_fixable=
                        True
                    )
                )

        # -----------------------------
        # ORPHAN ACCEPTANCE CRITERIA
        # -----------------------------

        for ac in result.acceptance_criteria:

            if (

                ac.requirement_id

                not in

                requirement_ids

            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"ORPHAN-AC-{ac.id}",

                        severity=
                        "HIGH",

                        category=
                        "TRACEABILITY",

                        file_name=
                        "requirement_analysis.json",

                        description=
                        f"Acceptance Criteria "
                        f"{ac.id} references "
                        f"missing requirement.",

                        recommendation=
                        "Fix requirement mapping.",

                        requirement_id=
                        ac.requirement_id,

                        auto_fixable=
                        True
                    )
                )

        # -----------------------------
        # ORPHAN SCENARIOS
        # -----------------------------

        all_scenarios = (

            result.positive_scenarios

            +

            result.negative_scenarios

            +

            result.boundary_scenarios
        )

        for scenario in all_scenarios:

            if (

                scenario.requirement_id

                not in

                requirement_ids

            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"ORPHAN-SC-{scenario.id}",

                        severity=
                        "HIGH",

                        category=
                        "TRACEABILITY",

                        file_name=
                        "requirement_analysis.json",

                        description=
                        f"Scenario "
                        f"{scenario.id} "
                        f"references "
                        f"missing requirement.",

                        recommendation=
                        "Fix requirement mapping.",

                        requirement_id=
                        scenario.requirement_id,

                        auto_fixable=
                        True
                    )
                )

        return findings