class TestDataGenerator:

    @staticmethod
    def generate_value(
        element_name: str,
        input_type: str = None,
        label: str = None,
        placeholder: str = None
    ):

        search_text = " ".join(
            [
                str(element_name or ""),
                str(label or ""),
                str(placeholder or "")
            ]
        ).lower()

        if input_type:

            input_type = (
                input_type.lower()
            )

            if input_type == "email":
                return "test@test.com"

            if input_type == "password":
                return "Password123"

            if input_type == "number":
                return "12345"

            if input_type == "tel":
                return "9876543210"

            if input_type == "date":
                return "2025-01-01"

            if input_type == "url":
                return "https://example.com"

        if "email" in search_text:
            return "test@test.com"

        if "password" in search_text:
            return "Password123"

        if "phone" in search_text:
            return "9876543210"

        if "mobile" in search_text:
            return "9876543210"

        if "first" in search_text:
            return "John"

        if "last" in search_text:
            return "Doe"

        if "full name" in search_text:
            return "John Doe"

        if "name" in search_text:
            return "John Doe"

        if "city" in search_text:
            return "Mumbai"

        if "country" in search_text:
            return "India"

        if "address" in search_text:
            return "Test Address"

        if "pin" in search_text:
            return "411001"

        if "zipcode" in search_text:
            return "411001"

        if "postal" in search_text:
            return "411001"

        if "policy" in search_text:
            return "POL123456"

        if "customer" in search_text:
            return "CUS123456"

        if "employee" in search_text:
            return "EMP123456"

        return "TEST_DATA"