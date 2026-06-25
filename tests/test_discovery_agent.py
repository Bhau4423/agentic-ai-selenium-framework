from agents.discovery_agent.agent import (
    DiscoveryAgent
)

from pathlib import Path
import json


def load_urls():

    requirement_file = Path(
        "data/intermediate/requirement_analysis.json"
    )

    if not requirement_file.exists():

        raise FileNotFoundError(
            "requirement_analysis.json not found"
        )

    with open(
        requirement_file,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    base_url = data.get(
        "base_url"
    )

    application_urls = data.get(
        "application_urls",
        []
    )

    urls = []

    for app_url in application_urls:

        path = app_url.get(
            "url"
        )

        if not path:

            continue

        if path.startswith(
            "http"
        ):

            urls.append(
                path
            )

        elif base_url:

            urls.append(
                f"{base_url}{path}"
            )

    return urls


if __name__ == "__main__":

    print(
        "\n========== AGENT 2 STARTED =========="
    )

    urls = load_urls()

    print(
        f"\nURLs Found: {len(urls)}"
    )

    for url in urls:

        print(url)

    agent = DiscoveryAgent()

    result = agent.discover(
        urls=urls,
        verbose=True
    )

    print(
        "\n========== AGENT 2 COMPLETED =========="
    )

    print(
        f"Pages     : {result['pages']}"
    )

    print(
        f"Elements  : {result['elements']}"
    )

    print(
        f"Forms     : {result['forms']}"
    )

    print(
        f"Links     : {result['links']}"
    )

    print(
        f"Tables    : {result['tables']}"
    )

    print(
        f"\nInventory : "
        f"{result['inventory_file']}"
    )