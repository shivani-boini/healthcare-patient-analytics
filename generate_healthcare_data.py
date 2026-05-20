import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
random.seed(42)
Faker.seed(42)

# ── Config ────────────────────────────────────────────────────────────────────
NUM_PATIENTS = 5000

PROGRAMS = [
    "Diabetes Management",
    "Cardiac Wellness",
    "Mental Health Support",
    "Weight Loss Program",
    "Preventive Care"
]

ENROLLMENT_STATUS = ["Enrolled", "Active", "Dropped", "Completed"]
CHANNELS = ["Online Portal", "Phone", "In-Person", "Mobile App"]
REGIONS = ["North Texas", "South Texas", "Central Texas", "West Texas", "Houston Metro"]
AGE_GROUPS = ["18-30", "31-45", "46-60", "61-75", "75+"]

# ── Generator ─────────────────────────────────────────────────────────────────
def random_date(start_year=2023, end_year=2024):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

records = []

for _ in range(NUM_PATIENTS):
    program = random.choice(PROGRAMS)
    status = random.choices(
        ENROLLMENT_STATUS,
        weights=[0.15, 0.45, 0.25, 0.15]
    )[0]

    enrollment_date = random_date()

    # Conversion = made it to Active or Completed
    converted = 1 if status in ["Active", "Completed"] else 0

    # Engagement score 1-10
    if status == "Active":
        engagement = random.randint(6, 10)
    elif status == "Completed":
        engagement = random.randint(8, 10)
    elif status == "Dropped":
        engagement = random.randint(1, 4)
    else:
        engagement = random.randint(3, 6)

    # Sessions attended
    sessions = random.randint(0, 24) if status != "Dropped" else random.randint(0, 3)

    # Days since enrollment
    days_enrolled = (datetime(2025, 1, 1) - enrollment_date).days

    records.append({
        "patient_id": fake.uuid4()[:8].upper(),
        "age_group": random.choice(AGE_GROUPS),
        "gender": random.choice(["Male", "Female", "Non-binary"]),
        "region": random.choice(REGIONS),
        "program": program,
        "enrollment_channel": random.choice(CHANNELS),
        "enrollment_date": enrollment_date.strftime("%Y-%m-%d"),
        "enrollment_status": status,
        "converted": converted,
        "engagement_score": engagement,
        "sessions_attended": sessions,
        "days_enrolled": days_enrolled,
        "insurance_type": random.choice(["Medicaid", "Medicare", "Private", "Uninsured"]),
        "follow_up_completed": random.choice([0, 1]),
        "satisfaction_score": round(random.uniform(2.5, 5.0), 1) if status != "Dropped" else round(random.uniform(1.0, 3.0), 1)
    })

# ── Save ──────────────────────────────────────────────────────────────────────
df = pd.DataFrame(records)
df.to_csv("healthcare_patients.csv", index=False)

print(f"✅ Dataset generated: {len(df)} rows, {len(df.columns)} columns")
print(f"\nColumn list:\n{list(df.columns)}")
print(f"\nStatus breakdown:\n{df['enrollment_status'].value_counts()}")
print(f"\nConversion rate: {df['converted'].mean():.1%}")