#!/usr/bin/python3

#TODO: Update so images are pulled from the md dir


import os
from subprocess import call
import time
import markdown2
import re
import sys

root_dir = os.path.dirname(os.path.realpath(__file__))
md_dir = root_dir + '/md/'
html_dir = root_dir + '/html/'
current_time = time.time()

def update_file(file_name):
    html_file_name = re.sub(r'\.md', '.html', file_name)
    header = open(html_dir + "assets/header.html", 'r').read()
    footer = open(html_dir + "assets/footer.html", 'r').read()
    navigation = open(md_dir + "navigation", 'r')
    input = open(md_dir + file_name, 'r').read()
    output = open(html_dir + html_file_name, 'w')

    #build navigation
    nav_html = ''
    for line in navigation.readlines():
        file = re.sub(',.*', '', line)
        name = re.sub('.*,', '', line)
        nav_html += '<li><a href=' + file + '>' + name + '</a></li>'

    nav_html += '</ul></div><div id="page-content-wrapper">'

    markdown = markdown2.markdown(input, extras=['fenced-code-blocks', 'tables'])

    #tables!
    markdown = re.sub('<table>', '<table class="table table-bordered table-striped">', markdown)

    #take care of check boxes
    markdown = re.sub('\[\]', '<input type="checkbox">', markdown)

    out = header + nav_html + markdown + footer
    output.write(out)


def usage():
    print("\nDocumentation Generator\n")
    print("python update_md.py [Options]\n")
    print("Options:\n")
    print(" -h                         Print this help message")
    print(" -v                         Print version information")
    print(" -f <file name>             update specified file\n")
    print(" -a                         Update all files\n")
    print(" If no option is given this script will continually check for updates")
    print(" the the md directory and will update the html files accordingly\n")


def version():
    print("\nDocumentation Generator       Version 0.0.1.0\n")


merge_version = ""
assign = False
merge = False
documentation = False
users_guide = False
test_procedures = False
config_guide = False
design_description = False
issue = ""

argc = len(sys.argv)

all = False
file = False
file_name = ""
if len(sys.argv) > 1:
    for index, arg in enumerate(sys.argv):
        if arg == '-h':
            usage()
            exit()

        if arg == '-v':
            version()
            exit()

        if arg == '-a':
            all = True

        if arg == '-f':
            file = True
            file_name = sys.argv[index + 1]

if all:
    print("Updating all html")
    for root, dirs, filenames in os.walk(md_dir):
        for file in filenames:
            if re.search("md$", file):
                update_file(file)
elif file:
    update_file(file_name)
else:
    while True:
        time.sleep(1)
        for root, dirs, filenames in os.walk(md_dir):
            for file in filenames:
                if os.path.getmtime(md_dir + file) > current_time:
                    if re.search("md$", file):
                        print(time.strftime("%H:%M:%S") + "    " + file + ": updating html")
                        update_file(file)
            current_time = time.time()
