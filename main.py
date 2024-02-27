from gui import gui_utils
from video.utils import increase_volume_in_section

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
