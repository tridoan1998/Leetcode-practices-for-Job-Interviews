from datetime import datetime

from formatting import format_mes

def send(name, website):
    msg = format_mes(myname=name, mywebsite=website)
    return msg


