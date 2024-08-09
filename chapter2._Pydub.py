from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('Fix-You.mp3')

# Menyimpan file audio
audio.export('result.mp3', format='mp3')

# Memotong file audio: 10 detik pertama
clipped_audio = audio[:10000]
clipped_audio.export('clipped_result.mp3', format='mp3')

# Menggabungkan dua file audio
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

# Mengonversi file audio ke format lain
audio.export('result.wav', format='wav')

# Meningkatkan volume audio sebesar 10db
louder_audio = audio + 10
louder_audio.export('louder_result.mp3', format='mp3')

