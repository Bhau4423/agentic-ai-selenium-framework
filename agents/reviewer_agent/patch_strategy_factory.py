from agents.reviewer_agent.assertion_patch_strategy import (
    AssertionPatchStrategy
)


class PatchStrategyFactory:

    @staticmethod
    def get_strategy(
        category: str
    ):

        category = category.upper()

        if category == "ASSERTION":

            return AssertionPatchStrategy

        return None