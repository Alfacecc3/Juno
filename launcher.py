#launcher
import time
import subprocess as sb
exec(open('txtmkr.py').read())
time.sleep(1)
sb.call('cscript junoSpeaker.vbs')
