from agents.generator_agent.requirement_mapper import (
    RequirementMapper
)

mappings = (
    RequirementMapper.create_mappings()
)

for mapping in mappings:

    print(mapping)