# Simulador de Máquina de Turing

Simulador de Máquinas de Turing con memoria caché implementado en Python.

## Video
[![Ver video](https://img.youtube.com/vi/X70p4vTHLcQ/hqdefault.jpg)](https://youtu.be/X70p4vTHLcQ)

## Características

- Simulación de Máquinas de Turing con memoria caché
- Configuración mediante archivos YAML
- Visualización de descripciones instantáneas (IDs)
- Soporte para símbolos blancos en la cinta
- Tres máquinas de ejemplo incluidas

## Requisitos

- Python 3.x
- PyYAML

## Instalación

```bash
pip install pyyaml
```

## Uso

Ejecutar el simulador con cualquier archivo YAML de configuración:

```bash
python main.py <archivo>.yaml
```

### Ejemplos incluidos

```bash
# Reconocedor de cadenas que empiezan con 'a'
python main.py mt_recognizer.yaml

# Alterador: reemplaza 'a' por 'X'
python main.py mt_alter.yaml

# Reconocedor w#w (palíndromos con separador)
python main.py mt_w_w.yaml
```

## Estructura del proyecto

- `turing_machine.py` - Implementación de la Máquina de Turing
- `parser_yaml.py` - Parser de configuración YAML
- `main.py` - Punto de entrada del simulador
- `mt_*.yaml` - Ejemplos de máquinas de Turing

## Formato YAML

Los archivos de configuración deben seguir esta estructura:

```yaml
q_states:
  q_list: [lista de estados]
  initial: estado_inicial
  final: estado_final

tape_alphabet: [símbolos de la cinta]

delta: [transiciones]

simulation_strings: [cadenas a simular]
```

## Salida

El simulador muestra:
- Descripción instantánea en cada paso: `(estado, memoria) cinta`
- Posición del cabezal indicada con `^`
- Resultado final: ACEPTADA ✅ o RECHAZADA ❌


