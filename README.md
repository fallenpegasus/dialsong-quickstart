DialSong on OpenShift with Twilio
=================================

This is a very simple "dial-a-song" server that uses OpenShift and Twilio.


Instructions
------------

Create an account at http://openshift.com/

Create a python application

    rhc app create -a dialsong -t python-2.6

Add this upstream repo

    cd dialsong
    git remote add upstream -m master git://github.com/openshift/dialsong-quickstart.git
    git pull -s recursive -X theirs upstream master
    
Push this application into OpenShift

    git push

Browse to http://dialsong-$yournamespace.rhcloud.com/admin

Fill in the form.  For example:

    note:  Mandelbrot Set by Jonathan Coulton
    url:  http://www.archive.org/download/JocoLooksBack/04MandelbrotSet.mp3

Create a Twilio account at http://twilio.com

Browse to https://www.twilio.com/user/account

Go to the "Sandbox App".  Look for "App Details" and "Voice URL"

Set the Voice URL to http://dialsong-$yournamespace.rhcloud.com/twilio

On a telephone, dial the Sandbox number and the Sandbox PIN

Listen to the music
