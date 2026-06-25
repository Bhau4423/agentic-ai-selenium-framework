from agents.reviewer_agent.assertion_patch_strategy import (
    AssertionPatchStrategy
)

from agents.reviewer_agent.hallucination_patch_strategy import (
    HallucinationPatchStrategy
)


class PatchStrategyFactory:

    @staticmethod
    def get_strategy(
        category: str
    ):

        category = category.upper()

        if category == "ASSERTION":

            return AssertionPatchStrategy
        
        elif category == "HALLUCINATED_METHOD":

            return HallucinationPatchStrategy

        return None