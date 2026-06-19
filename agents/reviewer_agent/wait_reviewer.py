from pathlib import Path

from models.review_finding_model import (
    ReviewFinding
)


class WaitReviewer:

    @staticmethod
    def review():

        findings = []

        tests_folder = Path(
            "generated_framework/tests"
        )

        if not tests_folder.exists():

            return findings

        finding_counter = 1

        java_files = (
            tests_folder.glob(
                "*.java"
            )
        )

        for java_file in java_files:

            with open(
                java_file,
                "r",
                encoding="utf-8"
            ) as file:

                content = (
                    file.read()
                )

            click_count = (
                content.count(
                    ".click();"
                )
            )

            wait_click_count = (
                content.count(
                    "elementToBeClickable"
                )
            )

            send_keys_count = (
                content.count(
                    ".sendKeys("
                )
            )

            wait_visibility_count = (
                content.count(
                    "visibilityOf"
                )
            )

            # -------------------------
            # CLICK VALIDATION
            # -------------------------

            if (
                click_count >
                wait_click_count
            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"WAIT-{finding_counter:03}",

                        severity=
                        "MEDIUM",

                        category=
                        "WAIT",

                        file_name=
                        java_file.name,

                        description=
                        "Click action found without explicit wait.",

                        recommendation=
                        "Add elementToBeClickable wait.",

                        impacted_component=
                        "Test Script",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

            # -------------------------
            # SEND_KEYS VALIDATION
            # -------------------------

            if (
                send_keys_count >
                wait_visibility_count
            ):

                findings.append(

                    ReviewFinding(

                        finding_id=
                        f"WAIT-{finding_counter:03}",

                        severity=
                        "MEDIUM",

                        category=
                        "WAIT",

                        file_name=
                        java_file.name,

                        description=
                        "Input action found without visibility wait.",

                        recommendation=
                        "Add visibilityOf wait.",

                        impacted_component=
                        "Test Script",

                        auto_fixable=
                        True
                    )
                )

                finding_counter += 1

        return findings