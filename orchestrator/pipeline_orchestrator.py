import time

from pathlib import Path

from agents import requirement_agent
from agents.requirement_agent.agent import (
    RequirementAgent
)

from agents.discovery_agent.agent import (
    DiscoveryAgent
)

from agents.generator_agent.agent import (
    GeneratorAgent
)

from agents.reviewer_agent.review_cycle_manager import (
    ReviewCycleManager
)

from orchestrator.execution_summary_generator import (
    ExecutionSummaryGenerator
)


class PipelineOrchestrator:

    def __init__(self):

        self.requirement_file = Path(
            "input/requirements.txt"
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
            # AGENT 1
            # ====================================================

            self.print_section(
                "[1/4] REQUIREMENT ANALYSIS"
            )

            self.print_status(
                "RUNNING"
            )

            if not self.requirement_file.exists():

                raise FileNotFoundError(
                    f"Requirement file not found: "
                    f"{self.requirement_file}"
                )

            requirement_document = (
                self.requirement_file.read_text(
                    encoding="utf-8"
                )
            )

            agent_start = time.time()

            requirement_agent = (
                RequirementAgent()
            )

            requirement_result = (
                requirement_agent.analyze(
                    requirement_document
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

            print(
                f"Requirements Extracted : "
                f"{len(requirement_result.requirements)}"
            )

            print(
                f"Acceptance Criteria    : "
                f"{len(requirement_result.acceptance_criteria)}"
            )

            print(
                f"Positive Scenarios     : "
                f"{len(requirement_result.positive_scenarios)}"
            )

            print(
                f"Negative Scenarios     : "
                f"{len(requirement_result.negative_scenarios)}"
            )

            print(
                f"Boundary Scenarios     : "
                f"{len(requirement_result.boundary_scenarios)}"
            )

            # ====================================================
            # AGENT 2
            # ====================================================

            self.print_section(
                "[2/4] APPLICATION DISCOVERY"
            )

            self.print_status(
                "RUNNING"
            )

            agent_start = time.time()

            discovery_agent = (
                DiscoveryAgent()
            )

            discovery_result = (
                discovery_agent.discover(
                    self.application_url
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

            print(
                f"Pages Found           : "
                f"{discovery_result['pages']}"
            )

            print(
                f"Elements Found        : "
                f"{discovery_result['elements']}"
            )

            print(
                f"Forms Found           : "
                f"{discovery_result['forms']}"
            )

            print(
                f"Links Found           : "
                f"{discovery_result['links']}"
            )

            print(
                f"Tables Found          : "
                f"{discovery_result['tables']}"
            )

            print(
                f"Inventory File        : "
                f"{discovery_result['inventory_file']}"
            )

            # ====================================================
            # AGENT 3
            # ====================================================

            self.print_section(
                "[3/4] FRAMEWORK GENERATION"
            )

            self.print_status(
                "RUNNING"
            )

            agent_start = time.time()

            generator_agent = (
                GeneratorAgent()
            )

            generation_result = (
                generator_agent.generate_framework()
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

            print(
                f"Generated Pages       : "
                f"{len(generation_result['generated_pages'])}"
            )

            print(
                f"Generated Tests       : "
                f"{len(generation_result['generated_tests'])}"
            )

            print(
                f"Scenario Mappings     : "
                f"{generation_result['scenario_mappings']}"
            )

            print(
                f"Requirement Mappings  : "
                f"{generation_result['requirement_mappings']}"
            )

            print(
                f"Traceability Matrix   : "
                f"{generation_result['traceability']}"
            )

            # ====================================================
            # AGENT 4
            # ====================================================

            self.print_section(
                "[4/4] REVIEW & SELF HEALING"
            )

            self.print_status(
                "RUNNING"
            )

            agent_start = time.time()

            review_result = (
                ReviewCycleManager.execute()
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

            print(
                f"Review Status         : "
                f"{review_result['status']}"
            )

            print(
                f"Review Iteration      : "
                f"{review_result['iteration']}"
            )

            print(
                f"Validation Report     : "
                f"{review_result['report']}"
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