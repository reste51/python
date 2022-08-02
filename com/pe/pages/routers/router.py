import logging
import threading

from flask import render_template, Flask
from com.pe.data_pushing.scheduler import run_jobs
from com.pe.util.util import get_logger
from pe.pages.routers.person_router import set_p_route
from pe.pages.routers.vehicle_router import set_v_route

"""
    前端路由文件
"""

app = Flask(__name__, template_folder="../templates", static_folder="../static", static_url_path="/static")
logger = get_logger(__name__, logging.INFO)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pe/dataAccess')
def control():
    """
    数据接入
    :return:
    """
    threading.Thread(target=run_jobs).start()
    return {'code': 0}


# 设置人员路由
set_p_route(app)

# 设置车辆路由
set_v_route(app)

if __name__ == '__main__':
    app.run(host='192.168.31.238', port=9292, debug=True)
