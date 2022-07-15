from flask import render_template, request

from com.pe.util.util import get_logger
import logging

logger = get_logger(__name__, logging.INFO)

root_path = 'cases/person'


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

        res_netbar = request.args.get('res_netbar')
        res_hotel = request.args.get('res_hotel')
        res_roadway = request.args.get('res_roadway')

        logger.info(f'params: {date1},date2 = {date2}, zjhm={zjhm}' )

        return {'code': 0}

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
