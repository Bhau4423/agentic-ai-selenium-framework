from models.requirement_analysis_result import (
    RequirementAnalysisResult
)

from agents.requirement_agent.coverage_validator import (
    CoverageValidator
)


class RequirementValidator:

    @staticmethod
    def validate(
        result: RequirementAnalysisResult
    ):

        errors = []

        # -------------------------
        # BASIC VALIDATION
        # -------------------------

        if not result.requirements:

            errors.append(
                "No requirements generated"
            )

        if not result.acceptance_criteria:

            errors.append(
                "No acceptance criteria generated"
            )

        if not result.positive_scenarios:

            errors.append(
                "No positive scenarios generated"
            )

        if not result.negative_scenarios:

            errors.append(
                "No negative scenarios generated"
            )

        # Boundary scenarios are optional
        # for some requirements

        # -------------------------
        # COVERAGE VALIDATION
        # -------------------------

        coverage_findings = (
            CoverageValidator.validate(
                result
            )
        )

        if coverage_findings:

            print(
                "\nCoverage Findings:"
            )

            print(
                f"{len(coverage_findings)} findings detected"
            )

            high_count = len(

                [
                    finding

                    for finding

                    in coverage_findings

                    if finding.severity
                    == "HIGH"
                ]
            )

            medium_count = len(

                [
                    finding

                    for finding

                    in coverage_findings

                    if finding.severity
                    == "MEDIUM"
                ]
            )

            print(
                f"HIGH   : {high_count}"
            )

            print(
                f"MEDIUM : {medium_count}"
            )

        return errors