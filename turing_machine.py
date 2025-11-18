# turing_machine.py

from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple


@dataclass
class Transition:
    initial_state: str
    mem_in: Optional[str]
    tape_in: Optional[str]
    final_state: str
    mem_out: Optional[str]
    tape_out: Optional[str]
    move: str  # 'L', 'R' o 'S'


class TuringMachine:
    def __init__(
        self,
        states: List[str],
        initial_state: str,
        final_state: str,
        tape_alphabet: List[Optional[str]],
        transitions: List[Transition],
    ) -> None:
        self.states = states
        self.initial_state = initial_state
        self.final_state = final_state
        self.tape_alphabet = tape_alphabet

        # Guardamos blank como el primer símbolo None que aparezca, o None por defecto
        self.blank = None
        for sym in tape_alphabet:
            if sym is None:
                self.blank = None
                break

        # Tabla de transición: (estado, mem, tape) -> Transition
        self.delta: Dict[Tuple[str, Optional[str], Optional[str]], Transition] = {}

        for t in transitions:
            key = (t.initial_state, t.mem_in, t.tape_in)
            self.delta[key] = t

        # Estado de ejecución
        self.reset()

    def reset(self) -> None:
        self.current_state: str = self.initial_state
        self.memory: Optional[str] = None
        self.head: int = 0
        self.tape: List[Optional[str]] = []

    def load_tape(self, input_string: str) -> None:
        # Cada carácter de la cadena va como símbolo en la cinta
        self.tape = list(input_string)
        self.head = 0
        self.memory = None

    def _read_symbol(self) -> Optional[str]:
        if self.head < 0:
            # Forzamos cabeza mínima en 0
            self.head = 0
        if self.head >= len(self.tape):
            return self.blank
        return self.tape[self.head]

    def _write_symbol(self, sym: Optional[str]) -> None:
        if self.head < 0:
            self.head = 0
        # Expandimos cinta a la derecha si hace falta
        if self.head >= len(self.tape):
            self.tape.extend([self.blank] * (self.head - len(self.tape) + 1))
        self.tape[self.head] = sym

    def _get_transition(self) -> Optional[Transition]:
        tape_sym = self._read_symbol()
        key = (self.current_state, self.memory, tape_sym)
        return self.delta.get(key, None)

    def _tape_to_string(self) -> str:
        # Representamos blanks como '□' para debug
        return "".join(sym if sym is not None else "□" for sym in self.tape)

    def print_id(self) -> None:
        """
        Imprime la Descripción Instantánea (ID):
        (estado, memoria) cinta
                       ^
        """
        tape_str = self._tape_to_string()
        pointer = " " * self.head + "^"
        print(f"({self.current_state}, {self.memory})  {tape_str}")
        print(pointer)
        print()

    def step(self) -> bool:
        """
        Ejecuta un paso de la MT.
        Retorna False si no hay transición aplicable (se detiene).
        """
        t = self._get_transition()
        if t is None:
            return False

        # Escribir en cinta
        self._write_symbol(t.tape_out)

        # Actualizar estado y memoria
        self.current_state = t.final_state
        self.memory = t.mem_out

        # Mover cabeza
        if t.move == "R":
            self.head += 1
        elif t.move == "L":
            self.head -= 1
            if self.head < 0:
                self.head = 0
        # Si es 'S', no se mueve

        return True

    def run(self, input_string: str, max_steps: int = 10_000) -> bool:
        """
        Corre la MT sobre la cadena dada.
        Imprime todas las IDs.
        Retorna True si termina en estado de aceptación, False en caso contrario.
        """
        self.reset()
        self.load_tape(input_string)

        print("===================================")
        print(f"Simulando entrada: {input_string}")
        print("===================================\n")

        self.print_id()

        steps = 0
        while steps < max_steps:
            if not self.step():
                break
            self.print_id()
            steps += 1

        if self.current_state == self.final_state:
            print("Resultado: ACEPTADA ✅\n")
            return True
        else:
            print("Resultado: RECHAZADA ❌\n")
            return False
