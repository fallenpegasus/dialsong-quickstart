
# DialSong
# a demo of OpenShift and Twilio

# Implements a very simple "dial-a-song" service.

import os
import bottle

bottle.debug(True)

@bottle.get('/')
def web_root():
    return """
<html>
<body>
<h1>OpenShift DialSong</h1>
<p>A demonstration of <a href="http://openshift.com">OpenShift</a>
and <a href="http://twilio.com">Twilio</a>.</p>
<p>Go to
 http://github.com/openshift/dialsong-quickstart
to set up your own DialSong server.</p>
</body>
</html>
"""

@bottle.get('/admin')
def web_get_admin():
    return """
<html>
<body>
<h1>OpenShift DialSong</h1>
<h2>Get Admin</h2>
<form method='POST' action='/admin'>
URL of the music: <input type=text name=url><br>
About the music: <input type=text name=note><br>
<br>
<input type=submit value=Press>
</body>
</html>
"""

@bottle.post('/admin')
def web_post_admin():
    url = bottle.request.forms.get('url')
    note = bottle.request.forms.get('note')
    open(os.environ['OPENSHIFT_DATA_DIR'] + '/data-url', 'w').write(url)
    open(os.environ['OPENSHIFT_DATA_DIR'] + '/data-note', 'w').write(note)
    return """
<html>
<body>
<h1>OpenShift DialSong</h1>
<h2>Post Admin</h2>
URL of the music: %s<br>
About the music: %s<br>
</body>
</html>
""" % (url, note)


@bottle.get('/twilio')
def twilio():

    # Someone has dialed the number, and Twilio has done a HTTP GET to this URL
    # The query string may have the following parameters:
    #  CallSid, AccountSid, From, To, CallStatus, ApiVersion, Direction, FowardedFrom,
    #  CallerName, FromCity, FromState, FromZip, FromCountry,
    #  ToCity, ToState, ToZip, ToCountry

    can_play = False
    try:
        url = open(os.environ['OPENSHIFT_DATA_DIR'] + '/data-url').read()
        note = open(os.environ['OPENSHIFT_DATA_DIR'] + '/data-note').read()
        can_play = True
    except:
        can_play = False
        
    bottle.response.content_type = 'text/xml; charset=UTF8'

    if (can_play):
        return """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>OpenShift dialsong with Twilio, presents, </Say>
    <Say>%s</Say>
    <Play>%s</Play>
</Response>
""" % (note, url)
    else:
        return """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>OpenShift dialsong with Twilio, is not configured. </Say>
</Response>
"""

if __name__ == '__main__':
    bottle.run(host='localhost', port=8051, reloader=True)
else:
    application = bottle.default_app()
