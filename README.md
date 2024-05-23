# gopro_ctrl
Python utility for gopro remote control

# Requirements
python 3.11 (recommended, 3.12 not yet working with gopro api's) 

# Setup for developent
Setup python virtual env and install in development mode.
```
python -m venv _venv
.\_venv\Scripts\activate.bat
pip install -e .
```

# Running / Connection
The first connection requires for BLE pairing, which can be achieved by running the gopro_stream.py
and while it is scanning the ble devices, go to the GoPro Settings -> Connection -> Connect Quik App.
