# Django Blog

## Overview

A blog web application built with Django and Django Rest Framework, featuring user authentication, blog post management, and a RESTful API.

## Features

- User Authentication
- Blog Posts Management
- REST API Integration

## Getting Started
Here I intregrated both my backend knowledge in django and drf. I mostly followed "Django for Beginners: Build websites with Python and Django" Book by William S. Vincent for django part. I also followed "Django for APIs" for REST API. This is from same author.
### Prerequisites

Make sure you have Python, Django, and Django Rest Framework installed.

```bash
git clone https://github.com/carbon-ahs/django_blog.git
cd django_blog
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver