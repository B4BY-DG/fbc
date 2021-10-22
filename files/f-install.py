#coding=utf-8
#!/usr/bin/python2

import os
import re
import paltform

bit = platform.architecture()[0]
if bit == '64bit':
    os.system("cd 64bit && python2 f64.py")
elif bit == '32bit':
    os.system("cd 32bit && python2 f32.py")
