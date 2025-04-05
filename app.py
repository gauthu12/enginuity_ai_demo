
from flask import Flask, request, jsonify, render_template
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

app = Flask(__name__)

llm = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_type="azure",
    temperature=0.2
)

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

SIMULATED_LOGS = {
    "payment-service": "[2025-04-01 12:03:22] ERROR NullPointerException at line 42\n[2025-04-01 12:03:25] WARN Memory usage at 92%\n[2025-04-01 12:04:01] INFO Health check passed",
    "auth-service": "[2025-04-01 13:15:12] INFO Login successful\n[2025-04-01 13:17:03] ERROR TokenExpiredException at AuthManager.java:67\n[2025-04-01 13:18:33] INFO Token refreshed"
}

INCIDENT_HISTORY = [
    {
        "id": 4212,
        "service": "payment-service",
        "summary": "Null ref crash in May",
        "fix": "Patched null check in transaction handler",
        "timestamp": "2024-05-03 10:12:00"
    },
    {
        "id": 4321,
        "service": "auth-service",
        "summary": "Token expiry crash",
        "fix": "Implemented token refresh mechanism",
        "timestamp": "2024-06-10 09:45:00"
    }
]

ENGINEER_ACTIVITY = {
    "ravi": {
        "late_night_commits": 6,
        "alerts_handled": 12,
        "on_call_days": 5,
        "recent_commits": [
            {"timestamp": "2025-04-02T23:45:00", "message": "Fix memory leak"},
            {"timestamp": "2025-04-03T00:30:00", "message": "Patch null reference"},
            {"timestamp": "2025-04-03T01:10:00", "message": "Optimize loop"}
        ]
    },
    "nina": {
        "late_night_commits": 1,
        "alerts_handled": 2,
        "on_call_days": 1,
        "recent_commits": [
            {"timestamp": "2025-04-01T15:20:00", "message": "Update login logic"}
        ]
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = conversation.run(user_input)
    return jsonify({"response": response})

@app.route("/logs/<service>")
def get_logs(service):
    return jsonify({"logs": SIMULATED_LOGS.get(service, "No logs found.")})

@app.route("/incident_predict", methods=["POST"])
def incident_predict():
    service = request.json.get("service")
    if service == "payment-service":
        return jsonify({
            "prediction": "Likely null pointer crash due to missing transaction object",
            "confidence": 0.91
        })
    elif service == "auth-service":
        return jsonify({
            "prediction": "Likely token expiration issue on auth requests",
            "confidence": 0.87
        })
    return jsonify({"prediction": "No issues detected.", "confidence": 0.2})

@app.route("/smartfix", methods=["POST"])
def smartfix():
    service = request.json.get("service")
    for incident in INCIDENT_HISTORY:
        if incident["service"] == service:
            return jsonify({
                "match": True,
                "suggested_fix": incident["fix"],
                "reference_id": incident["id"],
                "timestamp": incident["timestamp"]
            })
    return jsonify({"match": False})

@app.route("/burnout_status/<engineer>")
def burnout_status(engineer):
    data = ENGINEER_ACTIVITY.get(engineer)
    if not data:
        return jsonify({"status": "unknown"})

    if data["late_night_commits"] > 5 or data["alerts_handled"] > 10:
        return jsonify({
            "status": "at risk",
            "suggestion": "Consider rotating on-call or rebalancing workload.",
            "recent_commits": data.get("recent_commits", [])
        })
    return jsonify({"status": "normal", "recent_commits": data.get("recent_commits", [])})

if __name__ == "__main__":
    app.run(debug=True)
