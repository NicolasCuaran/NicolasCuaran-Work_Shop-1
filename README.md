# Repository Setup Instructions

This repository contains Jupyter Notebooks for analyzing, cleaning, and visualizing candidate data from the `Candidates.csv` file. Follow the steps below to correctly set up your working environment.

## 1. Clone the Repository

Open a terminal and run the following command:

```bash
git clone <repository-url>
```

## 2. Prepare Essential Files

### Data File

Make sure you have the `Candidates.csv` file placed in the project's root folder.

### `.env` File

Create a file named `.env` in the project's root folder with the following format:

```env
PG_USER=username
PG_PASSWORD=password
PG_HOST=host
PG_PORT=port
PG_DATABASE=database_name
```

Replace the placeholders with your specific PostgreSQL database credentials.

## 3. Python Environment Setup

Ensure Python is installed on your system, then set up a virtual environment by executing:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

This installs all necessary dependencies listed in `requirements.txt`.

## 4. Running the Notebooks

Launch Jupyter Notebook by running:

```bash
jupyter notebook
```

Follow the detailed execution order below:

1. **000_TraslateScript.ipynb**: Run this notebook step by step as described within the file. This script is essential for preparing your data for further analysis.

2. **001_EDA_Candidates.ipynb**: Conduct exploratory data analysis to better understand the characteristics and structure of your data.

3. **002_HiredCandidates.ipynb**: Finally, run this notebook to clean your data and create the `HiredCandidates` table in your database, preparing the data for visualization.

## 5. Data Visualization

After creating the database table, you can use visualization tools like **Power BI** to create interactive dashboards and gain clear insights from the processed data.