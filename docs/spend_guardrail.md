# Spend Quality Guardrail

## Objective

The purpose of the Spend Quality Guardrail is to prevent users from paying for job applications that have a very low probability of success.

The system analyzes the student's skills, experience, and location before recommending whether the user should spend money on the application.

---

## Features Implemented

### 1. Skill Matching

The system compares:

- Python
- SQL
- Flask
- Machine Learning
- Communication

between the student and job requirements.

---

### 2. Experience Check

If the student's experience satisfies the job requirement,

+50 bonus points are awarded.

---

### 3. Location Matching

If both student and company are in the same location,

+30 bonus points are awarded.

---

### 4. Guardrail Decision

The recommendation is based on the final score.

| Match Score | Recommendation |
|-------------|----------------|
| 450 and above | Safe to Apply |
| 350 – 449 | Apply Carefully |
| Below 350 | Low Fit Warning |

---

## API Added

GET

```
/api/guardrails/spend/<student_id>
```

Example:

```
/api/guardrails/spend/1
```

---

## Technologies Used

- Python
- Flask
- Pandas
- REST API
- CSV Dataset

---

## Outcome

The Spend Quality Guardrail improves the user experience by warning users before they spend money on applications with a poor match score.

This helps users make better decisions and supports a more trustworthy AI-powered job recommendation platform.