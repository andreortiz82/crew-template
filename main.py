from dotenv import load_dotenv
from crewai import Crew, Process
from agents import researcher, writer, character
from tasks import research_task, writing_task, character_task

load_dotenv()

def main():
    custom_crew = Crew(
        agents=[researcher, writer, character],
        tasks=[research_task, writing_task, character_task],
        process=Process.sequential  # This can be adjusted to parallel if needed
    )

    # Define the input for the tasks, in this case, it could be a project brief or specifications
    inputs = {
        'topic': 'Paper Clips',
        'character': 'A warbot named Mr. Zurkon',
        'tone': 'funny, violent, diabolical, obsessed with world domination and the defeat of his enemies, always refers to himself in the third person.',
    }

    # Kick off the crew's task execution
    results = custom_crew.kickoff(inputs=inputs)
    print(results)

if __name__ == '__main__':
    main()
