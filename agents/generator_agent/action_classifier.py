class ActionClassifier:

    @staticmethod
    def classify(
        element: dict
    ):

        element_type = str(
            element.get(
                "element_type"
            ) or ""
        ).lower()

        input_type = str(
            element.get(
                "input_type"
            ) or ""
        ).lower()

        element_name = str(
            element.get(
                "element_name"
            ) or ""
        ).lower()

        label = str(
            element.get(
                "label"
            ) or ""
        ).lower()

        visible_text = str(
            element.get(
                "visible_text"
            ) or ""
        ).lower()

        aria_label = str(
            element.get(
                "aria_label"
            ) or ""
        ).lower()

        placeholder = str(
            element.get(
                "placeholder"
            ) or ""
        ).lower()

        combined_text = (
            f"{element_name} "
            f"{label} "
            f"{visible_text} "
            f"{aria_label} "
            f"{placeholder}"
        ).lower()

        # -------------------------
        # FILE UPLOAD
        # -------------------------

        if input_type == "file":

            return "FILE_UPLOAD"

        if "upload" in combined_text:

            return "FILE_UPLOAD"

        # -------------------------
        # FILE DOWNLOAD
        # -------------------------

        if "download" in combined_text:

            return "FILE_DOWNLOAD"

        # -------------------------
        # CHECKBOX
        # -------------------------

        if (
            element_type == "checkbox"
            or
            input_type == "checkbox"
        ):

            return "CHECKBOX"

        # -------------------------
        # RADIO BUTTON
        # -------------------------

        if (
            element_type == "radio"
            or
            input_type == "radio"
        ):

            return "RADIO"

        # -------------------------
        # DROPDOWN
        # -------------------------

        if (
            element_type == "dropdown"
            or
            element_type == "select"
        ):

            return "SELECT"

        # -------------------------
        # TABLE
        # -------------------------

        if element_type == "table":

            return "TABLE_VALIDATE"

        # -------------------------
        # ALERT
        # -------------------------

        if (
            "alert" in combined_text
            or
            "javascript alert" in combined_text
        ):

            return "ALERT_ACCEPT"

        # -------------------------
        # MODAL
        # -------------------------

        if (
            "modal" in combined_text
            or
            "popup" in combined_text
            or
            "dialog" in combined_text
        ):

            return "MODAL_CLOSE"

        # -------------------------
        # WINDOW
        # -------------------------

        if (
            "window" in combined_text
            or
            "tab" in combined_text
        ):

            return "WINDOW_SWITCH"

        # -------------------------
        # FRAME
        # -------------------------

        if (
            "frame" in combined_text
            or
            "iframe" in combined_text
        ):

            return "FRAME_SWITCH"

        # -------------------------
        # LOGIN FIELDS
        # -------------------------

        if (
            "username" in combined_text
            or
            "email" in combined_text
            or
            "password" in combined_text
        ):

            return "SEND_KEYS"

        # -------------------------
        # TEXT INPUTS
        # -------------------------

        if (
            element_type == "textbox"
            or
            element_type == "input"
            or
            element_type == "textarea"
        ):

            return "SEND_KEYS"

        # -------------------------
        # BUTTONS
        # -------------------------

        if element_type == "button":

            return "CLICK"

        # -------------------------
        # LINKS
        # -------------------------

        if element_type == "link":

            return "CLICK"

        # -------------------------
        # DEFAULT
        # -------------------------

        return "CLICK"