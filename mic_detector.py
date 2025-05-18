import pyaudio
import threading
import time

class MicDetector:
    def __init__(self, threshold=100, silence_delay=0.085):
        self.threshold = threshold
        self.silence_delay = silence_delay
        self.active = False
        self.running = False
        self.last_active_time = time.time()

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._detect)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def is_active(self):
        return time.time() - self.last_active_time < self.silence_delay

    def _detect(self):
        pa = pyaudio.PyAudio()
        stream = pa.open(format=pyaudio.paInt16, channels=1, rate=44100,
                         input=True, frames_per_buffer=1024)
        while self.running:
            data = stream.read(1024, exception_on_overflow=False)
            volume = max(abs(int.from_bytes(data[i:i+2], 'little', signed=True)) for i in range(0, len(data), 2))
            if volume > self.threshold:
                self.last_active_time = time.time()
            time.sleep(0.1)
        stream.stop_stream()
        stream.close()
        pa.terminate()