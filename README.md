# A Minimalistic Modern Django Boilerplate

This boilerplate is mainly for educational purposes. It is meant to be cloned as a starter code for future tutorials. But it could also be extended for full use in production or to quickly experiment with new Django ideas.

Fully featured boilerplates by nature are opinionated. This is not the goal here. This boilerplate has the minimal amount of code with minimal opinions. The idea is once you build and understand a basic example, you could swab parts of it with your own preferences, customize more complicated options, or simply build on top of this one. This is meant to replace the default startproject Django code.

## Usage
1. Git clone https://github.com/Jonathan-Adly/django-boilerplate
2. docker compose up -d --build
3. docker compose exec web python manage.py migrate
4. Hack away

Don't forget to remove the "home" function in config/urls.py and use your own!
