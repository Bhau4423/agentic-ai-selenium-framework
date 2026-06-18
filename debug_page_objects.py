from agents.generator_agent.requirement_mapper import (
    RequirementMapper
)

from agents.generator_agent.page_mapper import (
    PageMapper
)

requirement_mappings = (
    RequirementMapper.create_mappings()
)

page_objects = (
    PageMapper.build_page_objects(
        requirement_mappings
    )
)

for page in page_objects:

    print("\n===================")

    print(page)

    print("===================\n")