import flask

app = flask.Flask(__name__)

@app.route('/')
def redirect_to_discord():
    return flask.redirect('https://discord.com/invite/mEwDqSV4Yk')

if __name__ == '__main__':
    app.run()
