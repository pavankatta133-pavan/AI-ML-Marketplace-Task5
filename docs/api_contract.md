# API Contract

## Endpoint

GET /api/explain/<student_id>

## Response

Returns ranked job matches with explanation payload.

## Example

{
  "student_id": 1,
  "matches": [
    {
      "company": "Google",
      "role": "ML Engineer",
      "match_score": 445,
      "recommendation": "Highly Recommended",
      "explanation": [
        "Python matched",
        "Experience requirement satisfied"
      ]
    }
  ]
}