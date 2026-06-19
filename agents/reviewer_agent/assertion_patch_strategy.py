from models.scenario_context_model import (
    ScenarioContext
)


class AssertionPatchStrategy:

    @staticmethod
    def generate_assertion(
        context: ScenarioContext
    ):

        expected_result = (
            context.expected_result.lower()
        )

        scenario_type = (
            context.scenario_type.upper()
        )

        # -------------------------
        # POSITIVE SUCCESS
        # -------------------------

        if (
            "dashboard"
            in expected_result
        ):

            return (
                'Assert.assertTrue('
                'driver.getCurrentUrl()'
                '.contains("dashboard"));'
            )

        # -------------------------
        # NEGATIVE VALIDATION
        # -------------------------

        if scenario_type == "NEGATIVE":

            return (
                'Assert.assertFalse('
                'driver.getCurrentUrl()'
                '.contains("dashboard"));'
            )

        # -------------------------
        # BOUNDARY SUCCESS
        # -------------------------

        if scenario_type == "BOUNDARY":

            return (
                'Assert.assertTrue('
                'driver.getCurrentUrl()'
                '.contains("dashboard"));'
            )

        # -------------------------
        # FALLBACK
        # -------------------------

        return (
            'Assert.assertTrue('
            'driver.getCurrentUrl()'
            '.length() > 0);'
        )