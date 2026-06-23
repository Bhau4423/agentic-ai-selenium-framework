from pathlib import Path

from agents.requirement_agent.agent import (
    RequirementAgent
)

file_path = Path(
    "input/srs_document.txt"
)

with open(
    file_path,
    "r",
    encoding="utf-8"
) as file:

    requirement_document = file.read()

agent = RequirementAgent()

result = agent.analyze(
    requirement_document
)

print(
    "\n========== FINAL RESULT =========="
)

print(
    f"Requirements: {len(result.requirements)}"
)

print(
    f"Acceptance Criteria: {len(result.acceptance_criteria)}"
)

print(
    f"Positive Scenarios: {len(result.positive_scenarios)}"
)

print(
    f"Negative Scenarios: {len(result.negative_scenarios)}"
)

print(
    f"Boundary Scenarios: {len(result.boundary_scenarios)}"
)