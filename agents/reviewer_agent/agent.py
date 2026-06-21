from models.review_report_model import (
    ReviewReport
)

from agents.reviewer_agent.assertion_reviewer import (
    AssertionReviewer
)

from agents.reviewer_agent.coverage_reviewer import (
    CoverageReviewer
)

from agents.reviewer_agent.wait_reviewer import (
    WaitReviewer
)

from agents.reviewer_agent.locator_reviewer import (
    LocatorReviewer
)

from agents.reviewer_agent.missing_script_reviewer import (
    MissingScriptReviewer
)

from agents.reviewer_agent.edge_case_reviewer import (
    EdgeCaseReviewer
)

from agents.reviewer_agent.traceability_reviewer import (
    TraceabilityReviewer
)

from agents.reviewer_agent.hallucination_reviewer import (
    HallucinationReviewer
)

from agents.reviewer_agent.finding_deduplicator import (
    FindingDeduplicator
)

from agents.reviewer_agent.report_generator import (
    ReportGenerator
)


class ReviewerAgent:

    MAX_REVIEW_ITERATIONS = 5

    def review(
        self,
        iteration: int = 1
    ):

        print(
            "\n========== AGENT 4 STARTED =========="
        )

        print(
            f"\nReview Iteration: {iteration}"
        )

        if (
            iteration >
            self.MAX_REVIEW_ITERATIONS
        ):

            raise ValueError(
                "Maximum review iterations exceeded."
            )

        findings = []

        # --------------------------------
        # ASSERTION REVIEW
        # --------------------------------

        print(
            "\nRunning Assertion Review..."
        )

        assertion_findings = (
            AssertionReviewer.review()
        )

        findings.extend(
            assertion_findings
        )

        print(
            f"Assertion Findings: "
            f"{len(assertion_findings)}"
        )

        # --------------------------------
        # COVERAGE REVIEW
        # --------------------------------

        print(
            "\nRunning Coverage Review..."
        )

        coverage_findings = (
            CoverageReviewer.review()
        )

        findings.extend(
            coverage_findings
        )

        print(
            f"Coverage Findings: "
            f"{len(coverage_findings)}"
        )

        # --------------------------------
        # WAIT REVIEW
        # --------------------------------

        print(
            "\nRunning Wait Review..."
        )

        wait_findings = (
            WaitReviewer.review()
        )

        findings.extend(
            wait_findings
        )

        print(
            f"Wait Findings: "
            f"{len(wait_findings)}"
        )

        # --------------------------------
        # LOCATOR REVIEW
        # --------------------------------

        print(
            "\nRunning Locator Review..."
        )

        locator_findings = (
            LocatorReviewer.review()
        )

        findings.extend(
            locator_findings
        )

        print(
            f"Locator Findings: "
            f"{len(locator_findings)}"
        )

        # --------------------------------
        # MISSING SCRIPT REVIEW
        # --------------------------------

        print(
            "\nRunning Missing Script Review..."
        )

        script_findings = (
            MissingScriptReviewer.review()
        )

        findings.extend(
            script_findings
        )

        print(
            f"Missing Script Findings: "
            f"{len(script_findings)}"
        )

        # --------------------------------
        # EDGE CASE REVIEW
        # --------------------------------

        print(
            "\nRunning Edge Case Review..."
        )

        edge_findings = (
            EdgeCaseReviewer.review()
        )

        findings.extend(
            edge_findings
        )

        print(
            f"Edge Case Findings: "
            f"{len(edge_findings)}"
        )

        # --------------------------------
        # TRACEABILITY REVIEW
        # --------------------------------

        print(
            "\nRunning Traceability Review..."
        )

        traceability_findings = (
            TraceabilityReviewer.review()
        )

        findings.extend(
            traceability_findings
        )

        print(
            f"Traceability Findings: "
            f"{len(traceability_findings)}"
        )

        # --------------------------------
        # HALLUCINATION REVIEW
        # --------------------------------

        print(
            "\nRunning Hallucination Review..."
        )

        hallucination_findings = (
            HallucinationReviewer.review()
        )

        findings.extend(
            hallucination_findings
        )

        print(
            f"Hallucination Findings: "
            f"{len(hallucination_findings)}"
        )

        # --------------------------------
        # DEDUPLICATION
        # --------------------------------

        original_count = len(
            findings
        )

        findings = (
            FindingDeduplicator.deduplicate(
                findings
            )
        )

        removed_count = (
            original_count
            -
            len(findings)
        )

        if removed_count > 0:

            print(
                f"\nDuplicate Findings Removed: "
                f"{removed_count}"
            )

        # --------------------------------
        # STATUS
        # --------------------------------

        if len(findings) == 0:

            status = "APPROVED"

        else:

            status = "REVIEWED"

        # --------------------------------
        # REPORT
        # --------------------------------

        report = ReviewReport(

            iteration=iteration,

            status=status,

            total_findings=len(
                findings
            ),

            findings=findings
        )

        report_file = (
            ReportGenerator.save(
                report
            )
        )

        # --------------------------------
        # COUNTS
        # --------------------------------

        critical_count = len(
            [
                finding
                for finding in findings
                if finding.severity
                == "CRITICAL"
            ]
        )

        high_count = len(
            [
                finding
                for finding in findings
                if finding.severity
                == "HIGH"
            ]
        )

        medium_count = len(
            [
                finding
                for finding in findings
                if finding.severity
                == "MEDIUM"
            ]
        )

        low_count = len(
            [
                finding
                for finding in findings
                if finding.severity
                == "LOW"
            ]
        )

        print(
            f"\nReview Report: "
            f"{report_file}"
        )

        print(
            f"Total Findings: "
            f"{len(findings)}"
        )

        print(
            f"Critical Findings: "
            f"{critical_count}"
        )

        print(
            f"High Findings: "
            f"{high_count}"
        )

        print(
            f"Medium Findings: "
            f"{medium_count}"
        )

        print(
            f"Low Findings: "
            f"{low_count}"
        )

        print(
            f"Status: "
            f"{status}"
        )

        print(
            "\n========== AGENT 4 COMPLETED =========="
        )

        return {

            "iteration":
                iteration,

            "status":
                status,

            "total_findings":
                len(findings),

            "findings":
                findings,

            "critical":
                critical_count,

            "high":
                high_count,

            "medium":
                medium_count,

            "low":
                low_count,

            "report":
                report_file
        }