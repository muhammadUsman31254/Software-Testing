# 🧪 Autonomous Software Testing with Multi-Agent Architecture

Welcome to **SoftwareTesting Crew**, a fully autonomous, multi-agent testing pipeline powered by [CrewAI](https://crewai.com) and LLMs. This system transforms the software testing lifecycle — from test planning to reporting — into a seamless, intelligent process using specialized AI agents.

---

## 🚀 Features

- ✅ End-to-end automated testing pipeline  
- 🤖 Multi-agent collaboration with CrewAI  
- 🧠 LLM-powered reasoning via [GROQ](https://groq.com)  
- 🧪 Pytest-based unit test generation  
- 📊 Code coverage analysis and markdown reporting  
- ⚙️ Configurable and extensible architecture

---

## 🧠 Agent Responsibilities

| Agent        | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `planner`    | Analyzes source code and creates a structured test plan                     |
| `test_writer`| Generates unit tests using `pytest` best practices                          |
| `executor`   | Runs the generated tests and captures output                                |
| `reporter`   | Produces a detailed report including test results and coverage analysis     |

---

## 🗂️ Project Structure

```
Software_Testing/
├── .venv
├── src/software_testing/
│   ├── config/
│   │   ├── agents.yaml          # Agent configurations
│   │   └── tasks.yaml           # Task definitions
│   ├── tools/
│   │   └── pytest_tool.py       # Custom pytest execution tool
│   ├── crew.py                  # Core agent & task orchestration
│   └── main.py                  # Entry point
├── example.py                   # Sample code to test
├── pytest_example.py            # Auto-generated tests
├── test_report.md               # Markdown report output
├── requirements.txt             
├── .env                         
└── .gitignore  
└── uv.lock
└── README.md
└── pyproject.toml                 
```

---

## 🔧 Setup

### ✅ Requirements

- Python `>=3.10,<3.13`
- [CrewAI](https://github.com/joaomdmoura/crewai) with tools
- [GROQ API key](https://console.groq.com)
- pytest and pytest-cov for test execution

### ✅ Installation

**Option 1: Using pip**
```bash
pip install -r requirements.txt
```

**Option 2: Using uv (faster)**
```bash
pip install uv
uv pip install -r requirements.txt
```

**Option 3: Using crewai CLI**
```bash
crewai install
```

### 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
MODEL=groq/meta-llama/llama-4-maverick-17b-128e-instruct
GROQ_API_KEY=your-groq-api-key-here
```

**Get your GROQ API key:**
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up/login to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into your `.env` file

---

## ▶️ How to Run

### Basic Usage

Run the full pipeline on a Python file:

```bash
# Test default example.py file
python src/software_testing/main.py
```

### Command Line Options

```bash
# Show help
python src/software_testing/main.py --help

# Show version
python src/software_testing/main.py --version
```

### Output Files

The pipeline generates:

- `pytest_{filename}.py` – Generated test cases with pytest fixtures
- `test_report.md` – Comprehensive markdown report with coverage analysis

---

## ⚙️ Configuration

**Agent Config** – `config/agents.yaml`  
Define roles, goals, backstories, and tools for each agent.

**Task Config** – `config/tasks.yaml`  
Configure each task's purpose, expected output, and responsible agent.

---

## 🛠 Built-in Tools

- **FileReadTool** – Reads and analyzes source code files
- **FileWriterTool** – Writes generated test files and reports
- **PytestExecutionTool** – Executes pytest with coverage analysis and detailed reporting

## 🎯 Key Features

### Intelligent Test Generation
- Automatically identifies testable components in your code
- Generates comprehensive test cases including edge cases
- Follows pytest best practices and conventions
- Creates proper fixtures and setup/teardown methods

### Coverage Analysis
- Tracks code coverage using pytest-cov
- Generates both terminal and HTML coverage reports
- Identifies untested code paths
- Provides coverage improvement recommendations

### Multi-Agent Workflow
- **Sequential Processing**: Each agent builds on the previous agent's work
- **Specialized Roles**: Each agent has expertise in their specific domain
- **Quality Assurance**: Multiple validation layers ensure high-quality output

---

## 🔧 Advanced Configuration

### Custom Agent Behavior
Edit `config/agents.yaml` to customize agent personalities and goals:

```yaml
planner:
  role: Test Planning Specialist
  goal: Analyze code and create comprehensive test plans
  backstory: Expert software architect with testing focus
```

### Task Customization
Modify `config/tasks.yaml` to adjust task requirements:

```yaml
code_analysis:
  description: Analyze Python source code for testing opportunities
  expected_output: Structured test plan with scenarios
  agent: planner
```

---

## 🙌 Credits

Built with ❤️ using:

- [CrewAI](https://crewai.com) - Multi-agent orchestration framework
- [GROQ](https://groq.com) - Fast LLM inference
- [Pytest](https://pytest.org) - Python testing framework

---

## 📬 Support & Community

- 📚 [CrewAI Documentation](https://docs.crewai.com)
- 🐛 [Report Issues](https://github.com/joaomdmoura/crewai/issues)
- 💬 [Discord Community](https://discord.gg/X4JWnZnxPb)
- 🔧 [GROQ API Docs](https://console.groq.com/docs)

---

## 🔄 Troubleshooting

### Common Issues

**API Key Issues:**
```bash
# Check if API key is set
echo $GROQ_API_KEY
# or check .env file exists
cat .env
```

**Missing Dependencies:**
```bash
# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

**Permission Errors:**
```bash
# Make sure files are readable
chmod +r your_file.py
```

### Debug Mode
Run with verbose output:
```bash
python src/software_testing/main.py --verbose your_file.py
```

---

## 🧠 Smarter QA Starts Here

Transform your testing workflow with AI-powered automation.  
**No manual test writing. No coverage gaps. Just intelligent testing.**

Let your agents analyze, test, and report while you focus on building amazing software.