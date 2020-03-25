from flask import Flask
from flask import escape, url_for
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'user:%s' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('user_page', name='zhagnsan'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'

if __name__ == '__main__':
    app.run()