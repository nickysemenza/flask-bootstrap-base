__author__ = "Nicky Semenza"
from flask import Flask, render_template, request, redirect, g
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SERVER_PORT=4000
))


@app.before_request
def remove_trailing_slash():
    if request.path != '/' and request.path.endswith('/'):
        return redirect(request.path[:-1])
@app.route("/")
def homepage():
    return render_template('home.html')
@app.route("/about")
def aboutMe():
    return render_template('about.html')
@app.route("/test")
def test():
    return render_template('test.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port=app.config.get('SERVER_PORT'))



