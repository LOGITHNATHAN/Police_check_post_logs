# Police_check_post_logs
# 🚨 SecureCheck: A Python-SQL Digital Ledger for Police Post Logs

**Domain:** Law Enforcement & Public Safety  
**Technologies:** Python, SQL (PostgreSQL/MySQL), Streamlit

---

## 📌 Project Overview

**SecureCheck** is a centralized digital system designed to streamline police check post operations. It replaces inefficient manual logging with a secure SQL-based backend and a real-time Python-powered dashboard. The solution supports detailed tracking, automated alerts, and insightful analytics to assist law enforcement officers in decision-making.

---

## 🎯 Problem Statement

Police check posts require a robust logging and tracking system. Manual processes hinder efficiency, delay responses, and reduce accuracy. This project builds a secure, scalable digital ledger to:

- Log vehicle movements
- Track personnel activities
- Automate suspect detection
- Analyze crime patterns
- Enable multi-location check post integration

---

## 🚀 Key Features

- 🔄 **Real-time vehicle and personnel logging**
- 🚔 **SQL-based suspect vehicle identification**
- 📊 **Streamlit dashboard for real-time reports & trends**
- ⚠️ **Automated alerts for flagged vehicles**
- 📈 **Crime and violation trend analysis**
- 🌐 **Centralized multi-location database**

---

## 🧰 Tech Stack

| Component | Technology |
|----------|------------|
| Backend  | Python (Pandas, SQLAlchemy), SQL (PostgreSQL/MySQL) |
| Frontend | Streamlit |
| Database | PostgreSQL / MySQL / SQLite |
| Others   | GitHub, Google Sheets (Dataset) |

---

## 📂 Project Structure

```bash
.
├── data/
│   └── traffic_stops.csv
├── scripts/
│   ├── data_processing.py
│   └── sql_queries.sql
├── dashboard/
│   └── streamlit_app.py
├── README.md
└── requirements.txt

📥 Dataset
Traffic Stops Dataset (Google Sheet)

Dataset Columns:
stop_date, stop_time, country_name

driver_gender, driver_age, driver_race

violation, search_conducted, stop_outcome

stop_duration, drugs_related_stop, and more...
🛠️ Project Phases
🔹 Step 1: Python for Data Processing
Remove missing-value-only columns

Clean NaN values

Normalize driver_age, violation, etc.

🔹 Step 2: SQL Database Design
Define schema for logs, searches, and officers

Use foreign key constraints for relational integrity

🔹 Step 3: Streamlit Dashboard
Visualize vehicle logs, violations, officer activity

Enable SQL-based filters and real-time alerts

Provide trends, summaries, and high-risk flags

🧪 SQL Query Samples
📌 Medium-Level
Top 10 vehicles involved in drug-related stops

Most frequently searched vehicles

Arrest rate by age group, gender, and race

Common violations during nighttime

📌 Complex-Level
Yearly breakdown of stops using WINDOW functions

Join analysis of driver demographics and violations

Time-based heatmaps of stop occurrences

Top 5 violations with highest arrest rates

📄 Full list in scripts/sql_queries.sql

📈 Evaluation Metrics
⚡ Query Execution Time

✅ Data Accuracy & Integrity

🕒 System Uptime

👮 User Engagement (Officer Usage)

🚩 Violation Detection Rate


📊 Sample Dashboard Preview
(Streamlit UI showing traffic stops, violation stats, and demographic filters)
You can customize charts like bar graphs, pie charts, line trends, and more.

📚 Resources & References
📘 Streamlit Docs

🎥 Project Orientation Session

📊 Dataset Explanation

📂 SQL & Dashboard Samples


✅ Deliverables
✅ Cleaned Dataset and Data Processing Scripts

✅ SQL Schema and Query Files

✅ Streamlit Dashboard Application

✅ Project Documentation (README.md)

✅ Links to Reference & Orientation Materials

