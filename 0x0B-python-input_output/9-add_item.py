#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import json
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('8-load_from_json_file').load_from_json_file

    items = []

    if len(sys.argv) == 1:
        save_to_json_file(items, "add_item.json")
    else:
        try:
            items = load_from_json_file("add_item.json")
        except FileNotFoundError:
            pass
        finally:
            items.extend([sys.argv[i] for i in range(1, len(sys.argv))])
            save_to_json_file(items, "add_item.json")
