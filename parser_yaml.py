# parser_yaml.py

from typing import Tuple, List, Optional
import yaml

from turing_machine import TuringMachine, Transition


def load_mt_from_yaml(path: str) -> Tuple[TuringMachine, List[str]]:
    """
    Carga una Máquina de Turing y las cadenas a simular
    desde un archivo YAML con la estructura dada en el enunciado.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Estados
    q_states = data["q_states"]["q_list"]
    initial = data["q_states"]["initial"]
    final = data["q_states"]["final"]

    # Alfabeto de la cinta (puede contener None / blank)
    tape_alphabet_raw = data["tape_alphabet"]
    tape_alphabet: List[Optional[str]] = []
    for sym in tape_alphabet_raw:
        # Si viene vacío en YAML, es None
        tape_alphabet.append(sym)

    # Transiciones
    transitions: List[Transition] = []
    for item in data["delta"]:
        params = item["params"]
        out = item["output"]

        t = Transition(
            initial_state=str(params["initial_state"]),
            mem_in=params.get("mem_cache_value", None),
            tape_in=params.get("tape_input", None),
            final_state=str(out["final_state"]),
            mem_out=out.get("mem_cache_value", None),
            tape_out=out.get("tape_output", None),
            move=str(out["tape_displacement"]),
        )
        transitions.append(t)

    tm = TuringMachine(
        states=q_states,
        initial_state=initial,
        final_state=final,
        tape_alphabet=tape_alphabet,
        transitions=transitions,
    )

    simulation_strings = data.get("simulation_strings", [])

    return tm, simulation_strings
