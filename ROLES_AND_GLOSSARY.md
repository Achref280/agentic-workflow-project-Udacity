# Product Development Roles and Key Terms

A study guide based on the Email Router agentic-workflow project.

---

## 1. The big picture

Building a product moves through three questions:

| Question | Role that answers it | Deliverable |
|---|---|---|
| **What** do users need, and why? | Product Manager | User stories |
| **How** do we organize that into a coherent product and plan the delivery? | Program Manager | Features |
| **How** do we build it? | Development Engineer | Engineering tasks |

In this project each role is an AI agent, and an **Action Planning Agent** plays the part of a Technical Program Manager (TPM) who splits the request into steps.

```
Product Spec -> Product Manager -> User Stories
                                      |
                           Program Manager -> Features
                                      |
                       Development Engineer -> Tasks
                                      |
                             Consolidated Project Plan
```

---

## 2. The three roles

### 2.1 Product Manager (PM)

**Mission:** Own the *what* and the *why*. Make sure the team builds something users actually need.

**Typical responsibilities**
- Talk to users and stakeholders and understand their problems.
- Define personas (types of users) and their needs.
- Write user stories and prioritize them (what matters most first).
- Define success metrics, such as "reduce response time by 60%".
- Maintain the product vision and roadmap.
- Decide scope: what is in and what is out.

**Deliverables:** product spec/PRD (product requirements document), user stories, priorities, success metrics.

**In this project:** The Product Manager agent reads the product spec and writes stories such as:
> "As an IT Administrator, I want to configure and monitor the system through a dashboard so that I can ensure performance and security."

**Key skills:** user empathy, prioritization, communication, data-driven decisions, saying no.

**Does NOT:** decide how it is technically built, or manage the delivery schedule across teams.

### 2.2 Program Manager

**Mission:** Own the *organization and delivery* of work across people, teams and time.

**Typical responsibilities**
- Group related stories into cohesive **features** and shape a coherent release.
- Coordinate multiple teams and manage dependencies between them.
- Track timelines, milestones, risks and budgets.
- Remove blockers and report status to stakeholders.
- Keep several related projects aligned toward one goal.

**Deliverables:** feature list, roadmap/schedule, risk register, status reports, dependency maps.

**In this project:** The Program Manager agent groups stories into features, for example:
> **Feature Name:** System Monitoring and Reliability
> **Description:** Monitors the system to detect errors and keep it stable.
> **Key Functionality:** Log events, handle errors, send notifications.
> **User Benefit:** Reliable routing and timely alerts.

**Key skills:** planning, risk management, cross-team coordination, stakeholder communication.

**Does NOT:** decide what the product should be (PM) or write code (engineering).

> **Naming note:** The terms vary by company. A *Technical Program Manager (TPM)* adds technical depth, such as architecture and dependencies. Some companies use "Program Manager" for the role described here, and others use "Project Manager" for single, smaller projects.

### 2.3 Development Engineer (Software Engineer)

**Mission:** Own the *how*. Design and build working, reliable software.

**Typical responsibilities**
- Break stories and features into technical tasks.
- Estimate effort and identify technical risks.
- Design and write code, review others' code, write tests.
- Define acceptance criteria and dependencies for each task.
- Deploy, monitor and fix issues.

**Deliverables:** tasks, code, tests, technical designs, documentation.

**In this project:** The Development Engineer agent writes tasks like:
> **Task ID:** DEV-001
> **Task Title:** Implement the email classification service
> **Related User Story:** US-02
> **Description:** Build an LLM-based classifier that assigns intent and category.
> **Acceptance Criteria:** Returns a category and confidence score for each email.
> **Estimated Effort:** 16 hours
> **Dependencies:** None

**Key skills:** programming, system design, debugging, testing, estimation.

**Does NOT:** decide business priorities (PM) or manage cross-team schedules (Program Manager).

---

## 3. How the roles differ

| Aspect | Product Manager | Program Manager | Development Engineer |
|---|---|---|---|
| **Core question** | What and why? | How do we deliver it together? | How do we build it? |
| **Focus** | Users and value | Execution and coordination | Technology and code |
| **Main artifact** | User stories | Features, roadmap, schedule | Tasks, code, tests |
| **Time horizon** | Product vision and roadmap | Delivery of a program or release | Sprint-level work |
| **Success measure** | Users adopt it, goals are met | On time, on budget, risks managed | Works correctly, quality code |
| **Works with** | Users, stakeholders, design | Many teams, leadership | Other engineers, PMs |
| **Typical metric** | Response time down 60% | Milestones hit | Test coverage, bug count |

