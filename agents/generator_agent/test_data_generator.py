class TestDataGenerator:

    @staticmethod
    def generate_value(
        element_name: str,
        input_type: str = None
    ):

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

        element_name = (
            element_name.lower()
        )

        if "phone" in element_name:
            return "9876543210"

        if "mobile" in element_name:
            return "9876543210"

        if "first" in element_name:
            return "John"

        if "last" in element_name:
            return "Doe"

        if "name" in element_name:
            return "John Doe"

        if "city" in element_name:
            return "Mumbai"

        if "address" in element_name:
            return "Test Address"

        if "pin" in element_name:
            return "411001"

        if "zipcode" in element_name:
            return "411001"

        if "postal" in element_name:
            return "411001"

        return "TEST_DATA"