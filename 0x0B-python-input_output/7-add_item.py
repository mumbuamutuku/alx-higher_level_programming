#!/usr/bin/python3
# 7-add_item.py
"""Add all arguments to a Python list and save them to a file."""
from sys import argv
import json
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_file = 'add_item.json'
if os.path.isfile(my_file):
    my_list = load_from_json_file(my_file)
else:
    my_list = []
count = 0
for item in argv:
    if count != 0:
        my_list.append(item)
    count += 1
save_to_json_file(my_list, my_file)