**Quick contrast**
- PM vs Program Manager: the PM decides *what to build*, and the Program Manager makes sure it *ships coordinated and on time*.
- PM vs Engineer: the PM states the user need, and the engineer designs the solution.
- Program Manager vs Engineer: the Program Manager tracks *when and who*, and the engineer does the *building*.

**Where roles overlap:** small companies often combine PM and Program Manager. A PM and engineer collaborate on feasibility. Engineers may estimate while Program Managers schedule using those estimates.

---

## 4. Glossary

### Product and requirements terms

| Term | Definition | Example |
|---|---|---|
| **Product spec / PRD** | A document that describes what a product should do, why, and for whom. | `Product-Spec-Email-Router.txt` |
| **Stakeholder** | Anyone with an interest in the product: users, managers, customers, sponsors. | Support team lead |
| **Persona** | A fictional but realistic profile of a type of user, with goals and pain points. | "IT Administrator" |
| **User story** | A short requirement written from the user's view: *As a [user], I want [action] so that [benefit]*. | "As an SME, I want only complex emails routed to me so that I can focus on specialist work." |
| **Epic** | A large body of work that spans many stories. | "Email management" |
| **Feature** | A distinct capability of the product, usually a group of related stories. | "Email Routing Management" |
| **Requirement** | A condition the product must meet. *Functional* = what it does, *non-functional* = how well (speed, security). | "Handle 200% more email" |
| **Use case** | A step-by-step description of how a user achieves a goal with the system. | Admin edits routing rules |
| **Acceptance criteria** | Specific, testable conditions that must be true for work to count as done. | "Returns a category and a confidence score" |
| **Definition of done** | A team-wide checklist that every item must meet (tested, reviewed, documented). | Code reviewed and merged |
| **MVP (Minimum Viable Product)** | The smallest version that delivers real value and lets you learn from users. | Auto-route only; no dashboard yet |
| **Scope / scope creep** | Scope is the agreed boundaries. Creep is uncontrolled growth of them. | CRM integration excluded |
| **Backlog** | The prioritized list of work not yet done. | Product backlog |
| **KPI / success metric** | A measurable number showing whether goals are met. | 90% routing accuracy |
| **Roadmap** | A high-level plan of what will be delivered and roughly when. | Q1 pilot, Q2 full rollout |

### Planning and delivery terms

