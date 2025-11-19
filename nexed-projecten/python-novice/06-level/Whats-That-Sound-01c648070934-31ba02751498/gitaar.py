import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("gitaar.wav")
play_obj = wave_obj.play()

print("Geluid wordt afgespeeld")

play_obj.wait_done()
