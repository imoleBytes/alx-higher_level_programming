#!/usr/bin/python3

"""scripts add all argumets to a python list
saved to a json file
"""
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


argv = sys.argv[1:]
filename = "add_item.json"

if os.path.exists(filename):
    list_items = load_from_json_file(filename)
    new = list_items + argv
    save_to_json_file(new, filename)
else:
    save_to_json_file(argv, filename)
