"""
Vertex AI initialization is performed in the package's __init__.py
"""

import os

from dotenv import load_dotenv

# Load environment variables (this is redundant if __init__.py is imported first,
# but included for safety when importing config directly)
load_dotenv()

# Vertex AI settings
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")
