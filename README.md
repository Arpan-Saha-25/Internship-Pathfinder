# Internship Pathfinder

A multi-agent AI system that discovers, evaluates, ranks, and recommends internships tailored to a user’s resume and preferences.

## 🚀 Overview

Internship Pathfinder automates the internship search workflow using three collaborating agents:

* **Discovery Agent** – Finds internship listings.
* **Evaluation Agent** – Extracts skills, matches resumes, and ranks opportunities.
* **Mentor Agent** – Orchestrates the pipeline, learns preferences, and presents the final recommendations.

The system uses custom tools, session memory, context engineering, and optional A2A server support.

---

## 🧠 Features

* Multi-agent architecture
* Resume skill extraction and job–resume matching
* Smart internship discovery
* Ranking and scoring system
* User preference memory
* Tool-powered AI pipeline
* Optional A2A server for interoperable agent communication
* Deployment-ready configuration

---

## 📁 Project Structure

```
discovery_agent/
   agent.py
evaluation_agent/
   agent.py
mentor_agent/
   a2a_server.py
   agent.py
tools/
   internship_search.py
   resume_matcher.py
   skill_extractor.py
.agent_engine_config.json
requirements.txt
README.md
```

---

## 🔄 System Workflow

1. **User uploads resume**
2. Mentor Agent extracts context and calls Discovery Agent
3. Discovery Agent gathers internships
4. Evaluation Agent scores and ranks listings
5. Mentor Agent filters using memory + preferences
6. User receives final recommendations + reasoning

---

## 🧩 Agents

### **Discovery Agent**

* Searches internship sources
* Normalizes job structures
* Returns raw listings for evaluation

### **Evaluation Agent**

* Extracts skills from the resume
* Matches skills vs job descriptions
* Scores and ranks opportunities
* Outputs top-N relevant roles

### **Mentor Agent**

* Orchestrates the workflow
* Applies user preferences
* Stores memory of interests & applied roles
* Provides actionable insights & suggestions

---

## 🛠️ Tools

### **internship_search.py**

Fetches internship information using search/APIs.

### **skill_extractor.py**

Extracts standardized skills from resume text.

### **resume_matcher.py**

Matches resume skills to job requirements with scoring.

---

## ⚙️ Setup

### Install Requirements

```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Option 1: Run Mentor Agent directly

```
python mentor_agent/agent.py
```

### Option 2: Launch A2A Server

```
python mentor_agent/a2a_server.py
```

---

## 📐 Architecture Diagram

```
User → Mentor Agent → Discovery Agent
                       ↓
                Internship List
                       ↓
               Evaluation Agent
                       ↓
             Ranked Opportunities
                       ↓
                 Mentor Agent
                       ↓
               Final Recommendations
```

---

## 📜 Configuration

The file `.agent_engine_config.json` includes:

* agent definitions
* tool registration
* session memory configuration
* deployment parameters

---

## 💬 Example Output

* Top 5 internships tailored to your resume
* Match score for each role
* Missing skill analysis
* Why the system recommends each position

---

## 🌟 Future Enhancements

* Real-time internship APIs
* Multi-source scraping
* Application tracking system
* Email/WhatsApp notification integration

---

## 📄 License

MIT License
