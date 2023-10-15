from django_cron import CronJobBase, Schedule
from .news_api_client import NewsApiClient


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # Run daily

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'News Update Cron Job'  # A unique code for your cron job

    def do(self):
        api_client = NewsApiClient()
        api_client.request_news()
