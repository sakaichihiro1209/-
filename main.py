from flask import Flask, render_template
import cookie_service

app = Flask(__name__)

@app.route('/')
def index():
    get_cookie=cookie_service()
    group=get_cookie.get_cookie()
    
    title = 'demo'
    return render_template('index.html', title=title)


@app.route('/each_schedule')
def another_page():
  return render_template('each_schedule.html')

if __name__ == '__main__':
    app.run(debug=True)
