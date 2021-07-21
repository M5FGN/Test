from models.event import * 

event1 = Event('1/3/21', 'CodeClan Coffee', 5, 'Virtual', 'Grab a coffee, log in and chat with other CodeClan students')
event2 = Event('2/3/21', 'CodeClan Photo Competition', 10, 'Virtual', 'Send in your snaps to win prizes')
event3 = Event('3/3/21', 'Graduation', 20, 'Virtual', 'Celebrate with G24')

events = [event1, event2, event3]

def add_event(new_event):
    events.append(new_event)


