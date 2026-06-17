from agents.requirement_agent.agent import (
    RequirementAgent
)


requirement_document = """
User can login using email and password.

Email must be valid.

Password minimum length is 8.

After successful login user lands
on dashboard.
"""


agent = RequirementAgent()

result = agent.analyze(
    requirement_document
)

print(result)