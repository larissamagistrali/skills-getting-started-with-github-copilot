"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Join us for weekly chess matches and tournaments!",
        "participants": []
    },
    "Robotics Team": {
        "description": "Build and program robots to compete in regional competitions.",
        "participants": []
    },
    "Drama Club": {
        "description": "Perform in school plays and learn about theater production.",
        "participants": []
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in inter-school tournaments.",
        "participants": []
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play friendly matches every week.",
        "participants": []
    },
    "Painting Workshop": {
        "description": "Explore various painting techniques from watercolor to acrylic.",
        "participants": []
    },
    "Photography Club": {
        "description": "Learn photography fundamentals and showcase your work in school exhibitions.",
        "participants": []
    },
    "Science Olympiad": {
        "description": "Prepare for regional and national science competitions across multiple disciplines.",
        "participants": []
    },
    "Debate Team": {
        "description": "Develop critical thinking and public speaking skills through competitive debate.",
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/signup")
def unregister_from_activity(activity_name: str, email: str):
    """Unregister a student from an activity"""
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    activity = activities[activity_name]

    if email not in activity["participants"]:
        raise HTTPException(status_code=404, detail="Participant not found")

    activity["participants"].remove(email)
    return {"message": f"Unregistered {email} from {activity_name}"}
