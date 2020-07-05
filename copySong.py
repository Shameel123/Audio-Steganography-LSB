import wave
from numpy.fft import rfft, rfftfreq
with wave.open("Song.wav", "rb") as wav_file: # Open WAV file in read-only mode.
    # Get basic information.
    n_channels = wav_file.getnchannels() # Number of channels. (1=Mono, 2=Stereo).
    sample_width = wav_file.getsampwidth() # Sample width in bytes.
    framerate = wav_file.getframerate() # Frame rate.
    n_frames = wav_file.getnframes() # Number of frames.
    comp_type = wav_file.getcomptype() # Compression type (only supports "NONE").
    comp_name = wav_file.getcompname() # Compression name.
    # Read audio data.
    frames = wav_file.readframes(n_frames*10) # Read n_frames new frames.
    #assert len(frames) == sample_width * n_frames



# Duplicate to a new WAV file.
with wave.open("songDuplicate.wav", "wb") as wav_file: # Open WAV file in write-only mode.
    # Write audio data.
    params = (n_channels, sample_width, framerate, n_frames, comp_type, comp_name)
    wav_file.setparams(params)
    wav_file.writeframes(frames)
