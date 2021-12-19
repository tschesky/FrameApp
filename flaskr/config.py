from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, send_file
)

bp = Blueprint('config', __name__, url_prefix='/config')


@bp.route('', methods=['POST'], strict_slashes=False)
def update_config():
    if request.method == 'POST':
        return '200'
    return '400'


@bp.route('', methods=['GET'], strict_slashes=False)
def get_config():
    if request.method == 'GET':
        return '200'
    return '400'
