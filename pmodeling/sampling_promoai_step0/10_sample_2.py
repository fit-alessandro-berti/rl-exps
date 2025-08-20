import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
A = Transition(label='Assess compatibility')
B = Transition(label='Evaluate cost and resource needs')
C = Transition(label='Install the solution')
D = Transition(label='Procure necessary tools or licenses')
E = Transition(label='Provide support for troubleshooting')
F = Transition(label='Provide training')
G = Transition(label='Roll out solution to requesting department')
H = Transition(label='Test solution')
I = Transition(label='Submit IT solution request')

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        A, B, C, D, E, F, G, H, I
    ],
    order={
        (I, A): 1,
        (A, B): 1,
        (B, C): 1,
        (C, D): 1,
        (D, H): 1,
        (H, E): 1,
        (H, F): 1,
        (H, G): 1,
        (H, I): 1,
        (E, H): 1,
        (F, H): 1,
        (G, H): 1,
    }
)

print(root)