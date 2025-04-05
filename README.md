# 🚀 Enginuity AI – The DevOps Super Assistant

**Enginuity AI** is an intelligent ChatOps + automation platform that enhances engineering efficiency, production reliability, and team well-being.

## 🔥 Key Features

- 💬 ChatOps UI – Control deployments, get logs, and ask anything in natural language
- 🔍 Incident Predictor – ML-powered root cause analysis from logs
- 🩹 SmartFix Atlas – Auto-suggests remediations from incident memory
- 😓 Burnout Detector – Detects engineer fatigue based on dev activity
- 🧪 Secure CI/CD – Prevents risky or non-compliant pushes (optional)

## 🧑‍💻 Live Demo Steps

1. Clone the repo
2. Install requirements  
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Azure OpenAI keys  
   ```bash
   export AZURE_OPENAI_API_KEY=your-key
   export AZURE_OPENAI_API_BASE=https://<your-endpoint>.openai.azure.com/
   export AZURE_OPENAI_API_VERSION=2023-05-15
   export AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
   ```
4. Run the app  
   ```bash
   python app.py
   ```
5. Visit [http://localhost:5000](http://localhost:5000) in your browser

## 📈 Tech Stack

- Python + Flask
- LangChain + Azure OpenAI
- HTML + Tailwind CSS
- Simulated log & incident data

---
Made with ❤️ for Innovate48
