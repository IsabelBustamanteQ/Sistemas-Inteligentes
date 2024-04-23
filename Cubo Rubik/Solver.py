
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
            print(current_state.moves)
            if current_state.is_goal_state():
                print("camino encontrado: ", current_state.moves)
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