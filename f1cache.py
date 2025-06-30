import os
import fastf1

# Setup FastF1 cache
def load_cache():
    """
    Setup FastF1 cache directory.
    This function creates a cache directory for FastF1 if it doesn't exist.
    """
    if not os.path.exists('.fastf1_cache'):
        print("Creating FastF1 cache directory...")
    else:
        print("FastF1 cache directory already exists.")
        fastf1.Cache.enable_cache('.fastf1_cache')