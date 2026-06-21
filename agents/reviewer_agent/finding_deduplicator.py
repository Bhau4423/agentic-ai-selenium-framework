from models.review_finding_model import (
    ReviewFinding
)


class FindingDeduplicator:

    @staticmethod
    def deduplicate(
        findings: list[ReviewFinding]
    ):

        unique_findings = []

        processed_keys = set()

        for finding in findings:

            scenario_id = (
                finding.scenario_id
                or ""
            )

            file_name = (
                finding.file_name
                or ""
            )

            key = (
                scenario_id,
                file_name
            )

            if key in processed_keys:

                continue

            processed_keys.add(
                key
            )

            unique_findings.append(
                finding
            )

        return unique_findings