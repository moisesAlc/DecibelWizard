from moviepy.editor import *

from gui import gui_utils


def increase_volume_in_section(video_path_arg, start_time_arg, end_time_arg, volume_multiplier_arg, output_path_arg):
    # Carrega o vídeo
    video = VideoFileClip(video_path_arg)

    # Define o trecho do vídeo em que o volume será aumentado
    video_section = video.subclip(start_time_arg, end_time_arg)

    # Aumenta o volume do trecho do vídeo
    video_section = video_section.volumex(volume_multiplier_arg)

    # Obtém o trecho do vídeo antes do ponto de início
    pre_section = video.subclip(0, start_time_arg)

    # Obtém o trecho do vídeo após o ponto final
    post_section = video.subclip(end_time_arg, video.duration)

    # Concatena os trechos do vídeo
    final_video = concatenate_videoclips([pre_section, video_section, post_section])

    # Mantém as configurações originais do vídeo (resolução e taxa de quadros)
    final_video = final_video.set_make_frame(video.make_frame)
    final_video = final_video.set_duration(video.duration)

    # Salva o vídeo resultante com alta qualidade usando o codec libx264
    final_video.write_videofile(output_path_arg, codec='libx264', bitrate="5000k")

    # Fecha o vídeo carregado
    video.close()
    final_video.close()


if __name__ == '__main__':
    # Exemplo de uso
    video_path2 = gui_utils.get_file_gui()
    video_path = r'C:\Users\MoisesMadeira\Downloads\Vídeo 00 - Sumário.mp4'
    start_time = 6  # Segundos - ponto de início da seção que terá o volume aumentado
    end_time = 127  # Segundos - ponto final da seção que terá o volume aumentado
    volume_multiplier = 5  # Fator pelo qual o volume será multiplicado (1.0 mantém o volume original)
    output_path = gui_utils.get_save_destination_gui()
    output_path_filename = output_path.name

    increase_volume_in_section(
        video_path2, start_time, end_time, volume_multiplier, output_path_filename
    )
