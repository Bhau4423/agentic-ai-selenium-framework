class RequirementChunker:

    DEFAULT_CHUNK_SIZE = 6000

    @staticmethod
    def chunk_text(
        document: str,
        chunk_size: int = DEFAULT_CHUNK_SIZE
    ):

        if not document:

            return []

        document = document.strip()

        chunks = []

        start = 0

        while start < len(document):

            end = start + chunk_size

            if end >= len(document):

                chunks.append(
                    document[start:]
                )

                break

            split_index = document.rfind(
                "\n",
                start,
                end
            )

            if split_index == -1:

                split_index = end

            chunk = document[
                start:split_index
            ].strip()

            if chunk:

                chunks.append(
                    chunk
                )

            start = split_index

        return chunks