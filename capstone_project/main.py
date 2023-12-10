import os
import nbformat
from nbconvert import PythonExporter
from IPython.display import display, HTML

# Obtén la ruta al directorio actual de main.py
script_directory = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo de notebook
notebook_path = os.path.join(script_directory, 'Capstone_Project_Wizeline_XARJ.ipynb')

# Ruta al archivo de audio
audio_file_path = os.path.join(script_directory, 'resources', 'Message.mp3')

# Depuración: Imprimir la ruta del cuaderno y el audio
print(f"Notebook Path: {notebook_path}")
print(f"Audio File Path: {audio_file_path}")

# Intentar abrir el contenido del cuaderno (notebook)
try:
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = notebook_file.read()

    # Convierte el cuaderno a un script de Python
    notebook_node = nbformat.reads(notebook_content, as_version=4)
    exporter = PythonExporter()
    python_script, _ = exporter.from_notebook_node(notebook_node)

    # Ejecuta el script de Python
    exec(python_script)

except FileNotFoundError:
    print("Error: El archivo del cuaderno (notebook) no se encuentra. Verifica la ruta.")
except Exception as e:
    print(f"Error inesperado: {e}")
