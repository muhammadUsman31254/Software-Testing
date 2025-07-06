#src\software_testing\crew.py
import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool
from software_testing.tools.pytest_tool import PytestExecutionTool
from dotenv import load_dotenv
load_dotenv()

@CrewBase
class SoftwareTesting():
    """Software Testing Automation Crew"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self):
        self.file_read_tool = FileReadTool()
        self.file_writer_tool = FileWriterTool()
        self.pytest_tool = PytestExecutionTool()

        # Configure Groq LLM
        self.llm = LLM(
            model="groq/meta-llama/llama-4-maverick-17b-128e-instruct",
            api_key=os.getenv("GROQ_API_KEY"),
        )

    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config['planner'],
            tools=[self.file_read_tool],
            llm=self.llm,
            verbose=True
        )
    
    @agent
    def test_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['test_writer'],
            tools=[self.file_read_tool, self.file_writer_tool],
            llm=self.llm,
            verbose=True
        )

    @agent
    def executor(self) -> Agent:
        return Agent(
            config=self.agents_config['executor'],
            tools=[self.file_read_tool, self.pytest_tool],
            llm=self.llm,
            verbose=True
        )
    
    @agent
    def reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['reporter'],
            tools=[self.file_read_tool, self.file_writer_tool],
            llm=self.llm,
            verbose=True
        )
    
    @task
    def code_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_analysis'],
        )
    
    @task
    def generate_tests_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_tests'],
        )
    
    @task
    def execute_tests_task(self) -> Task:
        return Task(
            config=self.tasks_config['execute_tests'],
        )

    @task
    def generate_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_report'],
            output_file='test_report.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Software Testing crew"""
        
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )