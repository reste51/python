import json
import logging
import os
import uuid
import requests

from flask import render_template, request

from com.pe.util.util import get_logger

logger = get_logger(__name__, logging.INFO)
root_path = 'cases/person'

# 资源名映射的 资源id
resource_data = {'netbar': '8ac6664f825c3d7301825c46b03f0000',
                 'hotel': 'ff80808182580aa20182581000e10004',
                 'roadway': 'ff80808182580aa20182581c94de000f'}
app_id = '111659441725828'
server_url = f'http://10.68.124.63:9020/subscribe/singleId?appId={app_id}'


def set_p_route(app):
    """
    设置人员路由
    :param app:
    :return:
    """

    @app.route('/pe/p_trails')
    def p_trails():
        """
        精准人员轨迹布控请求
        :return:
        """
        return render_template(f'{root_path}/p_trails.html')

    @app.route('/pe/p_trails2')
    def p_trails2():
        date1 = request.args.get('date1')
        date2 = request.args.get('date2')
        zjhm = request.args.get('zjhm')

        # 选择的资源信息
        netbar = request.args.get('res_netbar')
        hotel = request.args.get('res_hotel')
        roadway = request.args.get('res_roadway')

        data = get_subscribe_data()
        # 设置布控信息
        data['tasks'][0]['rules'][0]['dxbh'] = zjhm
        # 设置资源信息
        tmp_res = []
        if netbar is not None:
            tmp_res.append(resource_data['netbar'])
        if hotel is not None:
            tmp_res.append(resource_data['hotel'])
        if roadway is not None:
            tmp_res.append(resource_data['roadway'])
        data['tasks'][0]['bksjlx'] = tmp_res

        headers = {"content-type": "application/json"}
        json_params = json.dumps(data, indent=4)
        resp = requests.post(server_url, data=json_params, headers=headers).json()

        logger.info(f'传递的参数{json_params}, 响应的数据:{resp}')
        return resp

    @app.route('/pe/p_cd')
    def p_cd():
        """
        精准人员离开成都布控请求
        :return:
        """
        return render_template(f'{root_path}/p_cd.html')

    @app.route('/pe/p_cd2')
    def p_cd2():
        zjhm = request.args.get('zjhm')

        logger.info(zjhm)
        return {'code': 0}

    @app.route('/pe/p_crowd')
    def p_crowd():
        """
        重点人群布控请求
        :return:
        """
        return render_template(f'{root_path}/p_crowd.html')

    @app.route('/pe/p_crowd2')
    def p_crowd2():
        crowd = request.args.get('crowd')
        rule = request.args.get('rule')

        res_netbar = request.args.get('res_netbar')
        res_hotel = request.args.get('res_hotel')
        res_roadway = request.args.get('res_roadway')

        logger.info(f'params: crowd={crowd},rule = {rule}')
        return {'code': 0}

    @app.route('/pe/p_xk')
    def p_xk():
        """
        精准人员轨迹续控请求
        :return:
        """
        return render_template(f'{root_path}/p_xk.html')

    @app.route('/pe/p_xk2')
    def p_xk2():
        zjhm = request.args.get('zjhm')
        date1 = request.args.get('date1')
        date2 = request.args.get('date2')

        res_netbar = request.args.get('res_netbar')
        res_hotel = request.args.get('res_hotel')
        res_roadway = request.args.get('res_roadway')

        logger.info(zjhm)

        return {'code': 0}

    @app.route('/pe/p_ck')
    def p_ck():
        """
        精准人员轨迹撤控请求
        :return:
        """
        return render_template(f'{root_path}/p_ck.html')

    @app.route('/pe/p_ck2')
    def p_ck2():
        zjhm = request.args.get('zjhm')

        res_netbar = request.args.get('res_netbar')
        res_hotel = request.args.get('res_hotel')
        res_roadway = request.args.get('res_roadway')

        logger.info(zjhm)

        return {'code': 0}


def get_subscribe_data():
    """
    获取订阅数据
    :return:
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/data/subscribe.json', mode='r+', encoding='utf-8') as fp:
        model_data = json.loads(fp.read(), encoding='utf-8')

    # 初始化数据
    model_data['messageSequence'] = str(uuid.uuid4())
    model_data['tasks'][0]['rwbh'] = str(uuid.uuid4())
    model_data['tasks'][0]['rules'][0]['dxywzjbh'] = str(uuid.uuid4())

    return model_data
