import json

from agents.generator_agent.semantic_element_mapper import (
    SemanticElementMapper
)

with open(
    "data/intermediate/requirement_analysis.json",
    "r",
    encoding="utf-8"
) as file:

    requirement_data = json.load(file)

with open(
    "output/page_inventory.json",
    "r",
    encoding="utf-8"
) as file:

    inventory_data = json.load(file)

scenario = (
    requirement_data["positive_scenarios"][0]
)

page = (
    inventory_data["pages"][0]
)

mapper = SemanticElementMapper()

result = mapper.map_scenario(
    scenario,
    page
)

print(result)