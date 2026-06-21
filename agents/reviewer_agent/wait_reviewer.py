from pathlib import Path
import re

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

        for java_file in tests_folder.glob(
            "*.java"
        ):

            with open(
                java_file,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            lines = content.splitlines()

            # -------------------------
            # CLICK VALIDATION
            # -------------------------

            for index, line in enumerate(lines):

                if ".click();" not in line:
                    continue

                click_line = line.strip()

                wait_found = False

                search_start = max(
                    0,
                    index - 3
                )

                for previous_index in range(
                    search_start,
                    index
                ):

                    previous_line = (
                        lines[
                            previous_index
                        ]
                    )

                    if (
                        "elementToBeClickable"
                        in previous_line
                    ):

                        wait_found = True
                        break

                if not wait_found:

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
                            f"Missing wait before click: {click_line}",

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

            for index, line in enumerate(lines):

                if ".sendKeys(" not in line:
                    continue

                input_line = (
                    line.strip()
                )

                wait_found = False

                search_start = max(
                    0,
                    index - 3
                )

                for previous_index in range(
                    search_start,
                    index
                ):

                    previous_line = (
                        lines[
                            previous_index
                        ]
                    )

                    if (
                        "visibilityOf"
                        in previous_line
                    ):

                        wait_found = True
                        break

                if not wait_found:

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
                            f"Missing visibility wait: {input_line}",

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