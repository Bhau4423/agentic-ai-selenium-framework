class ResponseRepair:

    @staticmethod
    def repair(
        data: dict
    ):

        ResponseRepair._repair_scenarios(
            data.get(
                "positive_scenarios",
                []
            ),
            "POSITIVE"
        )

        ResponseRepair._repair_scenarios(
            data.get(
                "negative_scenarios",
                []
            ),
            "NEGATIVE"
        )

        ResponseRepair._repair_scenarios(
            data.get(
                "boundary_scenarios",
                []
            ),
            "BOUNDARY"
        )

        return data

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
                    "Expected result not provided."
                )