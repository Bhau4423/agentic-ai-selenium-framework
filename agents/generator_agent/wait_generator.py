class WaitGenerator:

    @staticmethod
    def get_safe_element_name(
        element_name: str
    ):

        return (
            element_name
            .replace(" ", "_")
            .replace("-", "_")
            .replace("[", "_")
            .replace("]", "_")
        )

    @staticmethod
    def generate(
        action_type: str,
        element_name: str
    ):

        element_name = (
            WaitGenerator.get_safe_element_name(
                element_name
            )
        )

        action_type = (
            action_type.upper()
        )

        if action_type == "CLICK":

            return (
                f"wait.until("
                f"ExpectedConditions."
                f"elementToBeClickable("
                f"page.get_{element_name}()"
                f"));"
            )

        return (
            f"wait.until("
            f"ExpectedConditions."
            f"visibilityOf("
            f"page.get_{element_name}()"
            f"));"
        )