import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./waouh_v2.db")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me-32-chars")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY", "")
SITE_URL = os.getenv("SITE_URL", "http://localhost:8000")
SITE_NAME = "L'Effet Waouh"
