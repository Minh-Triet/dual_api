from api_scheduler.collect_db import generate_data
from api_scheduler.development_config import scheduler


def create_apscheduler():
    if scheduler.state == 0:
        scheduler.start()
    jobs = scheduler.get_jobs()
    if not jobs:
        scheduler.add_job(generate_data, 'interval', seconds=30, id='123', replace_existing=True)
