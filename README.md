# Healthcare Patient Engagement & Program Adoption Analytics

## Overview
An end-to-end analytics project analyzing patient engagement, program adoption, 
and conversion patterns across 5,000 synthetic patient records spanning 5 
healthcare programs in Texas.

Built to mirror real-world healthcare analytics work — from raw data generation 
through SQL analysis to Tableau dashboard delivery.

---

## Business Problem
A healthcare operations team needed visibility into:
- Which programs have the highest patient drop-off rates
- What drives conversion from enrollment to active participation
- How region, insurance type, and follow-up behavior impact outcomes
- Where to focus resources to improve program adoption

---

## Project Structure
healthcare-patient-analytics/
│
├── generate_healthcare_data.py   # Synthetic data generation (Faker + Pandas)
├── analyze_healthcare.py         # SQL analysis queries (SQLite)
├── healthcare_patients.csv       # Raw synthetic dataset (5,000 rows)
│
├── query_results/
│   ├── q1_conversion_by_program.csv
│   ├── q2_dropoff_by_channel.csv
│   ├── q3_regional_performance.csv
│   ├── q4_insurance_impact.csv
│   ├── q5_age_program_engagement.csv
│   └── q6_followup_impact.csv
│
└── README.md
---

## Dataset
- **5,000 synthetic patient records** generated using Python Faker
- **15 columns** including: program, region, enrollment channel, insurance type,
  engagement score, sessions attended, conversion status, satisfaction score
- **Zero nulls** — clean, analysis-ready dataset
- No real patient data used — fully synthetic and HIPAA-safe

---

## SQL Analysis — 6 Key Queries

| Query | Business Question |
|---|---|
| Q1 | Which programs have the highest conversion rates? |
| Q2 | Which enrollment channels have the highest drop-off? |
| Q3 | How does performance vary by region? |
| Q4 | Does insurance type impact engagement and conversion? |
| Q5 | Which age groups engage most with each program? |
| Q6 | Does follow-up completion drive higher conversion? |

---

## Key Findings
- **Cardiac Wellness** and **Diabetes Management** show the highest conversion rates
- Patients enrolled via **Mobile App** convert at a higher rate than phone or in-person
- **Follow-up completion** correlates with a ~30% higher conversion rate
- **Medicare** patients show the highest average engagement scores
- **Central Texas** outperforms other regions on both conversion and satisfaction

---

## Tools Used
- **Python** — Pandas, Faker (data generation + analysis)
- **SQL** — SQLite (analytical queries, aggregations, window functions)
- **Tableau Public** — Interactive dashboard (link below)
- **Git / GitHub** — Version control and project documentation

---

## Tableau Dashboard
🔗 *[Link to be added once published on Tableau Public]*

---

## Author
**Shivani Boini**  
Business & Data Analyst | 4+ years experience  
SQL · Python · Tableau · Power BI · Oracle OIC  
📍 Austin, TX | Open to W2 contract and full-time roles  
🔗 [LinkedIn](https://linkedin.com/in/shivani-boinii)