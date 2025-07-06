import sys
import os
import warnings
from pathlib import Path

from software_testing.crew import SoftwareTesting

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the software testing crew on a Python file.
    """
    # Manually specify the file path here
    file_path = "example.py"
    
    # Validate file path
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
        
    if not file_path.endswith('.py'):
        print(f"Error: File '{file_path}' is not a Python file.")
        sys.exit(1)
    
    # Get file name without extension for creating test file name
    target_file_path = Path(file_path)
    target_file_name = target_file_path.name
    
    # Prepare inputs for the crew
    inputs = {
        'target_file': file_path,
        'target_file_name': target_file_name,
    }
    
    try:
        print(f"\n🧪 Starting autonomous testing for: {target_file_name}\n")
        SoftwareTesting().crew().kickoff(inputs=inputs)
        print(f"\n✅ Testing completed successfully. Test report saved as test_report.md\n")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    run()