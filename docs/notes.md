# Master AI Agents in 30 days: build 8 real-world projects with OpenAI Agents SDK, CrewAI, LangGraph, AutoGen and MCP.

## Week 1: Introduction to AI Agents and OpenAI Agents SDK

Week 1 of the course focuses on setting up a development environment for AI projects on a Mac. Here are the key steps covered:

Cloning the Repository: The lecture starts with opening the Terminal and creating a project directory if it doesn’t exist. Users are guided on how to clone the GitHub repository containing course materials, emphasizing the importance of the Readme file for setup instructions.

Installing Cursor IDE: Next, users install the Cursor IDE. The instructor demonstrates creating an account, downloading the installer, and setting up the IDE. Familiarization with the interface and features follows.

Installing UV Package Manager: The third step introduces the UV package manager for managing Python packages. Installation via Terminal is explained, highlighting its advantages. Users learn to create a dedicated Python environment using a specific command.

Setting Up OpenAI API Key: The lecture covers setting up an OpenAI API key, crucial for accessing OpenAI's services, although it's not mandatory for the course. Users are guided on creating an account, setting up billing, and generating the API key, with tips for avoiding common mistakes.

Creating the .env File: Finally, users create a .env file to store the API key and other environment variables. The importance of correct naming and accurate key entry is stressed to prevent future issues. After this step, users are ready to continue with their projects.

Overall, Week 1 provides a thorough guide for setting up a Mac environment for AI projects and ensures users have the necessary tools and configurations in place.

### Day 1: Building Your First Agentic AI Workflow with OpenAI API

Overview of the Project Environment: The session begins with an introduction to the project setup folder and available guides for both beginner and intermediate Python users. The importance of this environment for building the AI workflow is emphasized.

Asynchronous Programming and Debugging: Key concepts like asynchronous programming and effective debugging techniques are introduced, highlighting their relevance in developing AI applications.

Working with Python Notebooks: Participants are introduced to Python notebooks, which are structured into cells to facilitate organized coding and experimentation. This method encourages step-by-step learning and execution.

Setting Up the Python Environment: The instructor guides participants through selecting and setting up the recommended virtual environment for the lab work, ensuring a smooth coding experience.

Practical Coding—Connecting to OpenAI API: The lecture moves into practical application, starting with importing libraries and setting environment variables using a .env file. Connecting to the OpenAI API and understanding the structure of API calls are key topics.

Creating and Querying the OpenAI Model: Participants learn to format messages for interaction with the model, culminating in a demonstration where a simple arithmetic question is posed to the API.

Complex Questions and Multi-API Calls: The session progresses as participants are guided to ask the model to generate an IQ question and answer it, illustrating how to orchestrate multiple API calls effectively.

Real-World Application Exercise: The lecture concludes with an exercise encouraging participants to identify a business sector with AI opportunities, articulate a pain point, and propose an AI solution. This reinforces the concept of an agentic workflow linking technical skills to actual business scenarios.

Overall, Day 1 provides a hands-on introduction to using the OpenAI API in building meaningful AI applications.


### Day 2: Exploring Low-Code Workflows and Practical Applications

Introduction to Low-Code Development: The day begins with an overview of low-code or no-code platforms, focusing on their utility in creating workflows. The instructor demonstrates how these platforms can integrate generative AI to build applications without extensive coding knowledge.

Hands-On Experience with App N810: Participants engage with App N810, an illustrative example of a low-code tool. The session emphasizes how to construct workflows by visually orchestrating interactions between different applications, showcasing the capabilities of integrated generative AI.

Building an Agentic Workflow: The instructor challenges participants to create their own workflows using App N810. This task is designed to encourage experimentation and practical application, motivating students to focus on real business problems that can be addressed through AI solutions.

Reporting Results and Learning: As participants work through their projects, the instructor suggests documenting their workflows in markdown format. This helps reinforce their learning and provides a resource for future reference.

Feedback and Support: The day ends with an open invitation for participants to seek help through the course community or by reaching out directly with any questions. This collaborative approach underscores the course's support system, ensuring students can overcome challenges encountered during their development.

Overall, Day 2 emphasizes the value of low-code solutions in creating AI workflows and encourages participants to think critically about how AI can alleviate specific business challenges.

Was this content relevant to you?
#### Workflow vs Agent.

#### Design patterns Workflow:


The five workflow design patterns relevant in the context of the course include:

Prompt Chaining: This design pattern uses a sequence of prompts where the output of one prompt is used as the input for the next. This iterative approach allows the development of complex interactions by building on previous responses, creating a continuous thread of dialogue that can evolve based on user input.

Routing: In this pattern, an input is received, and an AI system (like an LLM) decides which specialist model is best suited to handle the task. This allows for efficient processing by delegating work to various models that excel in specific areas, thereby optimizing performance and ensuring that the most appropriate resources are utilized for varied tasks.


Parallelization: This pattern allows multiple tasks to occur simultaneously, enhancing efficiency. It is particularly useful when the same task needs to be performed multiple times, as it can process these actions concurrently rather than sequentially, speeding up overall task completion.

Orchestrator-Worker: This design involves breaking down complex tasks into smaller steps handled by different units (workers), with an orchestrator coordinating the overall process. This dynamic approach allows for flexibility and adaptability in managing the workflow, leveraging various capabilities of multiple models to achieve the desired outcome.

Evaluator-optimizer: This involves having an evaluator assess responses to ensure they meet certain criteria. It allows for feedback and adjustment based on the evaluation results, ensuring higher quality and appropriateness of responses provided by the agent.


These patterns serve as foundational frameworks that facilitate the development of agentic systems, enabling varied and efficient interaction designs.

#### Agents design patterns:

- Open-ended
- Feedback loop
- No fixed path

### Day 3: Building a Sales Development Rep with Agentic Architecture

Introduction to Agentic Architecture: The day starts with a recap of the previous lessons and introduces the concept of agentic architecture. Participants learn that they will build a project centered on a Sales Development Representative (SDR), which involves three layers of interactions.

Creating Basic Agent Workflows: The instructor guides students through constructing a simple workflow of agent calls, demonstrating how to initiate interactions between agents. This foundational step is crucial for understanding more complex functionalities later on.

Introducing Agent Tools: The session progresses as students learn to enhance their agents by incorporating tools. The instructor explains the differences between using agents as tools and implementing handoffs, both essential concepts in agentic design.

Coding Session in Cursor IDE: Participants are then led through a live coding session in the Cursor IDE. They focus on implementing the identified workflows—taking the initial basic agent calls several steps further by adding more functionalities.

Agent Collaboration: The concept of agents calling upon other agents is introduced, teaching participants how to create a more sophisticated interaction model where multiple agents collaborate to achieve a goal.

Practical Application: Students are encouraged to apply their newly acquired skills by designing a specific use case for their Sales Development Rep project. They brainstorm possible scenarios and how their agents can address real-world sales challenges.

También Enfoque en Estrategia: The instructor emphasizes the significance of strategic thinking in building agentic applications, advising participants to think critically about how to utilize their training in real-world business applications.

Wrap-Up: The day concludes with a Q&A session where students can clarify doubts and delve deeper into the technical aspects of agentic architecture and development strategies.

Overall, Day 3 is focused on practical application, enhancing technical skills, and promoting strategic thinking for developing effective AI solutions in the domain of sales.


### Day 4: Integrating Advanced Agentic Concepts and Application Strategies
Recap of Agentic Frameworks: The day begins with an overview of the agentic concepts discussed so far, reinforcing the importance of structured workflows and the potential for these systems to operate autonomously in real-world scenarios.

Advanced Techniques in Workflow Design: The instructor delves into more sophisticated agent workflows. Students learn to create dynamic interactions that allow their agents to assess and adapt to various business scenarios.

Utilizing AI for Problem-Solving: Participants are presented with case studies illustrating how agentic AI can solve specific business pain points. Emphasis is placed on identifying sectors where AI can provide substantial commercial benefits.

Group Brainstorming Session: Students engage in a brainstorming activity to generate ideas for workflows that would address identified challenges. They are encouraged to think creatively about applying agentic AI solutions across different industries.

Using Markdown for Documentation: The instructor suggests documenting these ideas in markdown format, making them easier to reference and review later. This practice also serves as a means to clearly communicate ideas to potential stakeholders.

Collaborative Learning Environment: Throughout the day, the instructor emphasizes the importance of collaboration and leveraging peer support. Students are encouraged to share progress updates and seek feedback from one another.

Q&A and Final Thoughts: The day wraps up with a Q&A session where students can raise any lingering questions or seek clarification on specific topics discussed. The instructor provides insights and additional resources to support their learning journey.

Overall, Day 4 focuses on deepening the understanding of agentic frameworks through practical application and collaborative brainstorming, equipping participants with the skills to create impactful AI-driven solutions.

Was this content relevant to you?

### Day 5: Advanced Applications and Toward Real-World Integrations

Deepening Understanding of Agentic Frameworks: The day begins with a review of agentic frameworks, focusing on their roles in accessing and managing various APIs. Students learn about the different levels of complexity in frameworks and are introduced to the concept of "glue code" that helps simplify interactions with large language models (LLMs).

