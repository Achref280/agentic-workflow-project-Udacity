# agentic_workflow.py

# TODO: 1 - Import the following agents: ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the workflow_agents.base_agents module
from workflow_agents.base_agents import (
    ActionPlanningAgent,
    KnowledgeAugmentedPromptAgent,
    EvaluationAgent,
    RoutingAgent,
)
import os
import re
from dotenv import load_dotenv

# TODO: 2 - Load the OpenAI key into a variable called openai_api_key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# load the product spec
# TODO: 3 - Load the product spec document Product-Spec-Email-Router.txt into a variable called product_spec
with open("starter/phase_2/Product-Spec-Email-Router.txt", "r") as f:
    product_spec = f.read()

# Instantiate all the agents

# Action Planning Agent
knowledge_action_planning = (
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
    "A development Plan for a product contains all these components. \n"
    "Each step is assigned to one role, written as a label at the start of the line, "
    "one step per line, without numbering or bullets: \n"
    "Product Manager: defines user stories. \n"
    "Program Manager: defines product features by grouping user stories. \n"
    "Development Engineer: defines engineering tasks for the stories and features. \n"
    "Only include the steps the request needs, ordered so that stories come before features "
    "and features before tasks. Never include a step that compiles, consolidates or "
    "summarizes the results; the workflow assembles the final plan itself."
)
# TODO: 4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = ActionPlanningAgent(
    openai_api_key=openai_api_key, knowledge=knowledge_action_planning
)

# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    # TODO: 5 - Complete this knowledge string by appending the product_spec loaded in TODO 3
    f"\nProduct Spec:\n{product_spec}"
)
# TODO: 6 - Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_product_manager,
    knowledge=knowledge_product_manager,
)

# Product Manager - Evaluation Agent
# TODO: 7 - Define the persona and evaluation criteria for a Product Manager evaluation agent and instantiate it as product_manager_evaluation_agent. This agent will evaluate the product_manager_knowledge_agent.
# The evaluation_criteria must be the full string:
#                      "The answer should be stories that follow the following structure: " \
#                      "As a [type of user], I want [an action or feature] so that [benefit/value]."
# Pass product_manager_knowledge_agent as the agent_to_evaluate parameter.
product_manager_evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona="You are an evaluation agent that checks the answers of other worker agents.",
    evaluation_criteria="The answer should be stories that follow the following structure: "
    "As a [type of user], I want [an action or feature] so that [benefit/value].",
    agent_to_evaluate=product_manager_knowledge_agent,
    max_interactions=3
)
# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = (
    "Features of a product are defined by organizing similar user stories into cohesive groups. "
    "Write every feature with exactly these labelled fields:\n"
    "Feature Name: A clear, concise title that identifies the capability\n"
    "Description: A brief explanation of what the feature does and its purpose\n"
    "Key Functionality: The specific capabilities or actions the feature provides\n"
    "User Benefit: How this feature creates value for the user"
)
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
# (This is a necessary step before TODO 8. Students should add the instantiation code here.)
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_program_manager,
    knowledge=knowledge_program_manager,
)

# Program Manager - Evaluation Agent
persona_program_manager_eval = (
    "You are an evaluation agent that checks the answers of other worker agents."
)

# TODO: 8 - Instantiate a program_manager_evaluation_agent using 'persona_program_manager_eval' and the evaluation criteria below.
#                      "The answer should be product features that follow the following structure: " \
#                      "Feature Name: A clear, concise title that identifies the capability\n" \
#                      "Description: A brief explanation of what the feature does and its purpose\n" \
#                      "Key Functionality: The specific capabilities or actions the feature provides\n" \
#                      "User Benefit: How this feature creates value for the user"
# Pass program_manager_knowledge_agent as the agent_to_evaluate parameter.
program_manager_evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona=persona_program_manager_eval,
    evaluation_criteria="The answer should be product features that follow the following structure: "
    "Feature Name: A clear, concise title that identifies the capability\n"
    "Description: A brief explanation of what the feature does and its purpose\n"
    "Key Functionality: The specific capabilities or actions the feature provides\n"
    "User Benefit: How this feature creates value for the user",
    agent_to_evaluate=program_manager_knowledge_agent,
    max_interactions=3
)


# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = (
    "Development tasks are defined by identifying what needs to be built to implement each user story. "
    "Write every task with exactly these labelled fields, one task per user story or feature:\n"
    "Task ID: A unique identifier for tracking purposes\n"
    "Task Title: Brief description of the specific development work\n"
    "Related User Story: Reference to the parent user story\n"
    "Description: Detailed explanation of the technical work required\n"
    "Acceptance Criteria: Specific requirements that must be met for completion\n"
    "Estimated Effort: Time or complexity estimation\n"
    "Dependencies: Any tasks that must be completed first"
)
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_dev_engineer,
    knowledge=knowledge_dev_engineer,
)

# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = (
    "You are an evaluation agent that checks the answers of other worker agents."
)
# TODO: 9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.
#                      "The answer should be tasks following this exact structure: " \
#                      "Task ID: A unique identifier for tracking purposes\n" \
#                      "Task Title: Brief description of the specific development work\n" \
#                      "Related User Story: Reference to the parent user story\n" \
#                      "Description: Detailed explanation of the technical work required\n" \
#                      "Acceptance Criteria: Specific requirements that must be met for completion\n" \
#                      "Estimated Effort: Time or complexity estimation\n" \
#                      "Dependencies: Any tasks that must be completed first"
# Pass development_engineer_knowledge_agent as the agent_to_evaluate parameter.
development_engineer_evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona=persona_dev_engineer_eval,
    max_interactions=3,
    evaluation_criteria="The answer should be tasks following this exact structure: "
    "Task ID: A unique identifier for tracking purposes\n"
    "Task Title: Brief description of the specific development work\n"
    "Related User Story: Reference to the parent user story\n"
    "Description: Detailed explanation of the technical work required\n"
    "Acceptance Criteria: Specific requirements that must be met for completion\n"
    "Estimated Effort: Time or complexity estimation\n"
    "Dependencies: Any tasks that must be completed first",
    agent_to_evaluate=development_engineer_knowledge_agent,
)

# Routing Agent
# TODO: 10 - Instantiate a routing_agent. 
# You will need to define a list of agent dictionaries (routes) for 
# Product Manager, Program Manager, and Development Engineer.
#  Each dictionary should contain 
# 'name', 'description', and 'func' (linking to a support function).
#  Assign this list to the routing_agent's 'agents' attribute.

# Job function persona support functions
# TODO: 11 - Define the support functions for the routes of the routing agent 
# (e.g., product_manager_support_function, program_manager_support_function, 
# development_engineer_support_function).
# Each support function should:
#   1. Take the input query (e.g., a step from the action plan).
#   2. Get a response from the respective Knowledge Augmented Prompt Agent.
#   3. Have the response evaluated by the corresponding Evaluation Agent.
#   4. Return the final validated response.
def product_manager_support_function(query):
    return product_manager_evaluation_agent.evaluate(query)["final_response"]

def program_manager_support_function(query):
    return program_manager_evaluation_agent.evaluate(query)["final_response"]

def development_engineer_support_function(query):
    return development_engineer_evaluation_agent.evaluate(query)["final_response"]
# Run the workflow

routing_agent = RoutingAgent(
    openai_api_key=openai_api_key,
    agents=[
        {
            "name": "Product Manager",
            "description": "Responsible for defining product personas and user stories only."
            " Does not define features or tasks. Does not group stories",
            "func": product_manager_support_function,
        },
        {
            "name": "Program Manager",
            "description": "Responsible for defining product features only, by grouping "
            "similar user stories into cohesive features. Does not define user stories, "
            "personas or development tasks.",
            "func": program_manager_support_function,
        },
        {
            "name": "Development Engineer",
            "description": "Responsible for defining development tasks only, by identifying "
            "what needs to be built to implement each user story. Does not define "
            "personas, user stories or features.",
            "func": development_engineer_support_function,
        },
    ],
)

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
workflow_prompt = "Produce a complete project plan for the Email Router product, including user stories, product features, and engineering tasks."
# ****
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
# TODO: 12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
    #   2. Initialize an empty list to store 'completed_steps'.
completed_steps = []

# Role metadata: output section, dependency order (a role needs the earlier ones),
# and the request keywords that make the role mandatory in the plan.
ROLES = {
    "Product Manager": {
        "section": "User Stories",
        "rank": 0,
        "keywords": ("user stor", "stories"),
    },
    "Program Manager": {
        "section": "Product Features",
        "rank": 1,
        "keywords": ("feature",),
    },
    "Development Engineer": {
        "section": "Engineering Tasks",
        "rank": 2,
        "keywords": ("engineering task", "development task", "tasks"),
    },
}
evaluation_agents = {
    "Product Manager": product_manager_evaluation_agent,
    "Program Manager": program_manager_evaluation_agent,
    "Development Engineer": development_engineer_evaluation_agent,
}
AGGREGATION_PATTERN = re.compile(r"\b(compile|consolidat\w*|assemble|combine|summari[sz]e)\b", re.I)


