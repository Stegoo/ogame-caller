# Ogame Caller

The script gives you a call whenever you are attacked.

# Principles

What the script does :

1. Log into your account and check every 60-120min (random value) whether you are attacked.
2. If you are attacked, create a .call file and give it to asterisk. Also write the message to be read in a file.
3. asterisk calls you and read the message.

It also save your resources whenever it reaches a defined threshold.

# Dependancies and libraries

This only works on Linux.
Check the Vagrantfile for the commands. You need:
- an sip account (I use ovh)
- asterisk (voip server, 11.x 64bits)
- [flite](http://www.speech.cs.cmu.edu/flite/) (text to speech engine, 1.4 64bits)
- [flite-asterisk] (https://github.com/zaf/Asterisk-Flite)
- pip, python3, virtualenv
- supervisor

# Pitfalls to avoid when installing it

I lost a fair amount of time making the following mistakes :
- Don't install asterisk from apt, build it from the source. Don't install the latest version because many modules are not updated.
- Don't use google-tts, it's not reliable because they can forbid you the access any time they want. I could not get eSpeak to work so I went with Flite.
- Use `asterisk -r` to access the cli interface and type : `sip reload` to reload the sip.conf, `dialplan reload` to reload the extensions.conf, `module reload` to reload the modules.conf. Here is the [list of commands](http://www.asteriskguru.com/tutorials/cli_cmd_14.html) you may need

# Questions ?

If you are interested in using this script and have trouble installing it on your server. Open an issue and I will write more documentation.
