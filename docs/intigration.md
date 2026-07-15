# Marketplace Integration

## Objective

Validate the complete AI-ML Marketplace workflow from student profile to company job recommendations.

## Components

- Student Dataset
- Job Dataset
- Matching Algorithm
- Explainability Engine
- Company Portal
- REST APIs

## APIs

GET /api/explain/<student_id>

Returns job recommendations with explanation payload.

GET /api/company/jobs

Returns all company job listings.

GET /api/company/validate/<student_id>

Returns validated and ranked job recommendations.

## Technologies Used

- Python
- Flask
- Pandas
- REST API
- Git
- GitHub

## Outcome

The application successfully validates end-to-end matching and exposes integrated APIs for both students and companies.