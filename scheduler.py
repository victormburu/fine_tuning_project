import time
import schedule
import subprocess
import datetime
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('numerology.log'),
        logging.StreamHandler()
    ]
)

def generate_insights():
    try:
        logging.info("Generating daily insights...")
        subprocess.run([sys.executable, "daily_insight.py"], check=True)
        logging.info("Insights generated successfully")
    except Exception as e:
        logging.error(f"Error generating insights: {str(e)}")

if __name__ == "__main__":
    # Immediate run for GitHub Actions
    generate_insights()
    
    # Local scheduling logic
    if "--local" in sys.argv:
        schedule.every().day.at("09:00").do(generate_insights)
        logging.info("Scheduler started. Next run at 09:00")
        while True:
            schedule.run_pending()
            time.sleep(60)