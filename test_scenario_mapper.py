from agents.generator_agent.scenario_mapper import (
    ScenarioMapper
)


print(
    "\n========== AGENT 3.1 STARTED =========="
)

mappings = (
    ScenarioMapper.map_scenarios()
)

ScenarioMapper.save_mappings(
    mappings
)

print(
    f"\nScenario Mappings: "
    f"{len(mappings)}"
)

for mapping in mappings[:10]:

    print(
        f"\n{mapping.scenario_id}"
    )

    print(
        f"Scenario : "
        f"{mapping.scenario_title}"
    )

    print(
        f"Page     : "
        f"{mapping.page_name}"
    )

    print(
        f"Confidence : "
        f"{mapping.confidence_score}"
    )

    print(
        f"Quality    : "
        f"{mapping.mapping_quality}"
    )

    print(
        f"Elements : "
        f"{len(mapping.matched_elements)}"
    )

print(
    "\n========== AGENT 3.1 COMPLETED =========="
)