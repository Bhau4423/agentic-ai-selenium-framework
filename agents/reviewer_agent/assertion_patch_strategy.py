from multiprocessing import context

from models.scenario_context_model import (
    ScenarioContext
)


class AssertionPatchStrategy:

    @staticmethod
    def generate_assertion(
        context: ScenarioContext
    ):

        scenario_type = (
            context.scenario_type.upper()
        )

        expected_result = (
            context.expected_result.lower()
        )

    # ---------------------------------
    # NEGATIVE SCENARIO
    # ---------------------------------

        if scenario_type == "NEGATIVE":

            return (
                'Assert.assertFalse('
                'driver.getCurrentUrl().isEmpty());'
            )

    # ---------------------------------
    # URL VALIDATION
    # ---------------------------------

        if (
            "url" in expected_result
            or
            "page" in expected_result
            or
            "navigate" in expected_result
        ):

            return (
                'Assert.assertTrue('
                'driver.getCurrentUrl().length() > 0);'
            )

    # ---------------------------------
    # TEXT VALIDATION
    # ---------------------------------

        if (
            "message" in expected_result
            or
            "display" in expected_result
            or
            "visible" in expected_result
        ):

            return (
                'Assert.assertTrue('
                'driver.getPageSource().length() > 0);'
            )

    # ---------------------------------
    # DEFAULT ASSERTION
    # ---------------------------------

        return (
            'Assert.assertTrue('
            '!driver.getCurrentUrl().isEmpty());'
        )