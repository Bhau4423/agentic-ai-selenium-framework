class ResponseRepair:

    @staticmethod
    def repair(
        data: dict
    ):

        # -------------------------
        # NORMALIZE REQUIREMENT IDS
        # -------------------------

        ResponseRepair._normalize_requirement_ids(
            data
        )

        # -------------------------
        # POSITIVE SCENARIOS
        # -------------------------

        ResponseRepair._repair_scenarios(
            data.get(
                "positive_scenarios",
                []
            ),
            "POSITIVE"
        )

        # -------------------------
        # NEGATIVE SCENARIOS
        # -------------------------

        ResponseRepair._repair_scenarios(
            data.get(
                "negative_scenarios",
                []
            ),
            "NEGATIVE"
        )

        # -------------------------
        # BOUNDARY SCENARIOS
        # -------------------------

        ResponseRepair._repair_scenarios(
            data.get(
                "boundary_scenarios",
                []
            ),
            "BOUNDARY"
        )

        return data

    @staticmethod
    def _normalize_requirement_ids(
        data: dict
    ):

        requirements = data.get(
            "requirements",
            []
        )

        id_mapping = {}

        # -------------------------
        # REQUIREMENTS
        # -------------------------

        for index, requirement in enumerate(
            requirements,
            start=1
        ):

            old_id = requirement.get(
                "id",
                ""
            )

            new_id = (
                f"FR-{index:03}"
            )

            id_mapping[
                old_id
            ] = new_id

            requirement[
                "id"
            ] = new_id

        # -------------------------
        # ACCEPTANCE CRITERIA
        # -------------------------

        ResponseRepair._update_requirement_references(
            data.get(
                "acceptance_criteria",
                []
            ),
            id_mapping
        )

        # -------------------------
        # POSITIVE SCENARIOS
        # -------------------------

        ResponseRepair._update_requirement_references(
            data.get(
                "positive_scenarios",
                []
            ),
            id_mapping
        )

        # -------------------------
        # NEGATIVE SCENARIOS
        # -------------------------

        ResponseRepair._update_requirement_references(
            data.get(
                "negative_scenarios",
                []
            ),
            id_mapping
        )

        # -------------------------
        # BOUNDARY SCENARIOS
        # -------------------------

        ResponseRepair._update_requirement_references(
            data.get(
                "boundary_scenarios",
                []
            ),
            id_mapping
        )

    @staticmethod
    def _update_requirement_references(
        items,
        id_mapping
    ):

        for item in items:

            requirement_id = item.get(
                "requirement_id",
                ""
            )

            if (
                requirement_id
                in id_mapping
            ):

                item[
                    "requirement_id"
                ] = id_mapping[
                    requirement_id
                ]

    @staticmethod
    def _repair_scenarios(
        scenarios,
        scenario_type
    ):

        for index, scenario in enumerate(
            scenarios,
            start=1
        ):

            if (
                "scenario_type"
                not in scenario
            ):

                scenario[
                    "scenario_type"
                ] = scenario_type

            if (
                "title"
                not in scenario
            ):

                scenario[
                    "title"
                ] = (
                    f"{scenario_type} "
                    f"Scenario "
                    f"{index}"
                )

            if (
                "steps"
                not in scenario
            ):

                scenario[
                    "steps"
                ] = []

            if (
                "expected_result"
                not in scenario
            ):

                scenario[
                    "expected_result"
                ] = (
                    "Expected result "
                    "not provided."
                )