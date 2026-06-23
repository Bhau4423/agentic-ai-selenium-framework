class SemanticDictionary:

    SYNONYMS = {

        "login": [
            "signin",
            "authenticate",
            "username",
            "password",
            "credential"
        ],

        "upload": [
            "file",
            "browse",
            "attachment",
            "document"
        ],

        "alert": [
            "popup",
            "dialog",
            "message"
        ],

        "checkbox": [
            "check",
            "tick",
            "selection"
        ],

        "dropdown": [
            "select",
            "option",
            "choice"
        ],

        "slider": [
            "range",
            "drag",
            "move"
        ],

        "button": [
            "submit",
            "save",
            "continue",
            "next"
        ],

        "table": [
            "grid",
            "row",
            "column"
        ],

        "notification": [
            "message",
            "toast",
            "alert"
        ],

        "footer": [
            "bottom",
            "copyright"
        ]
    }

    @staticmethod
    def expand_keywords(
        keywords: set
    ):

        expanded = set(
            keywords
        )

        for keyword in keywords:

            keyword = keyword.lower()

            if (
                keyword
                in
                SemanticDictionary.SYNONYMS
            ):

                expanded.update(
                    SemanticDictionary.SYNONYMS[
                        keyword
                    ]
                )

        return expanded