from news.models import Article
from datetime import datetime, timedelta
from django.utils import timezone
import requests
import time
import random


class NewsApiClient:
    def __init__(self):
        self.categories = [
            "world",
            "sport",
            "business",
            "science_and_technology",
            "education",
            "entertainment",
            "health",
            "travel"
        ]
        self.countries = [
            ('us', 'en'),
            ('gb', 'en'),
            ('ng', 'en'),
            ('eg', 'ar'),
            ('sa', 'ar'),
            ('ae', 'ar'),
            ('ca', 'en'),
            ('mx', 'es'),
            ('it', 'it'),
            ('de', 'de'),
            ('ar', 'es'),
            ('es', 'es'),
            ('jp', 'ja'),
            ('au', 'en'),
            ('fr', 'fr'),
            ('be', 'fr'),
            ('tr', 'tr',),
            ('ua', 'ru'),
            ('ru', 'ru'),
            ('br', 'pt'),
            ('id', 'en'),
            ('in', 'en')
        ]
        self.sort = "sort"
        self.page = 1
        self.data = []

    def build_url(self, category, language, country, page):
        return f"https://newsi-app.com/api/local?category={category}&language={language}&sort={self.sort}&country={country}&page={page}"

    def request_news(self):
        try:
            for country_code, language in self.countries:
                for category in self.categories:
                    self.page = 1
                    while True:
                        url = self.build_url(category, language, country_code, self.page)
                        response = requests.get(url)

                        if response.status_code == 200:
                            news_data = response.json()

                            if not news_data:
                                break  # No more data for this category and country

                            for news in news_data:
                                if news["hasBody"]:
                                    date_object = datetime.strptime(news["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
                                    # Extract the date component
                                    published_on = date_object.date()

                                    # Create a new article object
                                    new_article = Article(
                                        category=category,
                                        country_code=country_code,
                                        language=language,
                                        author=news["sourceName"],
                                        title=news["title"],
                                        content=news["body"],
                                        url_to_image=news["image"],
                                        url=news["link"],
                                        published_on=published_on,
                                        published_time_stamp=datetime.utcfromtimestamp(
                                            news["publishedTimestamp"]).replace(
                                            tzinfo=timezone.utc)
                                    )

                                    # Save the new article object to the database
                                    new_article.save()

                            self.page += 1
                            # time.sleep(random.randint(6, 15))  # Add some delay between requests to avoid rate
                            # limiting
                        else:
                            print(f"Failed to retrieve data from page {self.page} for {category} in {country_code}")

            print("done fetching news")

        except Exception as e:
            print(e)

        finally:
            # Deleting all old news articles that were not created today to free up space

            today_date = datetime.now()
            # Calculate yesterday's date by subtracting one day
            yesterday_date = today_date - timedelta(days=1)
            yesterday_articles = Article.objects.filter(created_on=yesterday_date)

            if not yesterday_articles.exists():
                # No articles were published yesterday
                pass
            else:
                articles_not_today = Article.objects.exclude(created_on=today_date)
                articles_not_today.delete()


api_client = NewsApiClient()
api_client.request_news()
