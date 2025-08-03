import cv2
import os

# Ruta del video
video_path = "C:\\Users\\tu\\Desktop\\dentdirect\\videos_bollos\\videobollo.mp4"

# Carpeta de salida para las imágenes
output_folder = "C:\\Users\\tu\\Desktop\\dentdirect\\fotos_bollos\\images"
os.makedirs(output_folder, exist_ok=True)

# Cargar el video
cap = cv2.VideoCapture(video_path)

# Verificar si el video se cargó correctamente
if not cap.isOpened():
    print("Error: No se pudo cargar el video.")
    exit()

# Configuración de extracción
frame_rate = 40  # Extraer 1 imagen cada 40 fotogramas
frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Salir cuando se terminen los fotogramas

    # Guardar una imagen cada 'frame_rate' fotogramas
    if frame_count % frame_rate == 0:
        output_path = os.path.join(output_folder, f"frame_{saved_count}.jpg")
        cv2.imwrite(output_path, frame)
        print(f"Imagen guardada: {output_path}")
        saved_count += 1

    frame_count += 1

cap.release()
print(f"Extracción completada. Total de imágenes guardadas: {saved_count}")