class AssertionGenerator:

    @staticmethod
    def generate(
        scenario_title: str,
        scenario_type: str
    ):

        title = (
            scenario_title.lower()
        )

        if (
            "login" in title
            or "authentication" in title
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

        return (
            "Assert.assertTrue(true);"
        )