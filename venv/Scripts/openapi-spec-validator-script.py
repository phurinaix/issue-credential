#!D:\Blockchain\Blockcerts\cert-issuer\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'openapi-spec-validator==0.2.7','console_scripts','openapi-spec-validator'
__requires__ = 'openapi-spec-validator==0.2.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('openapi-spec-validator==0.2.7', 'console_scripts', 'openapi-spec-validator')()
    )
