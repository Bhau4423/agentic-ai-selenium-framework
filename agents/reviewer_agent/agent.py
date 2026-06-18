from models.review_report_model import (
    ReviewReport
)

from agents.reviewer_agent.assertion_reviewer import (
    AssertionReviewer
)

from agents.reviewer_agent.coverage_reviewer import (
    CoverageReviewer
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

        # -------------------------
        # ASSERTION REVIEW
        # -------------------------

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

        # -------------------------
        # COVERAGE REVIEW
        # -------------------------

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

        # -------------------------
        # STATUS CALCULATION
        # -------------------------

        if len(findings) == 0:

            status = "APPROVED"

        else:

            status = "REVIEWED"

        # -------------------------
        # REVIEW REPORT
        # -------------------------

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

        # -------------------------
        # SUMMARY COUNTS
        # -------------------------

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