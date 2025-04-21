import subprocess

subprocess.getoutput("adb forward tcp:27042 tcp:27042")
subprocess.getoutput("adb forward tcp:27043 tcp:27043")


# adb forward tcp:6666 tcp:6666