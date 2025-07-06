# src\software_testing\tools\pytest_tool.py
import os
import subprocess
import tempfile
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class PytestExecutionInput(BaseModel):
    """Input schema for PytestExecutionTool."""
    test_file_path: str = Field(..., description="Path to the pytest file to execute.")

class PytestExecutionTool(BaseTool):
    name: str = "Pytest Execution Tool"
    description: str = (
        "Tool to execute pytest test files and return the results. "
        "Provide the path to the pytest file you want to execute."
    )
    args_schema: Type[BaseModel] = PytestExecutionInput
    
    def _run(self, test_file_path: str) -> str:
        """
        Run pytest on the specified test file and return the results.
        
        Args:
            test_file_path: Path to the pytest file to execute
            
        Returns:
            String containing the test execution results
        """
        if not os.path.exists(test_file_path):
            return f"Error: Test file '{test_file_path}' not found."
        
        try:
            # Create a temporary file to capture output
            with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.txt') as temp_file:
                temp_filename = temp_file.name
            
            # Run pytest with coverage and verbose output
            result = subprocess.run(
                ["python", "-m", "pytest", test_file_path, "-v", "--no-header", "--no-summary"],
                capture_output=True,
                text=True
            )
            
            # Prepare the output
            output = "# Pytest Execution Results\n\n"
            output += "## Test Results\n\n"
            output += "```\n"
            output += result.stdout if result.stdout else "No standard output captured."
            output += "\n```\n\n"
            
            if result.stderr:
                output += "## Errors\n\n"
                output += "```\n"
                output += result.stderr
                output += "\n```\n\n"
            
            output += f"## Exit Code: {result.returncode}\n\n"
            output += "0 = All tests passed\n"
            output += "1 = Tests failed\n"
            output += "2 = Test execution interrupted\n"
            output += "3 = Internal error\n"
            output += "4 = Command line usage error\n"
            output += "5 = No tests collected\n"
            
            return output
            
        except Exception as e:
            return f"Error executing pytest: {str(e)}"