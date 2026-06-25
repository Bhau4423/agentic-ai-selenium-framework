from agents.requirement_agent.prompt_builder import (
    PromptBuilder
)

from agents.requirement_agent.parser import (
    RequirementParser
)

from agents.requirement_agent.validator import (
    RequirementValidator
)

from agents.requirement_agent.chunker import (
    RequirementChunker
)

from agents.requirement_agent.merger import (
    RequirementMerger
)

from agents.requirement_agent.deduplicator import (
    RequirementDeduplicator
)

from agents.requirement_agent.coverage_validator import (
    CoverageValidator
)

from agents.requirement_agent.url_extractor import (
    URLExtractor
)

from agents.requirement_agent.id_normalizer import (
    IDNormalizer
)

from services.llm_service import (
    LLMService
)

from services.file_service import (
    FileService
)

from agents.requirement_agent.title_normalizer import (
    TitleNormalizer
)


class RequirementAgent:

    def __init__(self):

        self.llm = LLMService()

    def analyze(
        self,
        requirement_document: str
    ):

        print(
            "\n========== AGENT 1 STARTED =========="
        )

        chunks = (
            RequirementChunker.chunk_text(
                requirement_document
            )
        )

        print(
            f"\nDocument Chunks: "
            f"{len(chunks)}"
        )

        successful_results = []

        failed_chunks = []

        for index, chunk in enumerate(
            chunks,
            start=1
        ):

            print(
                f"\nProcessing Chunk "
                f"{index}/{len(chunks)}"
            )

            try:

                prompt = (
                    PromptBuilder.build_prompt(
                        chunk
                    )
                )

                response = (
                    self.llm.invoke(
                        prompt
                    )
                )

                result = (
                    RequirementParser.parse(
                        response
                    )
                )

                successful_results.append(
                    result
                )

            except Exception as e:

                failed_chunks.append(
                    {
                        "chunk": index,
                        "error": str(e)
                    }
                )

                print(
                    f"Chunk {index}: FAILED"
                )

                print(e)

        if not successful_results:

            raise ValueError(
                "All chunks failed. "
                "Unable to generate requirements."
            )

        print(
            "\nMerging Chunk Results..."
        )

        merged_result = (
            RequirementMerger.merge(
                successful_results
            )
        )

        print(
            "\nRemoving Duplicate Requirements..."
        )

        merged_result = (
            RequirementDeduplicator
            .deduplicate(
                merged_result
            )
        )

        print(
            "\nNormalizing Scenario IDs..."
       )

        merged_result = (
            IDNormalizer.normalize(
                merged_result
            )
        )

        print(
            "\nNormalizing Scenario Titles..."
      )

        merged_result = (
            TitleNormalizer.normalize(
                merged_result
            )
       )

        print(
            "\nExtracting URLs..."
        )

        merged_result = (
            URLExtractor.extract(
                merged_result,
                requirement_document
            )
        )

        print(
            f"Base URL: "
            f"{merged_result.base_url}"
        )

        print(
            f"Application URLs: "
            f"{len(merged_result.application_urls)}"
        )

        # print(
        #     "\nRunning Coverage Validation..."
        # )

        coverage_findings = (
            CoverageValidator.validate(
                merged_result
            )
        )

        # --------------------------------
        # TRACEABILITY SUMMARY
        # --------------------------------

        # print(
        #     "\n========== TRACEABILITY SUMMARY =========="
        # )

        # print(
        #     f"Requirements         : "
        #     f"{len(merged_result.requirements)}"
        # )

        # print(
        #     f"Acceptance Criteria  : "
        #     f"{len(merged_result.acceptance_criteria)}"
        # )

        # print(
        #     f"Positive Scenarios   : "
        #     f"{len(merged_result.positive_scenarios)}"
        # )

        # print(
        #     f"Negative Scenarios   : "
        #     f"{len(merged_result.negative_scenarios)}"
        # )

        # print(
        #     f"Boundary Scenarios   : "
        #     f"{len(merged_result.boundary_scenarios)}"
        # )

        print(
            "\nRunning Coverage Validation..."
        )

        print(
            f"Coverage Findings : "
            f"{len(coverage_findings)}"
        )

        if coverage_findings:

            # print(
            #     "\n========== COVERAGE DETAILS =========="
            # )

            high_count = 0
            medium_count = 0

            for finding in coverage_findings:

                if (
                    finding.severity
                    == "HIGH"
                ):
                    high_count += 1

                if (
                    finding.severity
                    == "MEDIUM"
                ):
                    medium_count += 1

                # print(
                #     f"\n[{finding.severity}] "
                #     f"{finding.finding_id}"
                # )

                # print(
                #     f"Requirement ID: "
                #     f"{finding.requirement_id}"
                # )

                # print(
                #     f"Description: "
                #     f"{finding.description}"
                # )

                # print(
                #     f"Recommendation: "
                #     f"{finding.recommendation}"
                # )

            # print(
            #     "\n========== COVERAGE SUMMARY =========="
            # )

            # print(
            #     f"HIGH   : {high_count}"
            # )

            # print(
            #     f"MEDIUM : {medium_count}"
            # )

        # print(
        #     f"\nTotal Requirements: "
        #     f"{len(merged_result.requirements)}"
        # )

        # print(
        #     f"Total Acceptance Criteria: "
        #     f"{len(merged_result.acceptance_criteria)}"
        # )

        # print(
        #     f"Total Positive Scenarios: "
        #     f"{len(merged_result.positive_scenarios)}"
        # )

        # print(
        #     f"Total Negative Scenarios: "
        #     f"{len(merged_result.negative_scenarios)}"
        # )

        # print(
        #     f"Total Boundary Scenarios: "
        #     f"{len(merged_result.boundary_scenarios)}"
        # )

        errors = (
            RequirementValidator.validate(
                merged_result
            )
        )

        if errors:

            raise ValueError(
                f"Validation Failed: {errors}"
            )

        FileService.save_json(

            "data/intermediate/requirement_analysis.json",

            merged_result.model_dump()
        )

        if failed_chunks:

            print(
                "\n========== FAILED CHUNKS =========="
            )

            for failure in failed_chunks:

                print(
                    f"Chunk "
                    f"{failure['chunk']} "
                    f"-> "
                    f"{failure['error']}"
                )

        print(
            "\n========== AGENT 1 COMPLETED =========="
        )

        return merged_result