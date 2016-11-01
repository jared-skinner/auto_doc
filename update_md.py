#!/usr/bin/python3

import os
from subprocess import call
import time
import markdown2
import re

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

while True:
    time.sleep(1)
    for root, dirs, filenames in os.walk(md_dir):
        for file in filenames:
            if os.path.getmtime(md_dir + file) > current_time:
                print(file + ": updating html")
                update_file(file)
        current_time = time.time()
