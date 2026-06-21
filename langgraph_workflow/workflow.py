from langgraph.graph import (
    StateGraph,
    END
)

from langgraph_workflow.graph_state import (
    GraphState
)

from langgraph_workflow.nodes.requirement_node import (
    requirement_node
)

from langgraph_workflow.nodes.discovery_node import (
    discovery_node
)

from langgraph_workflow.nodes.generator_node import (
    generator_node
)

from langgraph_workflow.nodes.reviewer_node import (
    reviewer_node
)

from langgraph_workflow.nodes.patch_node import (
    patch_node
)

from langgraph_workflow.nodes.approval_node import (
    approval_node
)


class LangGraphWorkflow:

    @staticmethod
    def approval_router(
        state
    ):

        status = (
            state.get(
                "status",
                "REJECTED"
            )
        )

        print(
            f"\n[LangGraph] Routing Decision: {status}"
        )

        if status == "APPROVED":

            return "approved"

        return "patch"

    @staticmethod
    def build():

        workflow = StateGraph(
            GraphState
        )

        # --------------------------------
        # NODES
        # --------------------------------

        workflow.add_node(
            "requirement",
            requirement_node
        )

        workflow.add_node(
            "discovery",
            discovery_node
        )

        workflow.add_node(
            "generator",
            generator_node
        )

        workflow.add_node(
            "reviewer",
            reviewer_node
        )

        workflow.add_node(
            "approval",
            approval_node
        )

        workflow.add_node(
            "patch",
            patch_node
        )

        # --------------------------------
        # ENTRY
        # --------------------------------

        workflow.set_entry_point(
            "requirement"
        )

        # --------------------------------
        # MAIN FLOW
        # --------------------------------

        workflow.add_edge(
            "requirement",
            "discovery"
        )

        workflow.add_edge(
            "discovery",
            "generator"
        )

        workflow.add_edge(
            "generator",
            "reviewer"
        )

        workflow.add_edge(
            "reviewer",
            "approval"
        )

        # --------------------------------
        # CONDITIONAL ROUTING
        # --------------------------------

        workflow.add_conditional_edges(

            "approval",

            LangGraphWorkflow.approval_router,

            {
                "approved": END,
                "patch": "patch"
            }
        )

        # --------------------------------
        # SELF HEAL LOOP
        # --------------------------------

        workflow.add_edge(
            "patch",
            "reviewer"
        )

        return workflow.compile()