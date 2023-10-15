from django.db import models

# Create your models here.


categories = (
    ("world", "World"),
    ("sport", "Sports"),
    ("business", "Business"),
    ("science_and_technology", "Science & Technology"),
    ("education", "Education"),
    ("entertainment", "Entertainment"),
    ("health", "Health"),
    ("travel", "Travel")
)

countries = (
    ('ar', 'Argentina'),
    ('au', 'Australia'),
    ('be', 'Belgium'),
    ('br', 'Brazil'),
    ('ca', 'Canada'),
    ('de', 'Germany'),
    ('eg', 'Egypt'),
    ('fr', 'France'),
    ('gb', 'United Kingdom'),
    ('id', 'Indonesia'),
    ('in', 'India'),
    ('it', 'Italy'),
    ('jp', 'Japan'),
    ('mx', 'Mexico'),
    ('ng', 'Nigeria'),
    ('ru', 'Russia'),
    ('sa', 'Saudi Arabia'),
    ('tr', 'Turkey'),
    ('ua', 'Ukraine'),
    ('us', 'United States')
)

languages = (
    ('ar', 'Arabic'),
    ('en', 'English'),
    ('tr', 'Turkish'),
    ('fr', 'French'),
    ('ja', 'Japanese'),
    ('es', 'Spanish'),
    ('ru', 'Russian'),
    ('pt', 'Portuguese'),
    ('de', 'German'),
    ('it', 'Italian')
)


class Article(models.Model):
    country_code = models.CharField(max_length=100, choices=countries, default="0")
    language = models.CharField(max_length=100, choices=languages, default="0")
    category = models.CharField(max_length=50, choices=categories, default="0")
    title = models.CharField(max_length=2100)
    content = models.TextField()
    url_to_image = models.TextField()
    url = models.TextField()
    author = models.CharField(max_length=1000)
    published_on = models.DateField()
    published_time_stamp = models.TimeField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
