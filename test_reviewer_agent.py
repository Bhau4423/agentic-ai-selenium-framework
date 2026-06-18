from agents.reviewer_agent.agent import (
    ReviewerAgent
)

agent = ReviewerAgent()

result = (
    agent.review()
)

print(
    "\nRESULT:"
)

print(result)