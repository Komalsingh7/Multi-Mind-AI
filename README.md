# 🧠 Multi Mind AI

**Multi Mind AI** is a multi-agent AI application designed to handle different intelligent tasks using specialized AI agents. Instead of relying on a single model for every task, the system divides responsibilities among dedicated agents for **summarization, research article generation, refinement, validation, and sensitive-data sanitization**.

The application provides an interactive **Streamlit** interface where users can select an AI task, provide input, and receive intelligent results generated through specialized agents.

## 🚀 Live Demo

🔗 **Try the application here:**  
https://multi-mind-ai--komalsingh74200.replit.app/

---

## 🚀 Features

### 📄 Summarize Medical Text

Generate concise and meaningful summaries from lengthy medical or research-oriented text.

### ✍️ Write & Refine Research Articles

Generate research-style content and improve it through a multi-step pipeline:

```text
User Input
    ↓
Writer Agent
    ↓
Refiner Agent
    ↓
Validator Agent
    ↓
Final Article
```

### 🔐 Medical Data Sanitization

Detect and sanitize sensitive information from medical text to help protect personally identifiable information (PII/PHI).

### 🤖 Multi-Agent Architecture

Different agents are responsible for different tasks instead of putting all responsibilities into a single prompt.

### 🧠 LLM Integration

The application integrates Google's Gemini models to power the AI agents.

### 🖥️ Streamlit Interface

A simple and interactive web interface makes it easy to use the different AI capabilities without interacting directly with APIs.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │     Streamlit UI     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Agent Manager     │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌────────────┐   ┌──────────────┐  ┌──────────────┐
       │ Summarizer │   │ Article       │  │ Sanitizer    │
       │   Agent    │   │ Pipeline      │  │    Agent     │
       └────────────┘   └──────┬───────┘  └──────────────┘
                               │
                      ┌────────┴────────┐
                      ▼                 ▼
               ┌────────────┐   ┌────────────┐
               │  Refiner   │   │ Validator  │
               │   Agent    │   │   Agent    │
               └────────────┘   └────────────┘
```

---

## 🤖 Agents

| Agent                | Responsibility                            |
| -------------------- | ----------------------------------------- |
| **SummarizeTool**    | Summarizes long medical/research text     |
| **WriteArticleTool** | Generates research-style articles         |
| **RefinerAgent**     | Improves clarity, structure, and quality  |
| **ValidatorAgent**   | Validates generated content               |
| **SanitizeDataTool** | Detects and removes sensitive information |
| **AgentManager**     | Manages and coordinates different agents  |

---

## 🔄 How It Works

### 1. User selects a task

The user can choose from options such as:

* Summarize Medical Text
* Write & Refine Research Article
* Sanitize Medical Data

### 2. Input is processed

The selected tool sends the user's input to the appropriate AI agent.

### 3. Agent performs the task

Each agent uses a specialized prompt and the configured LLM to perform its responsibility.

### 4. Multi-agent processing

For complex tasks, multiple agents work together.

For example:

```text
Research Topic
      ↓
WriteArticleTool
      ↓
Generated Draft
      ↓
RefinerAgent
      ↓
Improved Draft
      ↓
ValidatorAgent
      ↓
Validated Final Article
```

### 5. Result is displayed

The final output is presented through the Streamlit interface.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### AI / LLM

* Google Gemini API
* Gemini 2.5 Flash

### Framework

* Streamlit

### Architecture

* Multi-Agent AI System
* Modular Agent Architecture

### Other Technologies

* Environment Variables
* API Integration
* Prompt Engineering

---

## 📁 Project Structure

```text
Multi-Mind-AI/
│
├── app.py
│
├── agent_base.py
│
├── agents/
│   ├── summarize_tool.py
│   ├── write_article_tool.py
│   ├── refiner_agent.py
│   ├── validator_agent.py
│   └── sanitize_data_tool.py
│
├── agent_manager.py
│
├── requirements.txt
│
├── .env
│
└── README.md
```

> The exact filenames may differ depending on the current version of the project.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Multi-Mind-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Make sure `.env` is included in `.gitignore`:

```text
.env
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔑 Environment Variables

The project requires a Gemini API key.

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit your API key to GitHub.

---

## 💡 Example Use Cases

### Medical Text Summarization

**Input:**

```text
A lengthy medical research report...
```

**Output:**

```text
A concise summary containing the major findings,
important observations, and key conclusions.
```

### Research Article Generation

```text
Topic
  ↓
AI-generated article
  ↓
Content refinement
  ↓
Quality validation
  ↓
Final article
```

### Medical Data Sanitization

```text
Original:
Patient John Doe, age 42, visited ABC Hospital...

              ↓

Sanitization Agent

              ↓

Sanitized:
Patient [REDACTED], age 42, visited [REDACTED]...
```

---

## 🔐 Privacy & Security

Since the project can process medical or sensitive information, privacy should be considered carefully.

The sanitization component is designed to identify and remove sensitive information before further processing.

However, this project should **not be considered a production-grade medical privacy solution without additional security, compliance, testing, and human review**.

### Recommended Practices

* Never commit API keys.
* Never commit real patient information.
* Use synthetic or anonymized datasets for development.
* Keep `.env` files out of version control.
* Validate sanitized output before using it for sensitive workflows.

---

## 🎯 Why Multi-Agent AI?

A single AI agent can perform multiple tasks, but specialized agents make the architecture more modular and easier to maintain.

Instead of:

```text
User → One Large AI Prompt → Result
```

Multi Mind AI uses:

```text
                 ┌── Summarizer
                 │
User → Manager ──┼── Writer
                 │
                 ├── Refiner
                 │
                 ├── Validator
                 │
                 └── Sanitizer
```

This allows each agent to have:

* A specific responsibility
* Specialized prompts
* Independent logic
* Easier testing
* Better maintainability
* Easier future expansion

---

## 🔮 Future Improvements

Potential improvements include:

* [ ] Add conversation memory
* [ ] Add document/PDF upload
* [ ] Support multiple LLM providers
* [ ] Add agent-to-agent communication
* [ ] Add structured logging
* [ ] Add automated evaluation of generated content
* [ ] Improve PHI/PII detection
* [ ] Add authentication
* [ ] Add persistent chat history
* [ ] Add model selection from the UI
* [ ] Deploy the application to a cloud platform
* [ ] Add unit and integration tests

---

## 📊 Project Highlights

* 🧠 Multi-agent AI architecture
* 🤖 Specialized AI agents for different tasks
* ✍️ Automated research article generation
* 🔄 Iterative article refinement and validation
* 📄 Medical text summarization
* 🔐 Sensitive medical-data sanitization
* ⚡ Gemini-powered AI processing
* 🖥️ Interactive Streamlit interface
* 🧩 Modular and extensible architecture

---

## 👩‍💻 Author

**Komal Singh**

Computer Science & Engineering

### Coding Profiles

* LeetCode: `komal_singh72`
* Codeforces: `komalsingh2004`
* GeeksForGeeks: `komalsingh72`

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!
