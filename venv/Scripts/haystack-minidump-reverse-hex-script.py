#!E:\webProject\mysite\venv\Scripts\python3.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'haystack==0.36','console_scripts','haystack-minidump-reverse-hex'
__requires__ = 'haystack==0.36'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('haystack==0.36', 'console_scripts', 'haystack-minidump-reverse-hex')()
    )
