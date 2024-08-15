from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx

# Memuat file video
video = VideoFileClip('Video/Never_Let_Go.mp4')

# Menyimpan file video
video.write_videofile('result.mp4')

# Memotong video untuk 10 detik pertama
short_video = video.subclip(0, 10)
short_video.write_videofile('short_result.mp4')

# Menggabungkan 2 file video
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

# Menambahkan efek pembalikan waktu pada video
reversed_video = short_video.fx(vfx.time_mirror)
reversed_video.write_videofile('reversed_result.mp4')

# Kecepatan video menjadi 2 kali lebih cepat
sped_up_video = short_video.fx(vfx.speedx, 2)
sped_up_video.write_videofile('sped_up_result.mp4')