from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('indexNew.html')


# 注意：不要使用 app.run()，生产环境由 Gunicorn 启动
# 本地开发调试时，可以在终端运行：
#   flask run --debug
# 或：
#   gunicorn app:app --bind 0.0.0.0:5000
