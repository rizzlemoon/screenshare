# About
Super-simple screen sharing with nothing but Python and Flask.

# Necessary libraries

    pip install -r requirements.txt

# Running

    python screen.py
    
Then visit [http://localhost:5000](http://localhost:5000).

# Options

    python screen.py --port 5000 --interval 500 --prefix /screen
    
    * --port: port number
    * --interval: refresh interval in millseconds
    * --prefix: server url prefix

You can also change refresh interval by query string like below.

	http://localhost:5000/?interval=1000

# Disclaimer

Tested with Ubuntu 12.04. The pyscreenshot library may not work on your system!


# Changes

Supporting python3.
[https://github.com/di/screenshare](https://github.com/di/screenshare