# LangGraph - My Learning Journey

This repository contains my code and notes as I learn about Agentic AI using LangGraph from the [Agentic AI using LangGraph](https://youtube.com/playlist?list=PLKnIA16_RmvYsvB8qkUQuJmJNuiCUJFPL) playlist by CampusX.

## What I've Learned

I will be checking off the topics as I complete them. You can find the code for each topic in the respective folders.

- [x] Agentic AI Fundamentals
- [x] LangChain vs. LangGraph
- [x] Sequential Workflows
- [x] Parallel Workflows
- [x] Branching & Nested Workflows
- [x] Iterative Workflows
- [x] Memory (Short-term & Long-term)
- [x] Chatbot Application
---

## Workflows and Projects

This repository showcases a variety of workflows built with LangGraph, demonstrating different patterns for building AI agents and applications.

### Sequential Workflows

These workflows execute tasks in a specific order, with the output of one step feeding into the next.

* **Simple LLM Workflow** (`sequential_workflow/simple_llm_workflow.ipynb`): A basic example of a sequential workflow that takes a question from the user, passes it to a large language model (LLM), and returns the answer.

* **Blog Generator Workflow** (`sequential_workflow/blog_generator_workflow.ipynb`): This workflow automates the process of writing a blog post. It takes a title as input, generates a 3-point outline, and then uses both the title and the outline to create the full blog content.

* **BMI Calculator Workflow** (`sequential_workflow/bmi_calculator_workflow.ipynb`): A non-LLM example of a sequential workflow. This simple application takes a user's height and weight, calculates their BMI, and then categorizes the result (e.g., underweight, normal weight, overweight).

### Parallel Workflow

This workflow executes multiple tasks simultaneously to improve efficiency.

* **UPSC Essay Review Workflow** (`parallel_workflow/upse_essay_review_workflow.ipynb`): This workflow is designed to provide comprehensive feedback on an essay. It evaluates the essay on three different criteria—**language**, **clarity**, and **depth**—in parallel. After all evaluations are complete, it generates a final summary of the feedback and calculates an average score.

### Conditional Workflow

This workflow uses conditional logic to decide which tasks to execute based on the input.

* **Review Response Workflow** (`conditional_workflow/review_response_workflow.ipynb`): This workflow automates customer review responses. It first analyzes the sentiment of a customer's review.
    * If the review is **negative**, the workflow first runs a "diagnosis" to understand the problem and then generates an appropriate, empathetic reply.
    * If the review is **positive**, it skips the diagnosis step and immediately generates a positive response.

### Chatbot Application

This is a simple chatbot built with a Streamlit frontend and a LangGraph backend.

* **`chatbot/chatbot_app.py`**: The user-facing application built with Streamlit that provides a simple chat interface.
* **`chatbot/chatbot_app_backend.py`**: The backend of the chatbot, powered by LangGraph. It manages the conversation state, allowing the chatbot to remember previous messages in the conversation.
* **`chatbot/chatbot_v1.py` and `chatbot/chatbot_v1_2.py`**: Earlier, simpler versions of the chatbot that demonstrate the basic principles of building conversational AI with LangGraph.

---

## How to Run These Projects

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/zeesshhh0/learning_langgraph.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Explore the Jupyter Notebooks:** The workflows are contained in Jupyter Notebooks (`.ipynb`) in their respective folders. You can run them cell by cell to see how they work.
4.  **Run the Chatbot:** To run the chatbot application, navigate to the `chatbot` directory and run the following command:
    ```bash
    streamlit run chatbot_app.py
    ```