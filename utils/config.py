from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

STANDARD_USER = os.getenv("STANDARD_USER")
LOCKED_USER = os.getenv("LOCKED_USER")
PASSWORD = os.getenv("PASSWORD")

FAULTY_USERNAME = os.getenv("FAULTY_USERNAME")
FAULTY_PASSWORD = os.getenv("FAULTY_PASSWORD")

BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"