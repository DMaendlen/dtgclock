"""
Date-Time-Group clock for usage in desaster relief operations.
For details regarding DTG check out https://en.wikipedia.org/wiki/Date-time_group
"""

from datetime import datetime
from tkinter import Tk, Label


def get_timezone_letter(now: datetime):
    """
    Get timezone letter for the timezone of a datetime object.
    """

    timezones = dict([(-12.0, 'Y'),
                      (-11.0, 'X'),
                      (-10.0, 'W'),
                      (-9.0, 'V'),
                      (-8.0, 'U'),
                      (-7.0, 'T'),
                      (-6.0, 'S'),
                      (-5.0, 'R'),
                      (-4.0, 'Q'),
                      (-3.0, 'P'),
                      (-2.0, 'O'),
                      (-1.0, 'N'),
                      (0.0, 'Z'),
                      (1.0, 'A'),
                      (2.0, 'B'),
                      (3.0, 'C'),
                      (4.0, 'D'),
                      (5.0, 'E'),
                      (6.0, 'F'),
                      (7.0, 'G'),
                      (8.0, 'H'),
                      (9.0, 'I'),
                      (10.0, 'K'),
                      (11.0, 'L'),
                      (12.0, 'M')])

    offset = now.astimezone().utcoffset().seconds / 3600 # 3600 seconds per hour
    if now.astimezone().utcoffset().days:
        # subtract a full day
        offset = offset - 24

    return timezones[offset]

def set_time():
    """
    Create a time string for the current time in the format of %d%H%M{Timezoneletter}%b%y.
    Then use that string to update the Tkinter label every second.
    """
    now = datetime.now()
    time = now.strftime("%d%H%M-x-%b%y").lower()
    label.config(text=time.replace('-x-', get_timezone_letter(now)))
    label.after(1000, set_time)



window = Tk()
window.title("Date Time Group")
window.geometry('495x70')

label = Label(window,
              background='#00387b',
              foreground='white',
              font=("Lubalin Graph Bold", 43, 'bold'))
label.pack(anchor='center')
set_time()

window.mainloop()
