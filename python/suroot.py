#!/usr/bin/env python
import sys
import traceback
import re
import threading
import paramiko
from paramikoe import SSHClientInteraction

def main(ip, username, password, prompt, xprompt):

    # Use SSH client to login
    try:

        # Create a new SSH client object
        client = paramiko.SSHClient()

        # Set SSH key parameters to auto accept unknown hosts
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the host
        client.connect(hostname=hostname, username=username, password=password)

        # Create a client interaction class which will interact with the host
        interact = SSHClientInteraction(client, timeout=10, display=True)
        interact.expect(xprompt)
        if not username == 'root':
            interact.send('su - root')
	    interact.expect([xprompt, 'Password: '])
	    if interact.last_match == 'Password: ':
		interact.send('pass')
		interact.expect(prompt)

        # Run the first command and capture the cleaned output, if you want the output
        # without cleaning, simply grab current_output instead.
        interact.send('uname -a')
        interact.expect(prompt)
        cmd_output_uname = interact.current_output_clean


        # To expect multiple expressions, just use a list.  You can also selectively
        # take action based on what was matched.

        # Method 1: You may use the last_match property to find out what was matched
        interact.send('~/paramikoe-demo-helper.py')
        interact.expect([prompt, 'Please enter your name: '])
        if interact.last_match == 'Please enter your name: ':
            interact.send('Fotis Gimian')
            interact.expect(prompt)


        # Send the exit command and expect EOF (a closed session)
        interact.send('exit')
	#interact.expect()

    except Exception as e:
        traceback.print_exc()
    finally:
        try:
            client.close()
        except:
            pass

if __name__ == '__main__':
    ip = 'localhost'
    username = 'xinhu'
    password = 'xxxxxxx'
    prompt = '.*root.*'
    xprompt = '.*xinhu.*'
    for i in xrange(1, 254):
	    ip = '192.168.1.' + str(i)
	    mission = threading.Thread(target=main, args=(ip, username, password, prompt, xprompt))
	    mission.start()
###这里用密钥登录更好点。