import json
import os

PROFILE_PATH = "data/user_profile.json"

DEFAULT_PROFILE = {
    "skills": [],
    "projects": [],
    "experience": []
}

def load_profile():
    if not os.path.exists(PROFILE_PATH):
        save_profile(DEFAULT_PROFILE)
        return DEFAULT_PROFILE

    try:
        with open(PROFILE_PATH, "r") as f:
            return json.load(f)
    except:
        # If file is empty or broken — reset it
        save_profile(DEFAULT_PROFILE)
        return DEFAULT_PROFILE


def save_profile(profile):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=2)
