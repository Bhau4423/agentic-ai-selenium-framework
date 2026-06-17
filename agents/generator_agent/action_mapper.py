class ActionMapper:

    @staticmethod
    def detect_action(
        step: str
    ):

        step = step.lower()

        if (
            "enter" in step
            or "type" in step
            or "input" in step
        ):

            return "SEND_KEYS"

        if (
            "click" in step
            or "press" in step
            or "submit" in step
        ):

            return "CLICK"

        if (
            "select" in step
            or "choose" in step
        ):

            return "SELECT"

        if (
            "verify" in step
            or "validate" in step
            or "check" in step
        ):

            return "ASSERT"

        if (
            "navigate" in step
            or "open" in step
            or "launch" in step
        ):

            return "NAVIGATE"

        return "UNKNOWN"

    @staticmethod
    def map_steps(
        scenario
    ):

        results = []

        steps = scenario.get(
            "steps",
            []
        )

        for step in steps:

            results.append(
                {
                    "step": step,
                    "action": (
                        ActionMapper.detect_action(
                            step
                        )
                    )
                }
            )

        return results