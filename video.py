from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import os

# Configurações
image_folder = 'frames'
output_video = 'saida.mp4'
fps = 4

# Coleta e ordena as imagens
images = sorted([
    os.path.join(image_folder, img)
    for img in os.listdir(image_folder)
    if img.endswith(".png")
])

# Cria e exporta o vídeo
clip = ImageSequenceClip(images, fps=fps)
clip.write_videofile(output_video, codec='libx264')

print(f"Vídeo salvo como: {output_video}")
