import time
import schedule
import subprocess
import datetime
import logging
from threading import Event

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scheduler.log'),
        logging.StreamHandler()
    ]
)

def run_streamlit_app():
    """Run Streamlit app for daily insights"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Starting daily insight app at {current_time}")
    
    try:
        # Start Streamlit with explicit config
        process = subprocess.Popen(
            [
                "streamlit", "run", "daily_insight.py",
                "--server.headless=true",
                "--server.port=8501",
                "--browser.gatherUsageStats=false"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        
        # Wait 60 seconds then terminate
        time.sleep(60)
        process.terminate()
        logging.info("Successfully terminated Streamlit app")
        
    except Exception as e:
        logging.error(f"Error running Streamlit app: {str(e)}")

# Schedule daily at 9 AM
schedule.every().day.at("09:00").do(run_streamlit_app)

# Graceful shutdown handler
exit_event = Event()

def shutdown_handler(signum, frame):
    logging.info("Shutting down scheduler...")
    exit_event.set()

# Main loop
logging.info("Scheduler started. Daily runs scheduled at 09:00 UTC")
try:
    while not exit_event.is_set():
        schedule.run_pending()
        time.sleep(60)
except KeyboardInterrupt:
    shutdown_handler(None, None)