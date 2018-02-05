# askme/main/views.py

import os
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask import current_app

from flask_uploads import UploadSet, IMAGES

from . import main


@main.route('/uploads/<filename>')
def uploaded_file(filename):
    images = current_app.config['images']
    url = images.url(filename)
    
    return redirect(url)
    
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['content'])
    return render_template('index.html')

@main.route('/editor_upload_img', methods=['POST'])
def editor_upload_img():
    images = current_app.config['images']
    if request.method == 'POST' and 'file' in request.files:
        filename = images.save(request.files['file'])
        #rec = Photo(filename=filename, user=g.user.id)
        #rec.store()
        flash("Photo saved.")

        return jsonify(location=url_for('main.uploaded_file', filename=filename))