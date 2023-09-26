"""Flask App Creator"""

from App import create_app

""" Run Flask API."""
app = create_app()

if __name__ == "__main__":
    app.run()