def parse_plan_step(step):
    """Split a planner line into (role, text); role is None if the label is unknown."""
    cleaned = re.sub(r"^\s*(?:\d+[.)]\s*|[-*]\s*)", "", step).strip()
    role, _, text = cleaned.partition(":")
    role = role.strip().strip("*").strip()
    if role in ROLES and text.strip():
        return role, text.strip()
    return None, cleaned


def check_plan(steps, request):
    """Planner checker: return a list of problems; an empty list means the plan is valid."""
    problems = []
    if not steps:
        return ["The plan is empty."]

    parsed = [parse_plan_step(step) for step in steps]
    for step, (role, text) in zip(steps, parsed):
        if role is None:
            problems.append(
                f"Step '{step}' must start with one of these role labels: {', '.join(ROLES)}."
            )
        elif AGGREGATION_PATTERN.search(text):
            problems.append(
                f"Step '{step}' compiles or summarizes results; remove it, the workflow assembles the plan."
            )

    roles = [role for role, _ in parsed if role]
    ranks = [ROLES[role]["rank"] for role in roles]
    if ranks != sorted(ranks):
        problems.append("Steps are out of order: stories first, then features, then tasks.")

    requested = request.lower()
    for role, info in ROLES.items():
        if any(keyword in requested for keyword in info["keywords"]) and role not in roles:
            problems.append(f"The request needs {info['section']}, but no {role} step was planned.")
    return problems


def plan_workflow(request, max_attempts=3):
    """Run the planner, check its plan, and send the problems back until the plan is valid."""
    prompt = request
    for attempt in range(1, max_attempts + 1):
        steps = action_planning_agent.extract_steps_from_prompt(prompt)
        problems = check_plan(steps, request)
        print(f"Plan attempt {attempt}: {steps}")
        if not problems:
            return [parse_plan_step(step) for step in steps]
        print(f"Plan checker found problems: {problems}")
        prompt = (
            f"{request}\n\nYour previous plan was rejected:\n"
            + "\n".join(f"- {problem}" for problem in problems)
            + "\nReturn a corrected plan."
        )
    raise RuntimeError(f"Planner could not produce a valid plan: {problems}")


workflow_steps = plan_workflow(workflow_prompt)
project_plan = {info["section"]: [] for info in ROLES.values()}

for agent_name, step_text in workflow_steps:
    section = ROLES[agent_name]["section"]
    step = f"{agent_name}: {step_text}"

    print(f"Executing step: {step_text}")
    prior_context = "\n\n".join(
        f"{completed['role']}:\n{completed['content']}"
        for completed in completed_steps
    )
    agent_input = (
        f"Step: {step_text}\n\n"
        f"Product specification:\n{product_spec}"
    )
    if prior_context:
        agent_input += f"\n\nCompleted project-plan sections:\n{prior_context}"

    result = routing_agent.route_prompt(
        step,
        agent_name=agent_name,
        agent_input=agent_input,
    )
    if not routing_agent.best_agent or routing_agent.best_agent["name"] != agent_name:
        raise RuntimeError(f"Workflow step was not routed to {agent_name}")
    evaluation_agent = evaluation_agents[agent_name]
    if (
        not evaluation_agent.last_evaluation
        or not evaluation_agent.last_evaluation.lower().startswith("yes")
    ):
        raise RuntimeError(
            f"{agent_name} did not produce an accepted result for step: {step_text}"
        )

    print(f"Step routed to {agent_name}")
    completed_step = {"role": section, "content": result}
    completed_steps.append(completed_step)
    project_plan[section].append(result)
    print(f"Completed step: {step_text}")
    print(f"Result: {result}")

# TODO: 13 - Implement the assembly step used by TODO 12 step 4.
#   Group the entries in 'completed_steps' by the role that produced them and print one plan, e.g.:
#
#       print("\n*** Consolidated Project Plan ***\n")
#       for section in ("User Stories", "Product Features", "Engineering Tasks"):
#           print(f"--- {section} ---")
#           # print the completed_steps belonging to this section
#
#   Keep the routing input separate from this assembly: route on the short step text only, and do
#   not feed accumulated context back into 'routing_agent.route()'.
print("\n*** Consolidated Project Plan ***\n")
for section, contents in project_plan.items():
    print(f"--- {section} ---")
    if not contents:
        print("(not requested)")
    for content in contents:
        print(content)
