from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
STANDARD_USER = os.getenv("STANDARD_USER")
LOCKED_USER = os.getenv("LOCKED_USER")
PASSWORD = os.getenv("PASSWORD")
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
VALID_USERNAME = os.getenv("STANDARD_USER")
VALID_PASSWORD = os.getenv("PASSWORD")
LOCKED_OUT_USERNAME = os.getenv("LOCKED_USER")
LOCKED_OUT_PASSWORD = os.getenv("PASSWORD")
INVALID_USERNAME = os.getenv("FAULTY_USERNAME")
INVALID_PASSWORD = os.getenv("FAULTY_PASSWORD")

