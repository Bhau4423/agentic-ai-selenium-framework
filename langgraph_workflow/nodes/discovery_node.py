import json

from agents.discovery_agent.agent import (
    DiscoveryAgent
)


def discovery_node(
    state
):

    print(
        "\n[LangGraph] Discovery Node"
    )

    with open(
        "data/intermediate/requirement_analysis.json",
        "r",
        encoding="utf-8"
    ) as file:

        requirement_data = (
            json.load(file)
        )

    base_url = (
        requirement_data.get(
            "base_url"
        )
    )

    application_urls = (
        requirement_data.get(
            "application_urls",
            []
        )
    )

    if not base_url:

        raise ValueError(
            "Base URL not found in SRS"
        )

    urls_to_discover = []

    for item in application_urls:

        path = item.get(
            "url",
            ""
        )

        if not path:
            continue

        full_url = (
            base_url.rstrip("/")
            + "/"
            + path.lstrip("/")
        )

        urls_to_discover.append(
            full_url
        )

    print(
        f"URLs To Discover: "
        f"{len(urls_to_discover)}"
    )

    agent = (
        DiscoveryAgent()
    )

    result = (
        agent.discover(
            urls_to_discover
        )
    )

    state[
        "discovery_result"
    ] = result

    return state