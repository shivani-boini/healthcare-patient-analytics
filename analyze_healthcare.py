import pandas as pd
import sqlite3

# ── Load CSV into SQLite ──────────────────────────────────────────────────────
df = pd.read_csv("healthcare_patients.csv")
conn = sqlite3.connect("healthcare.db")
df.to_sql("patients", conn, if_exists="replace", index=False)
print("✅ Data loaded into SQLite — healthcare.db created\n")

# ── Query 1 — Conversion rate by program ─────────────────────────────────────
q1 = """
SELECT
    program,
    COUNT(*) AS total_patients,
    SUM(converted) AS converted_patients,
    ROUND(AVG(converted) * 100, 1) AS conversion_rate_pct,
    ROUND(AVG(engagement_score), 2) AS avg_engagement
FROM patients
GROUP BY program
ORDER BY conversion_rate_pct DESC
"""
df_q1 = pd.read_sql(q1, conn)
print("── Query 1: Conversion Rate by Program ──")
print(df_q1.to_string(index=False))

# ── Query 2 — Drop-off analysis by channel ───────────────────────────────────
q2 = """
SELECT
    enrollment_channel,
    enrollment_status,
    COUNT(*) AS patient_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY enrollment_channel), 1) AS pct_of_channel
FROM patients
GROUP BY enrollment_channel, enrollment_status
ORDER BY enrollment_channel, patient_count DESC
"""
df_q2 = pd.read_sql(q2, conn)
print("\n── Query 2: Drop-off by Enrollment Channel ──")
print(df_q2.to_string(index=False))

# ── Query 3 — Regional performance ───────────────────────────────────────────
q3 = """
SELECT
    region,
    COUNT(*) AS total_patients,
    ROUND(AVG(converted) * 100, 1) AS conversion_rate_pct,
    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction,
    ROUND(AVG(sessions_attended), 1) AS avg_sessions
FROM patients
GROUP BY region
ORDER BY conversion_rate_pct DESC
"""
df_q3 = pd.read_sql(q3, conn)
print("\n── Query 3: Regional Performance ──")
print(df_q3.to_string(index=False))

# ── Query 4 — Insurance type impact on conversion ────────────────────────────
q4 = """
SELECT
    insurance_type,
    COUNT(*) AS total_patients,
    ROUND(AVG(converted) * 100, 1) AS conversion_rate_pct,
    ROUND(AVG(engagement_score), 2) AS avg_engagement,
    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction
FROM patients
GROUP BY insurance_type
ORDER BY conversion_rate_pct DESC
"""
df_q4 = pd.read_sql(q4, conn)
print("\n── Query 4: Insurance Type Impact ──")
print(df_q4.to_string(index=False))

# ── Query 5 — Age group engagement breakdown ─────────────────────────────────
q5 = """
SELECT
    age_group,
    program,
    ROUND(AVG(engagement_score), 2) AS avg_engagement,
    ROUND(AVG(converted) * 100, 1) AS conversion_rate_pct,
    COUNT(*) AS patient_count
FROM patients
GROUP BY age_group, program
ORDER BY age_group, conversion_rate_pct DESC
"""
df_q5 = pd.read_sql(q5, conn)
print("\n── Query 5: Age Group x Program Engagement ──")
print(df_q5.to_string(index=False))

# ── Query 6 — Follow-up impact on conversion ─────────────────────────────────
q6 = """
SELECT
    follow_up_completed,
    ROUND(AVG(converted) * 100, 1) AS conversion_rate_pct,
    ROUND(AVG(engagement_score), 2) AS avg_engagement,
    ROUND(AVG(sessions_attended), 1) AS avg_sessions,
    COUNT(*) AS patient_count
FROM patients
GROUP BY follow_up_completed
ORDER BY follow_up_completed DESC
"""
df_q6 = pd.read_sql(q6, conn)
print("\n── Query 6: Follow-up Impact on Conversion ──")
print(df_q6.to_string(index=False))

# ── Export all query results for Tableau ─────────────────────────────────────
df_q1.to_csv("q1_conversion_by_program.csv", index=False)
df_q2.to_csv("q2_dropoff_by_channel.csv", index=False)
df_q3.to_csv("q3_regional_performance.csv", index=False)
df_q4.to_csv("q4_insurance_impact.csv", index=False)
df_q5.to_csv("q5_age_program_engagement.csv", index=False)
df_q6.to_csv("q6_followup_impact.csv", index=False)

print("\n✅ All 6 query results exported as CSVs — ready for Tableau")
conn.close()