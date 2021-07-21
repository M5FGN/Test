from codeclan_events import app
from flask import render_template, request, redirect
from models.events_list import events, add_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events/new')
def new():
    return render_template('new.html', title='Add Event')

@app.route('/events', methods=['post'])
def create():
    event_date = request.form['date']
    event_name = request.form['event_name']
    num_guests = request.form['num_guests']
    room_loc = request.form['room_loc']
    description = request.form['description']
    new_event = Event(event_date, event_name, num_guests, room_loc, description)
    add_event(new_event)
    return redirect('/events')