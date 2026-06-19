from agents.reviewer_agent.patch_strategy_factory import (
    PatchStrategyFactory
)

strategy = (
    PatchStrategyFactory.get_strategy(
        "ASSERTION"
    )
)

print(strategy)