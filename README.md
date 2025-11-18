# MT-TOC
# Clonar o abrir el proyecto
cd MT-TOC

# (Opcional) Crear entorno virtual
# python -m venv venv
# source venv/Scripts/activate   # En Windows

# Instalar la única dependencia necesaria
pip install pyyaml

# Ejecutar el simulador con cualquier archivo YAML
python main.py mt_recognizer.yaml
python main.py mt_alter.yaml
python main.py mt_w_w.yaml

# Ejemplo general:
python main.py <nombre_del_archivo>.yaml



## Link de YT:
https://youtu.be/-WM0C10m-7o