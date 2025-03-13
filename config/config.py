"""Configuration settings for the AFIP automation."""
import os
from dotenv import load_dotenv
load_dotenv()

CREDENTIALS = {
    "cuil": os.getenv("AFIP_CUIL", ""),
    "password": os.getenv("AFIP_PASSWORD", "")
}