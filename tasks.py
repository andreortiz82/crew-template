from crewai import Task
from agents import researcher, writer, character

research_task = Task(
    description=(
        "Use the internet to research the topic: '{topic}'. Compile interesting facts into a reasearch report."
    ),
    expected_output=("A research report on the topic '{topic}' for the writer to use."),
    agent=researcher,
    tools=researcher.tools,  
    async_execution=False,
)

writing_task = Task(
    description=(
        "Write an article using research report. Article should be at least 2 paragraphs. The article should be based on the facts of the research report."
    ),
    expected_output=("A article based on the research report."),
    agent=writer,
    async_execution=False,
)

character_task = Task(
    description=(
        "You are an actor and your current roll is: {character}."
        "Use the article on '{topic}' and perform it in character. "
        "Make sure that the tone is {tone}."
        "Do not reveal that you are an actor."
        "Summarize the performance in a markdown file."
    ),
    agent=character,
    async_execution=False,
    expected_output=("The performance on '{topic}' in the character of {character}. The performance should be in markdown format."),
    output_file="output.md",
)

tasks = [research_task, writing_task, character_task]
