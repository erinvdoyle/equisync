import os
import ssl
import subprocess
import sys

print("📥 Installing certificates using certifi...")

try:
    import certifi

    cafile = certifi.where()
    print(f"✅ certifi found: {cafile}")

    if not hasattr(ssl, 'create_default_context'):
        print("❌ Your Python install doesn't support ssl.create_default_context")
        sys.exit(1)

    # Set system environment variable to use certifi bundle
    os.environ['SSL_CERT_FILE'] = cafile

    print("🔐 SSL_CERT_FILE set to certifi bundle.")
    print("✅ Certificates installed successfully!")

except ImportError:
    print("❌ certifi is not installed. Installing it now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "certifi"])
    print("✅ certifi installed. Run the script again.")
