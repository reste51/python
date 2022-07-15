from flask import render_template, request
from com.pe.util.util import get_logger
import logging

logger = get_logger(__name__, logging.INFO)

root_path = 'cases/vehicle'


def set_v_route(app):
    @app.route('/pe/v_trails')
    def v_trails():
        """
        精准车辆轨迹布控请求
        :return:
        """
        return render_template(f'{root_path}/v_trails.html')

    @app.route('/pe/v_trails2')
    def v_trails2():
        date1 = request.args.get('date1')
        date2 = request.args.get('date2')
        hphm = request.args.get('hphm')

        res_netbar = request.args.get('res_netbar')
        res_hotel = request.args.get('res_hotel')
        res_roadway = request.args.get('res_roadway')

        logger.info(f'params: hphm={hphm}')

        return {'code': 0}

    @app.route('/pe/v_ck')
    def v_ck():
        """
        精准车辆轨迹自动撤控
        :return:
        """
        return render_template(f'{root_path}/v_ck.html')

    @app.route('/pe/v_ck2')
    def v_ck2():
        date1 = request.args.get('date1')
        date2 = request.args.get('date2')
        hphm = request.args.get('hphm')

        res_netbar = request.args.get('res_netbar')
        res_hotel = request.args.get('res_hotel')
        res_roadway = request.args.get('res_roadway')

        logger.info(f'params: hphm={hphm}')

        return {'code': 0}
