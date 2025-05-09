# flask-flashy

Custom flash system allowing custom keyword arguments for Flask.

## How it works

Flask's default `flash()` function simply takes two strings and passes them into the session (the message and category, eg `flash('Username Is In Use', 'warning')`), which is then obtained and cleared by `get_flashed_messages()` in jinja.

flask-flashy uses a keyword-based flashing system, allowing you to pass in as many keyword arguments as you'd like, while still keeping the default message and category to align with flask and allow for minimal edits to convert (eg `flash('Username Is In Use. Login Instead?', 'warning', url=url_for('login'), timestamp=datetime.now() )`).

## Installation & Basic Usage

Install via pip:

```bash
pip install flask-flashy
```

After installing, wrap your Flask app with flashy...

```python
from flask import Flask, render_template
from flask_flashy import Flashy, flash

app = Flask(__name__)
flashy = Flashy(app)

@app.route("/")
def index():
  flash('Hello flashy!')
  return render_template('index.html')
```

...or using the [application factory](https://flask.palletsprojects.com/en/stable/patterns/appfactories/) pattern.

```python
from flask import Flask
from flask_flashy import Flashy

flashy = Flashy()

def create_app():
    app = Flask(__name__)
    flashy.init_app(app)
    return app
```

> **_NOTE:_**  Flashy must be initialized in order to create the context processor which allows `get_flashy_messages()` to be used in jinja templates.

## Examples

After initializing the app, simply call for a flash in a route, passing in the message, optionally a second string as a category (will default to 'message' if not provided), and as many custom keyword arguments as you'd like.

```python
@app.route('/')
def index():
  flash('Woah there partner!', 'danger', url='https://example.com/')
  return render_template('index.html')
```

Then get the flashes in the template using jinja:

```html
{% with messages = get_flashy_messages() %}
{% if messages %}
<ul>
{% for message in messages %}
{% if message.url %}
<a href="{{ message.url }}"><li class="{{ message.category }}">{{ message.message }}</li></a>
{% else %}
<li class="{{ message.category }}">{{ message.message }}</li>
{% endif %}
{% endfor %}
</ul>
{% endif %}
{% endwith %}
```

> **_NOTE:_**  Yes, gone are the days of having to specify `with_categories=True`, it passes everything automatically.

And style and use to your hearts content.

Don't like flashy taking over the `flash()` function? Want to use both the flash and flashy systems in the same project (for whatever reason)? Simply import it with a custom name, such as...

```python
from flask-flashy import flash as flashyFlash
```

## TODO

- Category sorting like vanilla flask
- Fun flask-like logo
- ???

## Release History

- 0.2.2 - Hotfix, `get_flashed_messages()` was clearing the list before returning them resulting in an error.
- 0.2.1 - Fixed JSON serialization bug, now stores the flash directly as a dict, and converts into a FlashyMessage once retrieved.
- 0.2.0 - Made `flash()` and `get_flashed_messages()` their own functions rather than methods within `Flashy`, and more verbose docstrings.
- 0.1.0 - Initial release on pypi.