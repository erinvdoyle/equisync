import os
import ssl
import subprocess
import sys

print("Installing certificates using certifi...")

try:
    import certifi

    cafile = certifi.where()

    if not hasattr(ssl, 'create_default_context'):
        print("Your Python install doesn't support ssl.create_default_context")
        sys.exit(1)

    os.environ['SSL_CERT_FILE'] = cafile

except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "certifi"])
