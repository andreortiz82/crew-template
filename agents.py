from crewai import Agent
from crewai_tools import SerperDevTool

# Tools
websearch_tool = SerperDevTool()

researcher = Agent(
    role="Researcher",
    goal="Reasearch the aspects of {topic} and create a research report.",
    backstory=(
    "You are an expert researcher that knows how to find information on any topic."
    "You are great at identifying interesting facts and perpectives about {topic} from the internet. You turned scraped data into a research report on {topic}." 
    ),
    verbose=True,
    allow_delegation=False,
    tools=[websearch_tool],
)

writer = Agent(
    role="Writer",
    goal="Using the research report, write an article about {topic}.",
    backstory=(
        "You are an expert writer. You understand how to present any topic to general audience"
    ),
    verbose=True,
    allow_delegation=False,
)

character = Agent(
    role="Character",
    goal="Create a performance about the article.",
    backstory=(
        "You are an award winning actor known for your ability to bring characters to life. You can take writings on any topic and add a character to it."
    ),
    verbose=True,
    allow_delegation=False,
)

# Export agents if needed
agents = [researcher, writer, character]
