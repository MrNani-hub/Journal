from flask import Blueprint, render_template, request, redirect, url_for
from .models import JournalEntry
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    entries = JournalEntry.query.order_by(JournalEntry.date_created.desc()).all()
    return render_template('index.html', entries=entries)

@main.route('/add', methods=['POST'])
def add_entry():
    title = request.form['title']
    content = request.form['content']
    new_entry = JournalEntry(title=title, content=content)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('main.index'))