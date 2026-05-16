import subprocess

def webm_to_mp4(input, output):
    command = [
        'ffmpeg',
        '-i', input,             # Archivo de entrada
        '-c:v', 'libx264',       # Video codec compatible con iPhone
        '-preset', 'slow',       # Mejor calidad
        '-crf', '22',            # Calidad constante balanceada
        '-c:a', 'aac',           # Audio compatible con iPhone
        '-b:a', '192k',          # Bitrate de audio
        output
    ]
    
    try:
        print("Repairing metadata and converting...")
        subprocess.run(command, check=True)
        print(f"Successfully converted: {output}")
    except Exception as e:
        print(f"Error occurred while running FFmpeg: {e}")

def convert(video_name, input_dir='input', output_dir='output'):
    input_path = f"{input_dir}/{video_name}.webm"
    output_path = f"{output_dir}/{video_name}.mp4"
    webm_to_mp4(input_path, output_path)