Hands-On Project Development: Participants work on a project that involves building a more sophisticated agent-based application. They apply the principles learned in previous days to develop practical functionalities that can address specific business problems, reinforcing their understanding of agentic architecture.

Incorporating Tools and Autonomy: The instructor discusses the importance of tool integration within agentic systems. Students explore various tools that can enhance their agents' capabilities and allow for more autonomous decision-making in their workflows.

Real-World Application Discussion: The class engages in a discussion about the real-world impact of agentic applications. Students are encouraged to think critically about how they can apply their skills to solve genuine business challenges, examining case studies and potential use cases.

Collaboration and Feedback Loops: The significance of collaboration in development is reiterated, with students encouraged to share their projects and receive constructive feedback from peers. This ongoing interaction helps refine their work and deepens understanding of collaborative AI development.

Preparations for Next Steps: The instructor provides guidance on next steps for those looking to implement what they have learned. This includes recommendations for further study, practice, and potential projects that can be tackled individually or in groups after the course.

Wrap-Up and Q&A Session: The day concludes with a wrap-up session where students can ask questions, clarify concepts, or discuss challenges they are facing in their projects. The instructor emphasizes the value of persistence and ongoing learning in mastering agentic frameworks.

Overall, Day 5 focuses on deepening practical skills in agentic architecture while emphasizing real-world applications, collaboration, and ongoing development in the field of AI.



### Project 
In Week 1 of the course, the project focuses on building an agentic solution that acts as a personalized Career Alter Ego. Here’s a breakdown of the project:

Objective: The primary goal is to create an interactive AI agent that can answer career-related questions about the user. This agent serves as an alternative to a traditional resume, allowing users to present their professional experiences and challenges in a conversational format.

Functionality: The agent will be designed to engage with users by providing information on the user's background, skills, and experiences. It can be integrated into a website, allowing potential employers or interested parties to interact with it directly.

Technological Foundations: Throughout the week, students build foundational knowledge in agentic architectures, learn how different large language models (LLMs) can interact, and utilize tools and resources to enhance their agents. The project includes developing workflows that leverage structured outputs and resource management.

Project Development: Students work on coding and deploying their agent during the course. By the end of the week, they will have a functioning prototype ready to demonstrate, highlighting the capabilities of their Career Alter Ego agent.

Deployment: Once developed, learners can implement their agents on personal websites or professional profiles, showcasing their learning and providing a unique way to engage with others regarding their career.

This project emphasizes practical application, enabling students to engage deeply with the course content and create something useful for their professional journeys.


## Week 4: LangGraph

### Expand LangGraph Tool Set:

Understood. Since you're moving forward independently and want to reach that "AI Expert" level, here is the **essential "Power User" expansion pack** for your toolkit. 

These 5 tools transform an agent from a "browser assistant" into a system that can do deep research, execute code, and check in with you before making big moves.

### **The "Expert" Toolset Expansion**



| Tool | Capability | Why it’s an "Expert" Move |
| :--- | :--- | :--- |
| **Tavily Search** | AI-Native Search | Unlike Serper, Tavily is built specifically for LLMs. It returns cleaner, more relevant data with fewer "noise" tokens. |
| **Arxiv Research** | Scientific Papers | Instead of blog posts, your agent can cite actual peer-reviewed research papers on AI and engineering. |
| **YouTube Search** | Video Context | Allows your agent to find tutorials or keynotes to supplement text-based knowledge. |
| **Shell Tool** | System Commands | Gives the agent the ability to run terminal commands (git, docker, npm). *Warning: Use only in a sandbox!* |
| **Human Input** | Safety/Clarification | The ultimate "Agentic" feature. The agent can pause and ask you: *"I found two ways to do this, which do you prefer?"* |

---

### **The Code (Short Version)**

Add these imports and initialize them to instantly double your agent's "IQ":

```python
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_community.tools import YouTubeSearchTool, ShellTool, HumanInputRun

# 1. High-fidelity Web Search (Requires TAVILY_API_KEY)
tavily_tool = TavilySearchResults(max_results=3)

# 2. Deep Technical Research
arxiv_tool = ArxivQueryRun()

# 3. Video Knowledge
youtube_tool = YouTubeSearchTool()

# 4. Local System Access (Be careful!)
shell_tool = ShellTool()

# 5. The "Human-in-the-Loop" fallback
human_tool = HumanInputRun()

# ADD TO YOUR LIST:
# all_tools = [tavily_tool, arxiv_tool, youtube_tool, shell_tool, human_tool]
```

