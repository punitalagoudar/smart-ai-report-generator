# Smart AI Report Generator

A production-ready, AI-powered web application that helps users generate structured academic, technical, and business reports using Large Language Models (LLMs). The project demonstrates end-to-end development of a secure SaaS-style application covering backend logic, authentication, API integration, and cloud deployment.

Live demo: https://smart-ai-report-generator.onrender.com

---

## Table of Contents
- [Features](#features)
- [How it works](#how-it-works)
- [Tech stack](#tech-stack)
- [Requirements](#requirements)
- [Local installation & quick start](#local-installation--quick-start)
- [Configuration & environment variables](#configuration--environment-variables)
- [Running in production](#running-in-production)
- [Data storage & migrations](#data-storage--migrations)
- [Security best practices](#security-best-practices)
- [Planned enhancements](#planned-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features
- User authentication (register / login)
- AI-driven report generation with multiple templates (College, IEEE, Simple)
- Report validation and automated quality scoring
- Versioning for generated reports
- Downloadable finalized reports
- Secure handling of API keys via environment variables
- Production-ready deployment configuration

---

## How it works
1. User selects a report type and provides a topic (and any additional inputs).
2. The backend sends a structured prompt to the configured LLM provider.
3. Generated content is validated and scored for quality.
4. The final report is saved and can be downloaded or versioned for later retrieval.

---

## Tech stack
- Backend: Flask (Python)
- Frontend: HTML, CSS, Jinja2 templates
- Database: SQLite (development); recommended PostgreSQL for production
- AI: OpenRouter / OpenAI-compatible LLMs
- Server: Gunicorn
- Deployment: Render (example)

---

## Requirements
- Python 3.8+
- pip
- (Optional) virtualenv or venv

---

## Local installation & quick start

1. Clone the repository
```bash
git clone https://github.com/punitalagoudar/smart-ai-report-generator.git
cd smart-ai-report-generator
```

2. Create and activate a virtual environment (recommended)
- macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```
- Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set the required environment variables (examples below), then run the app:
```bash
# Example (Windows)
set OPENAI_API_KEY=your_api_key_here
python main.py

# macOS / Linux
export OPENAI_API_KEY=your_api_key_here
python main.py
```

The application should be available at http://127.0.0.1:5000 unless configured otherwise.

---

## Configuration & environment variables

The app uses environment variables for sensitive configuration. Typical variables include:

- OPENAI_API_KEY (or OPENROUTER_API_KEY) — API key for the chosen LLM provider  
- FLASK_ENV — development or production (optional)
- DATABASE_URL — (optional) if using a different database (e.g., PostgreSQL)

If you switch providers (OpenRouter vs OpenAI), update configuration accordingly. Check the code where the LLM client is initialized to confirm the exact variable names expected by your setup.

---

## Running in production

A simple production deployment example using Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 main:app
```

When deploying to Render or another cloud provider, ensure:
- API keys and secrets are set via the provider's secret management
- DEBUG is disabled
- Use a production-grade database (PostgreSQL) instead of SQLite
- Configure HTTPS and logging

---

## Data storage & migrations

- The project uses SQLite by default for simplicity and local development.
- For production, migrate to PostgreSQL or another managed database and update `DATABASE_URL`.
- If you introduce migrations, consider adding Alembic or Flask-Migrate to manage schema changes.

---

## Security best practices
- Never commit API keys or secrets to version control.
- Store API keys in environment variables or a secret manager.
- Run the app behind HTTPS in production.
- Apply appropriate input validation and rate limiting for API endpoints if the app is publicly accessible.

---

## Planned enhancements
- Migrate to PostgreSQL for persistent, scalable storage
- Role-based access control and admin features
- Usage analytics and performance metrics
- Subscription plans and usage limits
- Automated tests and CI pipeline

---

## Contributing
Contributions are welcome. Suggested workflow:
1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Make changes and add tests where appropriate
4. Open a pull request with a clear description of changes

Please keep commits small, well-documented, and follow the repository’s code style.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author
Punit Alagoudar  
Information Science & Engineering

For questions or collaboration, open an issue or contact via your GitHub profile.
