import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.petri_net.obj import PetriNet, Marking

# Define the activities
A1 = Transition(label='Site Survey')
A2 = Transition(label='Design Layout')
A3 = Transition(label='System Assembly')
A4 = Transition(label='Climate Setup')
A5 = Transition(label='Light Calibration')
A6 = Transition(label='Seed Selection')
A7 = Transition(label='Seedling Prep')
A8 = Transition(label='Nutrient Mix')
A9 = Transition(label='Irrigation Setup')
A10 = Transition(label='Sensor Install')
A11 = Transition(label='Data Integration')
A12 = Transition(label='Waste Routing')
A13 = Transition(label='Energy Audit')
A14 = Transition(label='Regulation Check')
A15 = Transition(label='Operational Test')
A16 = Transition(label='Community Outreach')

# Define the partial order
root = StrictPartialOrder(nodes=[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16])

# Define the dependencies between activities
root.order.add_edge(A1, A2)
root.order.add_edge(A2, A3)
root.order.add_edge(A3, A4)
root.order.add_edge(A4, A5)
root.order.add_edge(A5, A6)
root.order.add_edge(A6, A7)
root.order.add_edge(A7, A8)
root.order.add_edge(A8, A9)
root.order.add_edge(A9, A10)
root.order.add_edge(A10, A11)
root.order.add_edge(A11, A12)
root.order.add_edge(A12, A13)
root.order.add_edge(A13, A14)
root.order.add_edge(A14, A15)
root.order.add_edge(A15, A16)

# Define the markings
initial_marking = Marking()
final_marking = Marking({A16: 1})

# Print the model
print(root)