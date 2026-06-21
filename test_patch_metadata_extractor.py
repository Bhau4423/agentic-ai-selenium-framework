from agents.reviewer_agent.patch_metadata_extractor import (
    PatchMetadataExtractor
)

print(

    PatchMetadataExtractor
    .extract_missing_wait_target(

        "Missing wait before click: page.get_Submit().click();"
    )
)

print(

    PatchMetadataExtractor
    .extract_hallucinated_method(

        "Getter not found in generated page objects: get_error_message()"
    )
)

print(

    PatchMetadataExtractor
    .extract_locator(

        "Locator not found in inventory: wpforms_fields__0__first_"
    )
)