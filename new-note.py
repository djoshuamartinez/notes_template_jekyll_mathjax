#!/usr/bin/python3

from datetime import datetime
from time import timezone
import sys

notes_dir = "./course/_posts/"
stubs_dir = "./stubs/"

current_date = datetime.now()

new_note_file_name = current_date.strftime("%Y-%m-%d-%H%M")+".md"


tz = int(timezone*100/3600)
if tz < 0:
    tz = '+'+str(-tz).zfill(4)
else:
    tz = '-'+str(tz).zfill(4)


full_date = current_date.strftime('%Y-%m-%d %H:%M:%S '+tz)
friendly_date = current_date.strftime('%d/%m/%y')

new_note_full_url = notes_dir+new_note_file_name

stub = open(stubs_dir+'new-note.stub', 'r')
new_note = open(new_note_full_url, 'w')

contents = stub.read()
new_note.write(contents.replace('FULL_DATE', full_date)
    .replace('FRIENDLY_DATE', friendly_date))

stub.close()
new_note.close()

sys.stdout.write(new_note_full_url)
sys.stdout.flush()
sys.exit(0)
