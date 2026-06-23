# Agentic AI Capstone Project using LangGraph

## Overview

Agentic AI Capstone Project using LangGraph is an autonomous test automation framework that leverages AI agents to analyze requirements, discover application elements, generate automation frameworks, review generated artifacts, and perform self-healing through iterative validation cycles.

The framework demonstrates how Agentic AI can reduce manual effort involved in traditional automation framework development by orchestrating specialized agents through LangGraph workflows.

---

## Business Problem

Traditional test automation requires significant manual effort:

* Requirement analysis
* Test scenario identification
* UI element discovery
* Framework development
* Test script creation
* Review and maintenance

These activities consume substantial engineering time and often introduce human error.

This project addresses these challenges by introducing an AI-driven autonomous workflow capable of generating, reviewing, and repairing automation assets with minimal human intervention.

---

## Objectives

* Automate requirement analysis
* Discover application structure dynamically
* Generate automation frameworks automatically
* Validate generated assets
* Detect defects and coverage gaps
* Apply automated fixes
* Demonstrate Agentic AI orchestration using LangGraph

---

## Technology Stack

### AI & Orchestration

* LangGraph
* LangChain
* Generative AI Models
* Pydantic

### Automation

* Playwright (Application Discovery)
* Selenium (Generated Framework)

### Programming Language

* Python

### Reporting

* JSON Reports
* CSV Traceability Matrix

---

## System Architecture

```text
Requirement Document
        │
        ▼
┌─────────────────────┐
│ Requirement Agent   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Discovery Agent     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Generator Agent     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Reviewer Agent      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Approval Router     │
│ (LangGraph)         │
└───────┬─────┬───────┘
        │     │
 APPROVED     REVIEWED
        │         │
        ▼         ▼
       END   Patch Agent
                  │
                  ▼
           Reviewer Agent
```

---

## Agent Architecture

### Agent 1 - Requirement Analyst

Responsibilities:

* Parse BRD/User Stories
* Extract Requirements
* Generate Acceptance Criteria
* Generate Positive Scenarios
* Generate Negative Scenarios
* Generate Boundary Scenarios

Outputs:

* requirement_analysis.json

---

### Agent 2 - Discovery Agent

Responsibilities:

* Crawl application pages
* Discover forms
* Discover inputs
* Discover buttons
* Discover dropdowns
* Discover checkboxes
* Discover radio buttons
* Discover textareas
* Discover tables

Outputs:

* page_inventory.json

---

### Agent 3 - Framework Generator

Responsibilities:

* Map requirements to UI
* Generate Page Objects
* Generate Test Scripts
* Generate Framework Structure
* Generate Traceability Matrix

Outputs:

* Generated Selenium Framework
* Traceability Matrix

---

### Agent 4 - Reviewer & Self-Healing Agent

Responsibilities:

* Assertion Validation
* Coverage Validation
* Wait Validation
* Locator Validation
* Traceability Validation
* Hallucination Detection
* Edge Case Validation

Outputs:

* Review Reports
* Patch Reports
* Final Validation Reports

---

## LangGraph Workflow

The framework uses LangGraph as the orchestration layer.

Workflow:

```text
START
  │
  ▼
Requirement Node
  │
  ▼
Discovery Node
  │
  ▼
Generator Node
  │
  ▼
Reviewer Node
  │
  ▼
Approval Node
  │
  ▼
Conditional Routing
  │
  ├── APPROVED → END
  │
  └── REVIEWED → Patch Node
                      │
                      ▼
                 Reviewer Node
```

Features:

* State Management
* Conditional Routing
* Agent Collaboration
* Self-Healing Loop
* Maximum Iteration Protection

---

## Project Structure

```text
agentic-ai-capstone-project/

├── agents/
│   ├── requirement_agent/
│   ├── discovery_agent/
│   ├── generator_agent/
│   └── reviewer_agent/
│
├── langgraph_workflow/
│   ├── graph_state.py
│   ├── workflow.py
│   └── nodes/
│
├── generated_framework/
│
├── orchestrator/
│
├── output/
│
├── input/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Generated Outputs

### Requirement Analysis

```text
requirement_analysis.json
```

### Discovery Inventory

```text
page_inventory.json
```

### Traceability

```text
traceability_matrix.csv
```

### Review Reports

```text
review_report.json
patch_report.json
final_validation_report.json
```

### Execution Summary

```text
execution_summary.json
```

---

## How To Run

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute Framework

```bash
python main.py
```

### Execute LangGraph Workflow

```bash
python test_langgraph_workflow.py
```

---

## Key Features

* Multi-Agent Architecture
* LangGraph Orchestration
* Autonomous Discovery
* Automatic Framework Generation
* Self-Healing Review Process
* Traceability Matrix Generation
* Coverage Validation
* Hallucination Detection
* Patch-Based Repair
* Execution Reporting

---

## Business Benefits

* Reduced Automation Development Effort
* Faster Test Framework Creation
* Improved Requirement Coverage
* Reduced Human Error
* Enhanced Maintainability
* AI-Assisted Validation
* Automated Review Cycles

---

## Future Roadmap

### Phase 1 (Completed)

* Requirement Agent
* Discovery Agent
* Generator Agent
* Reviewer Agent
* LangGraph Workflow
* Self-Healing Loop

### Phase 2 (In Progress)

* Dashboard
* Architecture Visualization
* Real Requirement Validation

### Phase 3 (Post Approval)

* Python + Playwright Framework Generation
* Playwright Page Objects
* Playwright Test Generation
* Advanced AI Planning
* Multi-Framework Support

---

## Author

Shubham Patil

Agentic AI Capstone Project using LangGraph
