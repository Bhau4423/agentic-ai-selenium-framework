from agents.reviewer_agent.missing_script_patch_strategy import (
    MissingScriptPatchStrategy
)


class EdgeCasePatchStrategy:

    @staticmethod
    def generate(
        scenario_id: str
    ):

        return (
            MissingScriptPatchStrategy.generate(
                scenario_id
            )
        )