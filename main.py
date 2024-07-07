from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "data": [
            {
                "summary": "Solution 2 Brief Summary",
                "techStack": "Tech Stack B",
                "param": [
                    "Medium",
                    "High",
                    "High"
                ],
                "totalScore": 12,
                "additionalNotes": {
                    "param": [
                        "Scored High because...",
                        "Scored Medium because..."
                    ],
                    "totalScore": "Total score is calculated as 2 (Medium) + 5 (High) + 5 (High) = 12",
                    "githubLinks": [
                        "https://github.com/example3",
                        "https://github.com/example4"
                    ]
                }
            }
        ]
    }

