# 📦 PatentSage

---

## 🧠 Description

**PatentSage** is an open-source AI-powered RAG (Retrieval-Augmented Generation) application for advanced patent analysis, trend forecasting, and innovation prediction. It is designed for researchers, analysts, and R&D teams who want to:
- Analyze global patent trends in emerging technologies (e.g., thermonuclear fusion)
- Retrieve, explore, and forecast innovation using LLM agents and OpenSearch
- Automate patent data ingestion, semantic search, and trend analysis

---

## ⚙️ Tech Stack

| Technology         | Description                        |
|-------------------|------------------------------------|
| Python 3.10+      | Core application & scripts          |
| OpenSearch        | Vector & keyword search backend     |
| CrewAI            | Multi-agent orchestration           |
| LangChain         | LLM orchestration & tools           |
| Ollama            | Local LLM/embedding inference       |
| Docker Compose    | Service orchestration               |
| SerpAPI           | Patent data collection              |

---

## 🚀 Features

- 🔍 Hybrid, semantic, and keyword patent search
- 🤖 Multi-agent patent analysis & forecasting (CrewAI)
- 📈 Trend and innovation prediction for R&D
- 🗃️ Automated data ingestion from SerpAPI
- 🐳 Easy local deployment with Docker Compose
- 🛠️ Modular, extensible Python codebase

---

## 🛠️ Prerequisites

- Python 3.10+
- Docker & Docker Compose
- [Ollama](https://ollama.com/) (for local LLM/embedding)
- [SerpAPI](https://serpapi.com/) API key (for patent data collection)
- (Optional) OpenSearch Dashboards for visualization

---

## 💻 Running Locally

```bash
# 1. Clone the repository
$ git clone https://github.com/kyash99252/PatentSage.git
$ cd PatentSage

# 2. Set up environment variables
$ cp .env.example .env
# Edit .env and add your SERP_API_KEY

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Start OpenSearch & Dashboards (in background)
$ docker-compose up -d

# 5. (Optional) Start Ollama for LLM/embeddings
$ ollama serve
$ ollama pull llama3  # or another supported model

# 6. Ingest patent data (after collecting with SerpAPI)
$ python ingestion.py

# 7. Run the main CLI app
$ python agentic_rag.py
```

> **Tip:** OpenSearch must be running on port 9200. Ollama must be running on port 11434.

---

## 🧪 Testing Instructions

- Manual testing via CLI: Run `python agentic_rag.py` and follow the menu.

---

## 🐳 Docker Support

- `docker-compose up -d` launches OpenSearch and Dashboards
- Data persists in the `opensearch-data` Docker volume
- See `docker-compose.yml` for details

---

## 📁 Project Structure

```text
.
├── agentic_rag.py            # Main CLI app (menu-driven)
├── ingestion.py              # Data ingestion to OpenSearch
├── embedding.py              # Embedding utilities (Ollama)
├── opensearch_client.py      # OpenSearch client & index setup
├── patent_crew.py            # CrewAI multi-agent logic
├── patent_search_tools.py    # Search utilities (keyword, semantic, hybrid)
├── information_collector.py  # SerpAPI data collection
├── helper.py                 # Helper functions (SerpAPI, etc.)
├── requirements.txt          # Python dependencies
├── docker-compose.yml        # OpenSearch & Dashboards
├── files/                    # Raw/collected data
├── results/                  # Processed/ingested data
└── README.md                 # Project documentation
```

| Folder/File         | Purpose                        |
|---------------------|--------------------------------|
| `agentic_rag.py`    | Main CLI app                   |
| `ingestion.py`      | Data ingestion to OpenSearch    |
| `embedding.py`      | Embedding utilities             |
| `patent_crew.py`    | CrewAI agent logic              |
| `patent_search_tools.py` | Search tools                |
| `information_collector.py` | Data collection           |
| `helper.py`         | Helper functions                |
| `files/`            | Raw data                        |
| `results/`          | Processed data                  |

---

## 🔐 Environment Variables

| Variable         | Description                                 |
|------------------|---------------------------------------------|
| `SERP_API_KEY`   | SerpAPI key for patent data collection      |
| (others as needed) | (Add more as your project grows)          |

> Create a `.env` file based on `.env.example` and set your keys.

---

## 🙌 Acknowledgments / Inspirations

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com/)
- [OpenSearch](https://opensearch.org/)
- [SerpAPI](https://serpapi.com/)

<details>
  <summary>Advanced Setup / API Docs</summary>

  - See `patent_crew.py` for CrewAI agent/task customization
  - See `patent_search_tools.py` for search logic
  - See `ingestion.py` for data pipeline
  - For advanced OpenSearch config, edit `opensearch_client.py`

</details>