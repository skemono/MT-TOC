import sys
from parser_yaml import load_mt_from_yaml

def main():
    # Verificar que el usuario mandó el archivo YAML
    if len(sys.argv) < 2:
        print("Debe especificar el archivo YAML que describe la máquina de Turing.")
        print("Ejemplo: python main.py mt_recognizer.yaml")
        sys.exit(1)

    yaml_file = sys.argv[1]

    # Cargar la configuración de la MT y las cadenas a simular
    tm, cadenas = load_mt_from_yaml(yaml_file)

    if not cadenas:
        print("El YAML no contiene ninguna cadena en 'simulation_strings'.")
        return

    # Ejecutar la simulación para cada cadena
    for c in cadenas:
        tm.run(c)


if __name__ == "__main__":
    main()
