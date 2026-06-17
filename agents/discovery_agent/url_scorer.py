class URLScorer:

    @staticmethod
    def score(url: str) -> int:

        url = url.lower()

        if "login" in url:
            return 100

        if "register" in url:
            return 90

        if "form" in url:
            return 80

        if "dashboard" in url:
            return 70

        if "help" in url or "docs" in url:
            return 60

        return 50