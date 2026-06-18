# AI Incident Responder (LogShield AI) 🛡️🤖

A lightweight, local Cybersecurity Automated Incident Response Agent inspired by enterprise Security Copilot architectures. This project bridges the gap between cloud security theory and practical engineering by ingesting raw, unstructured server log files, parsing data points via Pandas, and leveraging the Gemini 2.5-Flash model to detect, isolate, and formulate mitigation strategies for security threats in real-time.

---

## 💡 The Inspiration: Microsoft Security Copilot Context

In modern enterprise environments, security operations centers (SOCs) are overwhelmed by millions of raw log entries daily. **Microsoft Security Copilot** revolutionized this space by introducing generative AI orchestrations over traditional Security Information and Event Management (SIEM) data. 

### The Core Concept:
Instead of a human analyst manually filtering thousands of rows of timestamps and IP addresses during an active breach, an AI orchestrator acts as a **Force Multiplier**. It:
1. Instantly synthesizes raw, complex datasets.
2. Identifies malicious signatures (like brute-force vectors or credential stuffing).
3. Drafts structured executive summaries and defensive actions immediately, cutting down Mean Time to Resolution (MTTR) from hours to seconds.

**This project implements that exact pipeline locally on a micro-scale.**

---

## ⚙️ Core Architecture & How It Works

This agent operates via a classic data-to-intelligence pipeline divided into four distinct phases:

```text
[ Raw CSV Logs ] ──> [ Pandas Data Parsing ] ──> [ Low-Temperature Gemini Evaluation ] ──> [ Actionable Incident Report ]
1. Data Ingestion & Transformation (Pandas)
Raw server logs are inherently unstructured for an LLM. The agent utilizes pandas to systematically read the database logs (server_logs.csv), isolating target parameters like timestamps, HTTP status codes, user IDs, and source IPs, before sanitizing and passing them downstream as a clean, structured string block.

2. Zero-Trust Environment Management (python-dotenv)
To mirror industry-standard production guardrails, the application utilizes a strict zero-trust credential model. Crucial access tokens (GEMINI_API_KEY) are isolated entirely within an encrypted local environment runtime (.env), completely separated from the open-source logic layer to eliminate token leakage vulnerabilities.

3. Hyper-Focused AI Orchestration (Gemini 2.5-Flash)
The sanitized logs are passed to the gemini-2.5-flash model alongside strict context-routing configurations:

System Instructions: The model is locked into a rigid Cybersecurity Incident Response Engineer persona, forcing it to analyze data through a deterministic, adversarial lens rather than acting as a conversational chatbot.

Deterministic Temperature (0.2): The model's creativity parameter is heavily dampened. Lowering the temperature to 0.2 forces strict factual adherence to the log data provided, completely mitigating the risk of AI hallucinations or false threat reporting.

4. Output Generation
The agent evaluates the delta between log entries. For instance, detecting multiple failed login attempts on restricted accounts (like root) within highly compressed intervals (e.g., a 9-second window) flags an active automated brute-force vector. It outputs a comprehensive cryptographic risk assessment detailing the attacker's footprint, targeted vectors, and step-by-step firewall mitigation protocols.

🛠️ Tech Stack & Dependencies
Language: Python 3.12+

Data Core: Pandas (Dataframe parsing and serialization)

AI Core: Google GenAI SDK (gemini-2.5-flash)

Environment Security: Python-Dotenv