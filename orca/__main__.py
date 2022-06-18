import uvicorn
from . import api

def main():
    uvicorn.run(api.app, host="0.0.0.0", port=5000, log_level="info")