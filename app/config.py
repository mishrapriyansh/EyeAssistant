from dotenv import load_dotenv
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ENV_PATH = os.path.join(ROOT_DIR, "local.env")
if not load_dotenv(ENV_PATH):
    raise Exception("Failed to load local.env file. Please ensure the file exists and is accessible.")

MAX_RESULTS = int(os.getenv("MAX_RESULT", "10"))
SAFE_SEARCH=os.getenv("SAFESEARCH")
TIMEOUT = int(os.getenv("TIMEOUT", "5"))
raw_domains = os.getenv("TRUSTED_DOMAINS", "")
TRUSTED_DOMAINS = [domain.strip() for domain in raw_domains.split(",") if domain.strip()]
FILE_OUTPUT_DIR = os.getenv("FILE_OUTPUT_DIR", r"C:\Users\mishr\RAG_ASST 01\data")