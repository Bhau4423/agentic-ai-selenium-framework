from pathlib import Path

import fitz
from docx import Document


class DocumentLoader:

    SUPPORTED_EXTENSIONS = [

        ".pdf",

        ".txt",

        ".docx"
    ]

    INPUT_FOLDER = Path(
        "input"
    )

    @staticmethod
    def load() -> str:

        if not DocumentLoader.INPUT_FOLDER.exists():

            raise FileNotFoundError(
                "Input folder not found."
            )

        supported_files = []

        for file in DocumentLoader.INPUT_FOLDER.iterdir():

            if (

                file.is_file()

                and

                file.suffix.lower()
                in DocumentLoader.SUPPORTED_EXTENSIONS

            ):

                supported_files.append(
                    file
                )

        if len(supported_files) == 0:

            raise FileNotFoundError(

                "No supported requirement document found "
                "inside the input folder."

            )

        if len(supported_files) > 1:

            raise ValueError(

                "Multiple requirement documents found "
                "inside the input folder. "
                "Keep only one supported document."

            )

        document = supported_files[0]

        extension = (
            document.suffix.lower()
        )

        if extension == ".txt":

            return (
                document.read_text(
                    encoding="utf-8"
                )
            )

        if extension == ".pdf":

            return (
                DocumentLoader.load_pdf(
                    document
                )
            )

        if extension == ".docx":

            return (
                DocumentLoader.load_docx(
                    document
                )
            )

        raise ValueError(
            f"Unsupported document type: {extension}"
        )

    @staticmethod
    def load_pdf(
        path: Path
    ) -> str:

        document = fitz.open(
            path
        )

        text = ""

        for page in document:

            text += (
                page.get_text()
                + "\n"
            )

        document.close()

        return text.strip()

    @staticmethod
    def load_docx(
        path: Path
    ) -> str:

        document = Document(
            path
        )

        text = []

        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                text.append(
                    paragraph.text.strip()
                )

        return "\n".join(
            text
        )