from agents.generator_agent.traceability_generator import (
    TraceabilityGenerator
)

print(
    "\n========== AGENT 3.2 STARTED =========="
)

output_file = (
    TraceabilityGenerator.save()
)

print(
    f"\nOutput File:"
)

print(
    output_file
)

print(
    "\n========== AGENT 3.2 COMPLETED =========="
)