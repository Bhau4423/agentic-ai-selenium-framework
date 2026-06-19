from agents.reviewer_agent.assertion_reviewer import (
    AssertionReviewer
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


class RevalidationEngine:

    @staticmethod
    def validate():

        findings = []

        findings.extend(
            AssertionReviewer.review()
        )

        findings.extend(
            WaitReviewer.review()
        )

        findings.extend(
            LocatorReviewer.review()
        )

        findings.extend(
            MissingScriptReviewer.review()
        )

        findings.extend(
            EdgeCaseReviewer.review()
        )

        findings.extend(
            TraceabilityReviewer.review()
        )

        findings.extend(
            HallucinationReviewer.review()
        )

        return findings