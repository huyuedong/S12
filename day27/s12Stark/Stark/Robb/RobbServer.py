#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import os
import sys

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Stark.settings")

    from Robb.backends.management import execute_from_command_line
    from Stark import settings

    execute_from_command_line(sys.argv)
