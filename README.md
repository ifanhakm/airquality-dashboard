# Air Quality Analysis Dashboard

An interactive dashboard for analyzing and visualizing air quality data from various monitoring stations between 2013 and 2017. This project was developed as part of the Dicoding "Data Analyst Path" submission.

## 📖 About The Project

This project aims to perform a comprehensive Exploratory Data Analysis (EDA) on a historical air quality dataset. The primary goal is to identify trends, patterns, and insights related to various pollutants (like CO, PM2.5, SO2, etc.) across different monitoring stations and over time. The final output is an interactive web-based dashboard built with Streamlit that allows users to explore the data visually.

The key business questions addressed are:

  * How does the concentration of major pollutants vary by year and month?
  * Which monitoring stations consistently record the highest levels of specific pollutants?

## 🛠️ Tech Stack

This project is built using the following technologies and libraries:

  * **Language:** Python
  * **Data Analysis:** Pandas, NumPy
  * **Data Visualization:** Matplotlib, Seaborn
  * **Dashboard:** Streamlit

## ✨ Features

The interactive dashboard provides the following features:

  * **Overall Data Display:** View the cleaned and prepared dataset.
  * **Monthly Pollutant Analysis:** A line chart visualizing the trend of selected pollutants (PM2.5, PM10, SO2, NO2, CO, O3) aggregated monthly.
  * **Top Stations by Pollutant:** A bar chart showing the top 10 stations with the highest average concentration for a selected pollutant.

## 🚀 How to Run

To run this project on your local machine, please follow these steps:

**1. Clone the repository:**

```bash
git clone https://github.com/ifanhakm/your-repository-name.git
cd your-repository-name
```

**2. Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**3. Install the required libraries:**

```bash
pip install -r requirements.txt
```

**4. Run the Streamlit dashboard:**

```bash
streamlit run dashboard_airQuality.py
```

Open your browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).

## 📁 File Structure

```
├── dashboard_airQuality.py         # Main script for the Streamlit dashboard
├── Proyek_Analisis_Data_AirQuality_IfanHakim.ipynb   # Jupyter Notebook for the full EDA process
├── data/                             # Directory containing the dataset
│   └── PRSA_Data_Combined.csv
├── requirements.txt                # List of required Python libraries
└── README.md                       # This file
```
