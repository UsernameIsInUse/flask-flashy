# flask-flashy

Custom flash system allowing custom keyword arguments for Flask.

## How it works

Flask's default `flash()` method simply takes two strings and passes them into the session (the message and category, eg `flash('Username Is In Use', 'warning')`), which is then obtained and cleared by `get_flashed_messages()` in jinja.

flask-flashy has a class-based flashing system, allowing you to pass in as many keyword arguments as you'd like, while still keeping the default message and category to align with flask and allow for minimal edits to convert (eg `flash('Username Is In Use. Login Instead?', 'warning', url=url_for('login'), timestamp=datetime.now() )`).

## Installation & Basic Usage

Install via pip:

```bash
pip install flask-flashy
```

After installing, wrap your Flask app with a `Flashy(app)`, or call `Flashy.init_app(app)`

```python
from flask import Flask
from flask_flashy import Flashy

app = Flask(__name__)
flashy = Flashy(app)
```

or to initialize later or use with blueprints:

```python
from flask import Flask
from flask_flashy import Flashy

app = Flask(__name__)
flashy = Flashy()
flashy.init_app(app)
```

## Examples

After initializing the app, simply call for a flash in a route, passing in the message, optionally a second string as a category (will default to 'message' if not provided), and as many custom keyword arguments as you'd like.

```python
@app.route('/')
def index():
  flashy.flash('Woah there partner!', 'danger', url='https://example.com/')
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

And style and use to your hearts content.

## TODO

- Category sorting like vanilla flask
- Fun flask-like logo
- ???

## Release History

- 0.1.0 - Initial release on pypi.