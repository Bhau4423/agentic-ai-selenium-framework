import time

from pathlib import Path

from langgraph_workflow.workflow import (
    LangGraphWorkflow
)

from orchestrator.execution_summary_generator import (
    ExecutionSummaryGenerator
)


class PipelineOrchestrator:

    def __init__(self):

        self.requirement_file = Path(
            "input/srs_document.txt"
        )

        self.application_url = (
            "https://practicetestautomation.com/practice-test-login/"
        )

    @staticmethod
    def print_banner():

        print("\n")

        print("=" * 70)
        print(
            " AGENTIC AI POWERED SELENIUM FRAMEWORK "
        )
        print("=" * 70)

    @staticmethod
    def print_section(
        title: str
    ):

        print("\n")
        print("-" * 70)
        print(title)
        print("-" * 70)

    @staticmethod
    def print_status(
        status: str
    ):

        print(
            f"Status : {status}"
        )

    @staticmethod
    def print_success():

        print(
            "Result : SUCCESS"
        )

    def run(self):

        start_time = time.time()

        self.print_banner()

        try:

            # ====================================================
            # LANGGRAPH EXECUTION
            # ====================================================

            self.print_section(
                "LANGGRAPH EXECUTION"
            )

            self.print_status(
                "RUNNING"
            )

            agent_start = time.time()

            graph = (
                LangGraphWorkflow.build()
            )

            graph_result = graph.invoke(

                {
                    "requirement_document":
                        self.requirement_file.read_text(
                            encoding="utf-8"
                        ),

                    "review_iteration":
                        1
                }

            )

            # =====================================
            # EXTRACT NODE RESULTS
            # =====================================

            requirement_result = (
                graph_result.get(
                    "requirement_result"
                )
            )

            discovery_result = (
                graph_result.get(
                    "discovery_result"
                )
            )

            generation_result = (
                graph_result.get(
                    "generation_result"
                )
            )

            review_result = (
                graph_result.get(
                    "review_result"
                )
            )

            agent_time = (
                time.time()
                - agent_start
            )

            self.print_status(
                "COMPLETED"
            )

            self.print_success()

            self.print_execution_time(
                agent_time
            )

            # ====================================================
            # FINAL SUMMARY
            # ====================================================

            total_time = round(
                time.time() - start_time,
                2
            )

            self.print_section(
                "FINAL EXECUTION SUMMARY"
            )

            print(
                f"Framework Status      : "
                f"{review_result['status']}"
            )

            self.print_execution_time(
                total_time
            )

            print("\nRequirement Analysis")

            print(
                f"Requirements          : "
                f"{len(requirement_result.requirements)}"
            )

            print(
                f"Acceptance Criteria   : "
                f"{len(requirement_result.acceptance_criteria)}"
            )

            print(
                f"Positive Scenarios    : "
                f"{len(requirement_result.positive_scenarios)}"
            )

            print(
                f"Negative Scenarios    : "
                f"{len(requirement_result.negative_scenarios)}"
            )

            print(
                f"Boundary Scenarios    : "
                f"{len(requirement_result.boundary_scenarios)}"
            )

            print("\nApplication Discovery")

            print(
                f"Pages                 : "
                f"{discovery_result['pages']}"
            )

            print(
                f"Elements              : "
                f"{discovery_result['elements']}"
            )

            print(
                f"Forms                 : "
                f"{discovery_result['forms']}"
            )

            print(
                f"Links                 : "
                f"{discovery_result['links']}"
            )

            print(
                f"Tables                : "
                f"{discovery_result['tables']}"
            )

            print("\nFramework Generation")

            print(
                f"Generated Pages       : "
                f"{len(generation_result['generated_pages'])}"
            )

            print(
                f"Generated Tests       : "
                f"{len(generation_result['generated_tests'])}"
            )

            print("\nReview & Validation")

            print(
                f"Review Iterations     : "
                f"{review_result['iteration']}"
            )

            print(
                f"Validation Report     : "
                f"{review_result['report']}"
            )

            # ====================================================
            # EXECUTION SUMMARY JSON
            # ====================================================

            summary = {

                "status":
                    review_result["status"],

                "execution_time_seconds":
                    total_time,

                "requirements":
                    len(
                        requirement_result.requirements
                    ),

                "acceptance_criteria":
                    len(
                        requirement_result.acceptance_criteria
                    ),

                "positive_scenarios":
                    len(
                        requirement_result.positive_scenarios
                    ),

                "negative_scenarios":
                    len(
                        requirement_result.negative_scenarios
                    ),

                "boundary_scenarios":
                    len(
                        requirement_result.boundary_scenarios
                    ),

                "pages":
                    discovery_result["pages"],

                "elements":
                    discovery_result["elements"],

                "forms":
                    discovery_result["forms"],

                "links":
                    discovery_result["links"],

                "tables":
                    discovery_result["tables"],

                "generated_pages":
                    len(
                        generation_result[
                            "generated_pages"
                        ]
                    ),

                "generated_tests":
                    len(
                        generation_result[
                            "generated_tests"
                        ]
                    ),

                "review_iterations":
                    review_result["iteration"],

                "final_report":
                    review_result["report"],

                "status_message":
                    (
                        "FRAMEWORK APPROVED"
                        if review_result["status"]
                        == "APPROVED"
                        else
                        "FRAMEWORK REJECTED"
                    )
            }

            summary_file = (
                ExecutionSummaryGenerator.save(
                    summary
                )
            )

            print(
                f"Execution Summary    : "
                f"{summary_file}"
            )

            print("\n")

            print("=" * 70)

            print(
                " PIPELINE STATUS "
            )

            print("=" * 70)

            print()

            print(
                f"{'Requirement Agent':<25}"
               f": COMPLETED"
            )

            print(
                f"{'Discovery Agent':<25}"
                f": COMPLETED"
            )

            print(
                f"{'Generator Agent':<25}"
                f": COMPLETED"
            )

            print(
                f"{'Reviewer Agent':<25}"
                f": {review_result['status']}"
            )

            print()

            print("=" * 70)

            if (
                review_result["status"]
                ==
                "APPROVED"
            ):

                print(
                    " FRAMEWORK APPROVED "
                )

            else:

                print(
                    " FRAMEWORK REJECTED "
                )

            print("=" * 70)

        except Exception as error:

            print("\n")

            print("=" * 70)
            print(
                " PIPELINE EXECUTION FAILED "
            )
            print("=" * 70)

            print(
                f"Error : {error}"
            )
    
    @staticmethod
    def print_execution_time(
        seconds: float
    ):

        minutes = int(
            seconds // 60
        )

        remaining = int(
            seconds % 60
        )

        if minutes == 0:

            print(
                f"Execution Time : {remaining} sec"
            )

        else:

            print(
                f"Execution Time : "
                f"{minutes} min "
                f"{remaining} sec"
            )