1
How to get Django settings variable
django, python, django 1.6

    from django.conf import settings
    foo = getattr(settings, "BAR")

`BAR` being a variable in the project settings.py file. I believe BAR must be uppercase here and in settings.py
