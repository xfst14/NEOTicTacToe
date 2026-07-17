import sys
import os

def get_resource_path(relative_path):
    """Get absolute path to a resource, works in dev and with PyInstaller."""
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))

    candidate = os.path.join(base_path, relative_path)
    if os.path.exists(candidate):
        return candidate

    src_candidate = os.path.join(base_path, "src", relative_path)
    if os.path.exists(src_candidate):
        return src_candidate

    return candidate
