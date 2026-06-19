from agents.reviewer_agent.context_builder import (
    ContextBuilder
)

contexts = (
    ContextBuilder.build_contexts()
)

for context in contexts:

    print(context)