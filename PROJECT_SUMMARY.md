# Project Summary and Key Lessons

## What this project is

An **AI-powered agentic workflow for project management**. Starting from a product specification (the pilot is an "Email Router"), it produces a structured project plan:

**user stories → product features → engineering tasks**

The scenario is a startup whose technical project managers are overloaded and produce inconsistent plans. The goal is a reusable system that makes this step consistent and scalable.

## The two phases

### Phase 1: the agent toolkit (`starter/phase_1/workflow_agents/base_agents.py`)

Reusable building blocks, each tested with its own script:

| Agent | What it does |
|---|---|
| `DirectPromptAgent` | Sends a prompt to the model and returns the answer (the model's own knowledge). |
| `AugmentedPromptAgent` | Adds a persona through the system prompt. |
| `KnowledgeAugmentedPromptAgent` | Adds a persona plus supplied knowledge the model must rely on. |
| `RAGKnowledgePromptAgent` | Retrieves relevant text chunks via embeddings, then answers from them (provided). |
| `EvaluationAgent` | A worker answers, an evaluator judges it against criteria, and feedback loops until it passes or runs out of attempts. |
| `RoutingAgent` | Picks the right agent for a prompt by comparing embeddings. |
| `ActionPlanningAgent` | Splits a large goal into ordered steps. |

### Phase 2: the workflow (`starter/phase_2/agentic_workflow.py`)

1. The **action planning agent** turns the request into steps.
2. The **routing agent** sends each step to the matching role.
3. Each role is a **knowledge agent** checked by an **evaluation agent**:
   - **Product Manager**: personas and user stories.
   - **Program Manager**: groups stories into features.
   - **Development Engineer**: defines engineering tasks.
4. The validated results are assembled into one consolidated plan.

## Key lessons

### Agent design
- **Persona and knowledge shape behavior.** The system prompt defines who the agent is and what it should rely on.
- **Small, single-purpose agents compose well.** Each class does one job, and the workflow combines them.
- **Evaluation loops raise quality.** A separate judge with explicit criteria, and a limit on retries, catches format errors. It checks structure far better than truth.
- **Routing by embeddings is semantic matching.** Cosine similarity compares meaning. Route descriptions should say what an agent does *and does not* do, so similar roles stay distinct.
- **Plan first, then execute.** Decomposing a big request into steps keeps each model call focused.

### API and code details
- Multiple `system` messages are allowed; the conventional order is system first, then user.
- `temperature=0` makes evaluator output more repeatable.
- A `lambda` or function stored in a dictionary (`"func"`) lets a router call any agent without knowing its class.
- An evaluator that wraps a worker already calls the worker. Don't call the worker separately and then pass its answer in as the prompt.

### Tooling and environment
- Use one **virtual environment per project** and select it in VS Code (**Python: Select Interpreter**).
- **Pylance** analyzes code (types, imports); **Black** formats; a linter like **Ruff** checks style, including line length.

### Judging agentic workflows
- They are strong at **structured, repeatable drafting** and weaker at judgment, so keep a human accountable.
- Errors compound across steps, and each extra agent adds cost and latency.
- To compare against a single prompt, use the same model and input, repeat runs, and measure format compliance, coverage, traceability, variance, tokens, calls and latency.

## Where to go next
- Run the full workflow and review each section of the plan yourself.
- Add automated checks for traceability (every task references a story).
- Compare the workflow with a single-prompt baseline using the metrics above.
