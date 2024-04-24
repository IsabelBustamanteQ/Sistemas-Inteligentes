
from queue import PriorityQueue
import copy
import numpy as np
class Solver():
    def __init__(self,cube):
        self.cube=cube
    def heuristic(self,new_cube):
        return new_cube.combined_heuristic()

    def a_star_solve(self):
        open=PriorityQueue()
        closed=set()
        f_initial=self.heuristic(self.cube)
        open.put((f_initial,self.cube))
        while not open.empty():
            current_cost,current_state=open.get()
            closed.add(current_state)
            if current_state.is_goal_state():
                self.instructions_to_solve(current_state.moves)
                return True
            
            for move in current_state.valid_moves():
                new_state=copy.deepcopy(current_state)
                new_state.action(move)
                new_state.add_move(move)
                new_cost=current_cost+self.heuristic(new_state)

                if new_state not in closed:                
                    open.put((new_cost,new_state))
                    closed.add(new_state)
        return False
    def instructions_to_solve(self, moves):
        if len(moves)==0:
            print("El cubo ya está armado")
            return True
        print("SOLUCION ENCONTRADA:")
        number_step=1
        for move in moves:
            match move:
                case "U":
                    step="Arriba Derecha"
                case "U'":
                    step="Arriba Izquierda"
                case "D":
                    step="Abajo Derecha"
                case "D'":
                    step="Abajo Izquierda"
                case "F":
                    step="Frente Derecha"
                case "F'":
                    step="Frente Izquierda"
                case "B":
                    step="Atrás Derecha"
                case "B'":
                    step="Atrás Izquierda"
                case "R":
                    step="Derecha a la Derecha"
                case "R'":
                    step="Derecha a la Izquierda"
                case "L":
                    step="Izquierda a la Derecha"
                case "L'":
                    step="Izquierda a la Izquierda"
            print("Paso ",number_step,": ",step," (",move,")")
            number_step+=1