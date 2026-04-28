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
   ```
pip install -r requirements.txt
python --version
```
## Contribution & Branching Guidelines

### Branch Naming Convention
- `eda-<country>` - Exploratory data analysis for a specific country (e.g., `eda-ethiopia`)
- `compare-countries` - Cross-country comparison analysis
- `dashboard-dev` - Streamlit dashboard development
- `setup-task` - Environment and CI/CD setup

### Workflow
1. Create a new branch from `setup-task` or `main`
2. Make your changes
3. Commit using Conventional Commits format:
   - `feat:` - New feature or analysis
   - `fix:` - Bug fix
   - `docs:` - Documentation update
   - `chore:` - Maintenance tasks
4. Push branch and create a Pull Request
5. Request review and merge after approval

### Adding a New Country Analysis
1. Copy an existing EDA notebook (e.g., `ethiopia_eda.ipynb`)
2. Rename to `<country>_eda.ipynb`
3. Change the CSV path and country name in the notebook
4. Run all cells to generate clean data
5. Commit and push to a new branch: `eda-<country>`

### Adding to the Dashboard
1. Ensure cleaned CSV exists in `data/` folder
2. Update `app.py` if new country needs special handling
3. Test locally: `streamlit run app.py`
4. Push to `dashboard-dev` branch and redeploy on Streamlit Cloud
