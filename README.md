<h1 align="center">
  <img src="https://64.media.tumblr.com/540a3c0b8c78f1ab203734bef1b10785/fe3ccd354f80a33d-5d/s1280x1920/45d0db1ea6f6225615f4b9a2d80042161591e6d0.pnj" alt="News API Logo" width="200">
</h1>

## Live Documentation

You can access live documentation of the application [here](https://newsapi.abhisheksurela.in). Additionally, you can check the live API by visiting this [link](https://newsapi.abhisheksurela.in/api/).

<p align="center">
  <a href="https://github.com/abhisheksurela79" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-abhisheksurela79-blue.svg?logo=github" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/abhisheksurela79" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Abhishek%20Surela-blue.svg?logo=linkedin" alt="LinkedIn">
  </a>
  <a href="https://www.instagram.com/abhi_81718" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-abhi__81718-orange.svg?logo=instagram" alt="Instagram">
  </a>
  <a href="https://www.facebook.com/abhii.abhishekk" target="_blank">
    <img src="https://img.shields.io/badge/Facebook-abhii.abhishekk-blue.svg?logo=facebook" alt="Facebook">
  </a>
  <!-- <a href="https://www.fiverr.com/users/toscanioliviero" target="_blank">
    <img src="https://img.shields.io/badge/Fiverr-toscanioliviero-brightgreen.svg?logo=fiverr" alt="Fiverr">
  </a> -->
</p>

<p align="center">
  NewsAPI is a powerful and versatile tool that provides developers and businesses with real-time access to a vast and constantly updated database of news articles and headlines from around the world. With easy-to-integrate features, it allows users to retrieve the latest news, filter by source, category, or keyword, and stay informed on global events effortlessly. Whether for creating news apps, conducting research, or enhancing content, NewsAPI is your gateway to a wealth of up-to-the-minute information, and the best part is, it's completely free for everyone!
</p>


## Why NewsAPI is Better Than https://newsapi.org

NewsAPI offers several advantages over https://newsapi.org, making it the preferred choice for developers and businesses:

- **Free for Production**: While https://newsapi.org restricts its free developer plan to localhost, NewsAPI allows you to use it in production without limitations. You can access real-time news data without incurring costs.

- **No User Login Required**: Unlike some other APIs, NewsAPI does not require user authentication or login to access its features, ensuring a hassle-free experience for developers.

- **Powerful Features**: NewsAPI provides a range of powerful features, including the ability to filter news by country, category, and keywords. You can customize the number of news articles per page to suit your needs.

- **Diverse Source Options**: NewsAPI offers a diverse range of source options, ensuring that you can access news from various countries and categories.

- **User-Friendly Integration**: Integrating NewsAPI into your projects is straightforward, making it an excellent choice for developers.


## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [API Usage](#api-usage)
- [Parameters](#parameters)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)


## Features

- Real-time access to news articles and headlines.
- Filter news by source, category, or keyword.
- Retrieve news from a wide range of countries.
- Customize the number of news articles per page.
- Easy-to-integrate API for developers.


## API Usage

You can access NewsAPI using a single endpoint: `/api/`. It accepts GET requests with optional parameters. Here's how you can use the API:

### Parameters

- `country_code`: Filter news by country. See the list of supported countries in the [Country Codes](#country-codes) section.
- `category`: Filter news by category. See the list of supported categories in the [Categories](#categories) section.
- `page_size`: Specify the number of news articles per page.
- `page`: Navigate between pages.

### Examples

Here are some example API requests:

```https
GET /api/?country_code=us&category=business&page_size=10&page=1
GET /api/?category=health&page_size=5
GET /api/?country_code=in&category=sport&page_size=15&page=2
```

## Country Codes

You can use the following country codes to filter news by country:

- Argentina (ar)
- Australia (au)
- Belgium (be)
- Brazil (br)
- Canada (ca)
- Egypt (eg)
- France (fr)
- Germany (de)
- India (in)
- Indonesia (id)
- Italy (it)
- Japan (jp)
- Mexico (mx)
- Nigeria (ng)
- Russia (ru)
- Saudi Arabia (sa)
- Spain (es)
- Turkey (tr)
- Ukraine (ua)
- United Arab Emirates (ae)
- United Kingdom (gb)
- United States (us)

## Categories

You can filter news by the following categories:

- Business (business)
- Education (education)
- Entertainment (entertainment)
- Health (health)
- Science & Technology (science_and_technology)
- Sports (sport)
- Travel (travel)
- World (world)


Certainly, here's the continuation of your README.md with information about how to download the repository, get started with your Django project, and the requirements.txt file:


## Getting Started

To get started with NewsAPI, you can follow these steps:

### Downloading the Repository

1. Clone the NewsAPI repository to your local machine using Git:

```bash
git clone https://github.com/abhisheksurela79/NewsAPI.git
```

### Setting Up the Django Project

2. Navigate to the project directory:

```bash
cd NewsAPI
```

3. Create a virtual environment (recommended) to isolate project dependencies:

```bash
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS and Linux:

```bash
source venv/bin/activate
```

5. Install the project dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```

6. Migrate the database and create a superuser for the admin panel:

```bash
python manage.py migrate
python manage.py createsuperuser
```

7. Start the Django development server:

```bash
python manage.py runserver
```

## Contributing

We welcome contributions from the community. If you'd like to contribute to the project, please feel free to do that.

## License

This project is licensed under the [MIT License]().
