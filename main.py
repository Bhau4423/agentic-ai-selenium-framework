from orchestrator.pipeline_orchestrator import (
    PipelineOrchestrator
)


if __name__ == "__main__":

    orchestrator = (
        PipelineOrchestrator()
    )

    orchestrator.run()