| Term | Definition |
|---|---|
| **Task** | A concrete unit of engineering work, usually small enough for one person to finish. |
| **Estimated effort** | The time or complexity predicted for a task (hours, days or story points). |
| **Story points** | A relative measure of effort or complexity, not a direct time. |
| **Dependency** | A task or item that must be finished before another can start. |
| **Milestone** | A significant checkpoint in a project, such as "pilot launched". |
| **Risk** | A potential problem that could harm the plan, with a likelihood and an impact. |
| **Blocker** | Something that currently prevents progress. |
| **Sprint** | A fixed work period, commonly 1 to 4 weeks, in Agile teams. |
| **Agile / Scrum** | Iterative ways of working in short cycles with frequent feedback. |
| **Prioritization** | Ranking work by value, effort or urgency (e.g. MoSCoW: Must, Should, Could, Won't). |
| **Pilot phase** | A limited early rollout used to test the product before full release. |

### Hierarchy cheat sheet

```
Product vision
  └─ Epic
       └─ Feature
            └─ User story
                 └─ Task
                      └─ Acceptance criteria / tests
```
A feature groups stories, and a story is broken into tasks.

### AI and agent terms used in this project

| Term | Definition |
|---|---|
| **Agent** | A program that uses an LLM, usually with a role, knowledge and instructions, to complete a task. |
| **LLM (Large Language Model)** | A model trained on text that generates language (e.g. GPT). |
| **Persona (agent)** | The role description given to an agent ("You are a Product Manager"). |
| **Knowledge-augmented agent** | An agent told to answer using supplied knowledge rather than its own. |
| **Action planning agent** | An agent that turns a high-level request into ordered steps. |
| **Routing agent** | An agent that decides which specialist should handle a request, here by embedding similarity. |
| **Evaluation agent** | An agent that checks another agent's output against criteria and requests corrections. |
| **Agentic workflow** | A process where several agents collaborate, each with a role, to complete a goal. |
| **Prompt** | The instruction or input given to an LLM. |
| **Chunk** | A smaller piece of a long text, used to make searching easier. |
| **Embedding** | A list of numbers that captures the meaning of text, so similar texts can be compared. |
| **Cosine similarity** | A score (-1 to 1) of how close two embeddings are in meaning. |
| **RAG (Retrieval-Augmented Generation)** | Retrieving relevant text first, then having an LLM answer using it. |
| **Temperature** | A setting for randomness. 0 gives the most consistent answers. |
| **TPM (Technical Program Manager)** | A program manager with technical depth who coordinates engineering work. |

---

## 5. Worked example: Email Router

**Business need:** Staff lose time sorting emails.

**Persona:** Customer Support Representative.

**User story (PM):**
> As a Customer Support Representative, I want routine inquiries answered automatically so that I can focus on complex issues.

**Feature (Program Manager):** *Response Generation Engine*, grouping the stories about auto-answers, approval workflow and response quality.

**Tasks (Engineer):**
1. DEV-001: Build the retrieval index of approved knowledge. *Effort: 12h. Dependencies: none.*
2. DEV-002: Generate draft responses with a RAG pipeline. *Effort: 16h. Dependencies: DEV-001.*
3. DEV-003: Add an approval screen for edits before sending. *Effort: 10h. Dependencies: DEV-002.*

**Acceptance criteria (example for DEV-002):** the draft cites only approved sources and is produced in under 5 seconds.

---

## 6. Interview preparation

### Common questions with strong answers

**1. What is the difference between a Product Manager and a Program Manager?**
A PM decides what to build and why, based on user needs and business goals. A Program Manager coordinates the delivery across teams: schedule, dependencies, risks and status. The PM owns the product outcome, and the Program Manager owns the execution.

**2. What makes a good user story?**
It follows the *As a / I want / so that* format and is small, valuable and testable. A common check is **INVEST**: Independent, Negotiable, Valuable, Estimable, Small, Testable.

**3. What is the difference between a story, a feature and a task?**
A story is a user need. A feature groups related stories into a capability. A task is a concrete piece of engineering work that implements a story.

**4. How do you write acceptance criteria?**
As specific, testable statements, often in Given/When/Then form: *Given an email about billing, when it is processed, then it is routed to the billing SME with its metadata.*

**5. How do you prioritize a backlog?**
Compare value against effort and risk using a framework such as MoSCoW, RICE (Reach, Impact, Confidence, Effort) or value vs effort. Align with business goals and get stakeholder input.

**6. How do you handle a dependency that is blocking your team?**
Identify it early, talk to the owning team, agree a date, add it to the risk log, and plan around it, for example by working on independent tasks first.

**7. What would you do if a stakeholder keeps adding requirements?**
Acknowledge the request, evaluate its value and cost, show the trade-off against scope and timeline, and either reprioritize or schedule it for a later phase.

**8. How do you estimate work?**
Break it into small tasks, estimate with the team (story points or hours), add buffer for risk, and refine from actual results.

**9. How do you measure the success of a product?**
Tie it to KPIs set up front, such as response time, accuracy and adoption, and review them after launch.

**10. Explain this project in two minutes.**
"I built an agentic workflow where AI agents play the roles of a Product Manager, Program Manager and Development Engineer. An action planner splits a request into role-based steps, a routing agent sends each step to the right specialist, and an evaluation agent checks each output against a required structure and asks for corrections. The result is a consolidated plan with user stories, features and tasks for an Email Router product."

### Questions about the agent workflow (technical interviews)
- *Why use an evaluation agent?* It checks output against criteria and drives a correction loop, which improves reliability.
- *What are the limits of embedding-based routing?* Similarity scores can be close, and ambiguous steps get misrouted, so explicit roles or a validator are more reliable.
- *How do later agents know earlier results?* They don't unless you pass the earlier outputs into their prompt or knowledge.
- *Why temperature 0?* For repeatable, consistent output.

### Tips
- Use concrete numbers and examples from the project.
- Describe your *own* contribution and the problems you fixed, for example misrouting and missing context.
- Be ready to draw the hierarchy: vision, epic, feature, story, task.
- Know when you would involve each role, and be honest where they overlap.

---

## 7. Quick self-test

1. Who writes user stories? *(Product Manager)*
2. Who groups stories into features and tracks the schedule? *(Program Manager)*
3. Who estimates and writes the acceptance criteria for tasks? *(Development Engineer, with the PM for story-level criteria)*
4. Is "Email filtering" a story, a feature or a task? *(A feature)*
5. What does an embedding capture? *(The meaning of text as numbers)*
6. What does the evaluation agent return when the output is wrong? *(A "No" plus the reasons, then correction instructions)*