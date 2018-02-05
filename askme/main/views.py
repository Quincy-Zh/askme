# askme/main/views.py

import os
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask import current_app

from flask_uploads import UploadSet, IMAGES

from . import main
from .models import Question

@main.route('/uploads/<filename>')
def uploaded_file(filename):
    images = current_app.config['images']
    url = images.url(filename)
    
    return redirect(url)

@main.route('/editor_upload_img', methods=['POST'])
def editor_upload_img():
    images = current_app.config['images']
    if request.method == 'POST' and 'file' in request.files:
        filename = images.save(request.files['file'])
        #rec = Photo(filename=filename, user=g.user.id)
        #rec.store()
        flash("Photo saved.")

        return jsonify(location=url_for('main.uploaded_file', filename=filename))
        
@main.route('/new', methods=['GET', 'POST'])
def new_question():
    if request.method == 'POST':
        #print(request.form['content'])
        
        q = Question(request.form['title'], request.form['content'])
        db.session.add(q)
        db.session.commit()
        
        flash('成功提问')
        
        return redirect(url_for('main.question', id=q.id))
        
    return render_template('new.html')
    
@main.route('/question/<int:id>')
def question(id):
    q = Question.query.get_or_404(id)
    
    return '{0}\n{1}\n{2}'.format(q.id, q.title, q.description)
    
@main.route('/')
def index():
    return 'Hello, ASKME'
    