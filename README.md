# Favorita AI Inventory System

## Project Overview

This project simulates a real-world inventory optimization system for a grocery retail chain using the Corporación Favorita dataset. The goal was to create a business-focused, AI-powered solution for demand forecasting and inventory replenishment, designed as if deployed inside a supply chain analytics team.

Instead of treating it as a Kaggle competition, the approach here was to build a modular, production-ready pipeline capable of forecasting demand, determining reorder points, setting safety stock levels, and triggering replenishment, all while being interpretable for stakeholders.

To keep the project efficient on local compute, forecasting was scoped to the top 4 high-performing stores and top 4 highest-volume product families, while maintaining scalability to the full dataset.

---

## Tools and Technologies

- Python (Pandas, NumPy, Scikit-learn)
- Prophet, SARIMA, and XGBoost for forecasting
- Matplotlib and Seaborn for data visualization
- SHAP for interpretability
- Streamlit for interactive dashboard
- Git and GitHub for version control

---

## Project Highlights

- **Demand Forecasting** — Built baseline forecasts with Prophet and extended experiments with SARIMA and XGBoost for both weekly and monthly horizons.
- **Business Integration** — Framed the pipeline to align with real supply chain KPIs like service level targets, stockout risk, and cost optimization.
- **Scalability** — Modular design allows expansion from a subset of stores and families to the entire network using cloud or distributed compute.
- **Interpretability** — Integrated SHAP explainability into the Streamlit dashboard to help decision-makers understand forecast drivers.
- **Stakeholder-ready Dashboard** — Interactive app for exploring forecasts, toggling promotion and holiday effects, and visualizing seasonal patterns.

---

## Folder Structure

```text
FAVORITA_AI_INVENTORY_SYSTEM/
├── app/            # Streamlit dashboard
├── data/           # Raw and processed data
├── notebooks/      # EDA, forecasting, and modeling notebooks
├── reports/        # Visualizations, summary reports
├── src/            # Core Python modules for data prep and modeling
├── requirements/   # Python dependencies
├── ROADMAP.md      # Project roadmap and milestones
└── streamlit_app.py # Main entry point for dashboard
```

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/FAVORITA_AI_INVENTORY_SYSTEM.git

# Navigate to the project folder
cd FAVORITA_AI_INVENTORY_SYSTEM

# (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements/requirements.txt

# Explore notebooks for EDA, modeling, and results
jupyter notebook notebooks/

# Launch the Streamlit dashboard
streamlit run streamlit_app.py
```

---

## Future Improvements

- Extend forecasting to all store-family combinations using distributed cloud compute
- Integrate external economic indicators and weather data for richer forecasts
- Add automated alerting for stockouts or demand spikes
- Deploy as a cloud-based application for multi-location access

---

## Contact

Author: Kewal Roshan Ezra  
Email: rezzisroshan@gmail.com  
LinkedIn: [Kewal Roshan Ezra](https://linkedin.com/kewalroshanezra)
