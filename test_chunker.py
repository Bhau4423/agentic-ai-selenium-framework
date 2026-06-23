from pathlib import Path

from agents.requirement_agent.chunker import (
    RequirementChunker
)


file_path = Path(
    "input/srs_document.txt"
)

with open(
    file_path,
    "r",
    encoding="utf-8"
) as file:

    document = file.read()

chunks = (
    RequirementChunker.chunk_text(
        document
    )
)

print(
    f"\nTotal Chunks: {len(chunks)}"
)

for index, chunk in enumerate(
    chunks,
    start=1
):

    print(
        f"\nChunk {index}"
    )

    print(
        f"Characters: {len(chunk)}"
    )