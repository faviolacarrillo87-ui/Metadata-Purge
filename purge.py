import os
import subprocess

def limpiar_metadatos(archivo):
    print(f"\n[!] Operación Z-Intel: Procesando {archivo}")
    try:
        # Comando para borrar metadatos y GPS de forma irreversible
        subprocess.run(["exiftool", "-all=", "-overwrite_original", archivo])
        print(f"[OK] {archivo} ahora es anónimo y seguro para compartir.")
    except Exception as e:
        print(f"[ERROR] Fallo en la limpieza: {e}")

print("--- METADATA PURGE | PORTAFOLIO Z-INTEL ---")
archivo_objetivo = input("Ingresa la ruta de la imagen o archivo a limpiar: ")

if os.path.exists(archivo_objetivo):
    limpiar_metadatos(archivo_objetivo)
else:
    print("Archivo no localizado.")

