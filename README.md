# Climate Challenge - Week 0

## Project Overview
Analysis of historical climate data for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria using NASA POWER data (2015-2026).

## Environment Setup

### Prerequisites
- Python 3.13+
- Git

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bethabreham/climate-challenge-week0.git
   cd climate-challenge-week0
2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

## CI/CD Pipeline
This repository uses GitHub Actions for continuous integration. The workflow (`.github/workflows/ci.yml`) runs on every push to the `main` branch and performs:

1. Checkout code
2. Setup Python 3.13
3. Install dependencies from `requirements.txt`
4. Verify Python version

The workflow passes if all steps complete successfully (green checkmark ✅ in Actions tab).
To run the same checks locally:
   ```bash
    pip install -r requirements.txt
    python --version
