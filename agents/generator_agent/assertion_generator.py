class AssertionGenerator:

    @staticmethod
    def generate(
        scenario_title: str,
        scenario_type: str
    ):

        title = (
            scenario_title.lower()
        )

        scenario_type = (
            scenario_type.upper()
        )

        # -------------------------
        # POSITIVE SCENARIOS
        # -------------------------

        if scenario_type == "POSITIVE":

            if (
                "login" in title
                or
                "authentication" in title
            ):

                return (
                    'Assert.assertTrue('
                    'driver.getCurrentUrl()'
                    '.contains("dashboard"));'
                )

            if (
                "search" in title
            ):

                return (
                    'Assert.assertTrue('
                    '!driver.getTitle().isEmpty());'
                )

            if (
                "contact" in title
            ):

                return (
                    'Assert.assertTrue('
                    '!driver.getPageSource()'
                    '.isEmpty());'
                )

        # -------------------------
        # NEGATIVE SCENARIOS
        # -------------------------

        if scenario_type == "NEGATIVE":

            return (
                'Assert.assertFalse('
                'driver.getCurrentUrl()'
                '.contains("dashboard"));'
            )

        # -------------------------
        # BOUNDARY SCENARIOS
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