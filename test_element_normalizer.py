from agents.reviewer_agent.element_name_normalizer import (
    ElementNameNormalizer
)

values = [

    "wpforms[fields][0][first]",

    "wpforms_fields__0__first_",

    "g-recaptcha-hidden",

    "g_recaptcha_hidden"
]

for value in values:

    print(
        value,
        "->",
        ElementNameNormalizer.normalize(
            value
        )
    )