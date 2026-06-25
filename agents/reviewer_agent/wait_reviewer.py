from pathlib import Path
import re

from models.review_finding_model import (
    ReviewFinding
)

from agents.reviewer_agent.review_file_provider import (
    ReviewFileProvider
)


class WaitReviewer:

    @staticmethod
    def review():

        findings = []

        reported_interactions = set()

        java_files = (
            ReviewFileProvider
            .get_generated_test_files()
        )

        if not java_files:

            return findings

        finding_counter = 1

        interaction_keywords = [

            ".click(",
            ".sendKeys(",
            ".clear(",
            ".submit(",
            ".selectByVisibleText(",
            ".selectByValue(",
            ".selectByIndex("
        ]

        wait_keywords = [

            "elementToBeClickable",
            "visibilityOf",
            "presenceOfElementLocated",
            "visibilityOfElementLocated"
        ]

        for java_file in java_files:

            with open(
                java_file,
                "r",
                encoding="utf-8"
            ) as file:

                lines = file.readlines()

        # ---------------------------------
        # REMOVE COMMENTS
        # ---------------------------------

            cleaned_lines = []

            inside_block_comment = False

            for line in lines:

                stripped = line.strip()

                if stripped.startswith("/*"):

                    inside_block_comment = True
                    continue

                if inside_block_comment:

                    if "*/" in stripped:

                        inside_block_comment = False

                        continue

                if stripped.startswith("//"):

                    continue

                cleaned_lines.append(line)

        # ---------------------------------
        # CHECK INTERACTIONS
        # ---------------------------------

            for index, line in enumerate(
                cleaned_lines
            ):

                stripped_line = (
                    line.strip()
                )

                interaction_found = False

                for keyword in interaction_keywords:

                    if keyword in stripped_line:

                        interaction_found = True
                        break

                if not interaction_found:

                    continue

                wait_found = False

                search_start = max(
                   0,
                   index - 10
                )

                for previous_index in range(
                    search_start,
                    index
                ):

                    previous_line = (
                        cleaned_lines[
                            previous_index
                        ]
                    )

                    for wait_keyword in wait_keywords:

                        if (
                            wait_keyword
                            in previous_line
                        ):

                            wait_found = True
                            break

                    if wait_found:

                        break

                if not wait_found:

                    interaction_key = (
                        java_file.name,
                        stripped_line
                    )

                    if interaction_key in reported_interactions:

                        continue

                    reported_interactions.add(
                        interaction_key
                    )

                    findings.append(

                        ReviewFinding(

                            finding_id=
                            f"WAIT-{finding_counter:03}",

                            severity=
                            "HIGH",

                            category=
                            "WAIT",

                            file_name=
                            java_file.name,

                            description=
                            (
                                "Missing wait before interaction: "
                                f"{stripped_line}"
                            ),

                            recommendation=
                            (
                                "Add appropriate explicit wait before interacting with the element."
                            ),

                            impacted_component=
                            "Generated Test",

                            auto_fixable=
                            True
                        )
                    )

                    finding_counter += 1

        # ---------------------------------
        # STANDALONE WAIT CHECK
        # ---------------------------------

            contains_wait = False

            contains_page_element = False

            for line in cleaned_lines:

                if "wait.until(" in line:

                    contains_wait = True

                if "page.get_" in line:

                    contains_page_element = True

            if (

                contains_page_element
                and
                not contains_wait

            ):

                has_interaction = False

                for line in cleaned_lines:

                    for keyword in interaction_keywords:

                        if keyword in line:

                            has_interaction = True
                            break

                    if has_interaction:

                        break

                if not has_interaction:

                    findings.append(

                        ReviewFinding(

                            finding_id=
                            f"WAIT-{finding_counter:03}",

                            severity=
                            "HIGH",

                            category=
                            "WAIT",

                            file_name=
                            java_file.name,

                            description=
                            (
                                "No explicit wait found in generated test."
                            ),

                            recommendation=
                            (
                                "Insert explicit wait before interacting with page elements."
                            ),

                            impacted_component=
                            "Generated Test",

                            auto_fixable=
                            True
                        )
                    )

                    finding_counter += 1

        return findings