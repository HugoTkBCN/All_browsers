#!/usr/bin/python3

import fileinput
import sys
import os

def generate_workspace(version):
    f=open("docker-compose.yml","w")
    new_line1 ='        - CHROME_VERSION='+version
    new_line2 ='    image: google-chrome:'+version
    template = "docker-compose_template.yml"
    macs = {
        '        - CHROME_VERSION=[VERSION]': new_line1,
        '    image: google-chrome:[VERSION]': new_line2
    }
    for line in fileinput.input(template):
        line = line.rstrip('\r\n')
        f.write(macs.get(line, line)+"\n")
    f.close()

version=sys.argv[1]
generate_workspace(version)
myCmd = './run'
os.system(myCmd)