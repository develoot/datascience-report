#!/usr/bin/python3

import csv
import math
import re
import subprocess
import sys
import threading
import time

def collect():
    t = math.floor(time.time())
    result = subprocess.run(['systemd-cgtop', '-br', '--iteration=1', '--cpu=time',
        f'{sys.argv[1]}'], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception()

    m = p.match(result.stdout)
    cputime = m.group(5)

    print(f'cputime: {cputime}')

    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([sys.argv[1], t, m.group(5)])

    threading.Timer(int(sys.argv[2]), collect).start()


"""
ControlGroup Tasks RunningTime CPUTime Memory Input/s Output/s
([a-zA-Z0-9-_./]*)(\s*)([0-9-]*)(\s*)([0-9-]*)(\s*)([0-9-]*)(\s*)([0-9-]*)(\s*)([0-9-]*)(\s*)([0-9-]*)
"""
p = re.compile('([a-zA-Z0-9-_./]*)(\s*)([0-9-]*)(\s*)([0-9-]*)(\s*)([0-9-]*)(\s*)([0-9-]*)(\s*)([0-9-]*)(\s*)([0-9-]*)')

collect()
