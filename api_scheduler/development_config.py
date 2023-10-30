import logging

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler

check_scheduler = []
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

executors = {
    'default': ThreadPoolExecutor(1),
    'processpool': ProcessPoolExecutor(5)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors,
                                job_defaults=job_defaults, timezone='Asia/ho_chi_minh')
