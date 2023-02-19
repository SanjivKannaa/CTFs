import os
os.environ.setdefault("secret_", "shit")
print(os.environ.get("secret_"))