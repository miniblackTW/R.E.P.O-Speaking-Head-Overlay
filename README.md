# R.E.P.O-Speaking-Head-Overlay
An app that detects your microphone and make the R.E.P.O robot head open or close its mouth

# Showcase Video:
[![YouTube](https://i.ytimg.com/vi/q6A8Z27x5aI/hqdefault.jpg)](https://youtu.be/q6A8Z27x5aI?si=ZLEUqJu5vPDpDXdG)

# How to use
- Clone this repository
- Install dependencies - `pip install flask pyaudio`
- Run `python app.py` at the root folder of this project (**Python 3 required**), it will be running on localhost:25226
- To use this in OBS as overlay, you just have to add `http://localhost:25226` as **Browser Source** to OBS (From my experience, 300×300 is just right)