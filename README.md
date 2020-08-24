[![rodrizapico](https://circleci.com/gh/rodrizapico/django-exercise.svg?style=svg)](https://circleci.com/gh/rodrizapico/django-exercise)

# Apollo Back-End Engineering Challenge

This challenge is designed to evaluate three things:
 - How well you know Python
 - How effectively you can work with the Django framework
 - How well you understand different data serialization formats, which is important for working with the diverse APIs Apollo integrates with
 
## Setting Up

Install Python 3.7 or later if it is not already installed. Then, use `pip` to install `django`. You should then be able to run the project from the `exercise` directory by running `python manage.py runserver`. 

To verify that the server is running correctly, visit `http:127.0.0.1:8000` in your browser.

## Challenge Guidelines

This Django project currently renders a very simple HTML page at the root path. Your task is to add a file input to this page and modify the view so that, when a file is submitted, convert it to JSON and return that to the user.

To test your solution, you can run `python manage.py test`. This will execute two tests, which attempt to submit a file and check the response.

A good solution will not only pass the tests, but also work on any user-submitted XML file.

### JSON Conversion

For the purposes of this exercise, you may ignore any XML attributes. We are only interested in converting the XML node tags and any text values into JSON.

Leaf nodes should be converted into a JSON object with the node tag as the key and the node's text value as the value. For example, `<Foo>Bar</Foo>` should be converted to `{"Foo": "Bar"}`.

Non-leaf nodes should be converted into a JSON object with the node name as the key and an array of the node's children as the value. For example:
```
<Foo>
    <Bar>Baz</Bar>
</Foo>
```
should be converted to
```javascript
{
    "Foo": [
        {"Bar": "Baz"}
    ]
}
```

The tests provide additional examples of more complex conversions.

## Additions / Modifications based on given proyect

I've added a `Dockerfile` & `docker-compose.yml` if you prefer running the application in a container.

You should also set the corresponding env variables (or if using the provided docker-compose, add a `.env` file) according to the provided `.env.sample`. I've made these changes since some stuff should not be public, such as Django's secret key, and others should be easily configurable based on the environment, such as DEBUG mode.

I also edited the `addresses.xml` test file since it didn't match what the corresponding test was expecting, and added some additional tests.

Finally, I implemented CI using CircleCI (as seen by the badge on top of this README), and made a basic deploy on heroku, which can be located here: [Django Exercise Sample](https://django-exercise-sample.herokuapp.com/).