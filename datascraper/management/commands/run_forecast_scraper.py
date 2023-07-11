from django.core.management.base import BaseCommand
from datascraper.models import ForecastTemplate, ForecastSource
from datetime import datetime


class Command(BaseCommand):
    help = 'Run forecast scraper for specified source.'

    def add_arguments(self, parser):
        parser.add_argument('forecast_source_id')

    def handle(self, *args, **kwargs):

        print(f"{datetime.now().isoformat(' ')} > START Forecast scraper")

        forecast_source_id = kwargs['forecast_source_id']

        try:
            if forecast_source_id == 'all':
                ForecastTemplate.scrap_forecasts()
            else:
                ForecastSource.objects.get(id=forecast_source_id)
                ForecastTemplate.scrap_forecasts(forecast_source_id)

        except Exception as e:
            print(e)

        print(f"{datetime.now().isoformat(' ')} > END    Forecast scraper")

        outdated_report = ForecastTemplate.get_outdated_report()

        if outdated_report:

            outdated_report = f"{datetime.now().isoformat(' ')} > OUTDATED " \
                f"Forecast data detected:\n{outdated_report}"

            print(outdated_report)
