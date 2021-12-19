import functools
import os
import sys
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, send_file
)
from flaskr.db import get_db
from werkzeug.utils import secure_filename
from flask import current_app
from flask import send_from_directory
from flask_cors import CORS, cross_origin

bp = Blueprint('images', __name__, url_prefix='/images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('', methods=['POST'], strict_slashes=False)
@cross_origin()
def upload_img():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return '400'
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return '400'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return '201'
    return '400'


@bp.route('', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_img_list():
    if request.method == 'GET':
        img_list = [f for f in os.listdir(current_app.config['UPLOAD_FOLDER'])
                    if os.path.isfile(os.path.join(current_app.config['UPLOAD_FOLDER'], f))]
        return jsonify(img_list)
    return '400'


@bp.route('/<img_name>', methods=['DELETE'])
@cross_origin()
def delete_img(img_name):
    os.remove(os.path.abspath(os.path.join(current_app.config['UPLOAD_FOLDER'], img_name)))
    return '200'


@bp.route('/<img_name>', methods=['GET'])
@cross_origin()
def serve_img(img_name):
    return send_file(os.path.abspath(os.path.join(current_app.config['UPLOAD_FOLDER'], img_name)))
