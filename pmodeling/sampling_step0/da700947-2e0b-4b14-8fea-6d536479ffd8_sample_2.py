import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A1 = Transition(label='Site Survey')
A2 = Transition(label='Structural Audit')
A3 = Transition(label='Climate Design')
A4 = Transition(label='Lighting Setup')
A5 = Transition(label='Irrigation Plan')
A6 = Transition(label='Nutrient Mix')
A7 = Transition(label='Sensor Install')
A8 = Transition(label='AI Calibration')
A9 = Transition(label='Pest Scan')
A10 = Transition(label='Energy Audit')
A11 = Transition(label='Renewable Sync')
A12 = Transition(label='Data Modeling')
A13 = Transition(label='Staff Briefing')
A14 = Transition(label='Compliance Check')
A15 = Transition(label='Community Meet')
A16 = Transition(label='Yield Review')
A17 = Transition(label='Feedback Loop')

# Define exclusive choices
E1 = OperatorPOWL(operator=Operator.XOR, children=[A1, A2])
E2 = OperatorPOWL(operator=Operator.XOR, children=[A3, A4])
E3 = OperatorPOWL(operator=Operator.XOR, children=[A5, A6])
E4 = OperatorPOWL(operator=Operator.XOR, children=[A7, A8])
E5 = OperatorPOWL(operator=Operator.XOR, children=[A9, A10])
E6 = OperatorPOWL(operator=Operator.XOR, children=[A11, A12])
E7 = OperatorPOWL(operator=Operator.XOR, children=[A13, A14])
E8 = OperatorPOWL(operator=Operator.XOR, children=[A15, A16])
E9 = OperatorPOWL(operator=Operator.XOR, children=[A17])

# Define loops
L1 = OperatorPOWL(operator=Operator.LOOP, children=[A1, A2])
L2 = OperatorPOWL(operator=Operator.LOOP, children=[A3, A4])
L3 = OperatorPOWL(operator=Operator.LOOP, children=[A5, A6])
L4 = OperatorPOWL(operator=Operator.LOOP, children=[A7, A8])
L5 = OperatorPOWL(operator=Operator.LOOP, children=[A9, A10])
L6 = OperatorPOWL(operator=Operator.LOOP, children=[A11, A12])
L7 = OperatorPOWL(operator=Operator.LOOP, children=[A13, A14])
L8 = OperatorPOWL(operator=Operator.LOOP, children=[A15, A16])
L9 = OperatorPOWL(operator=Operator.LOOP, children=[A17])

# Define the root POWL model
root = StrictPartialOrder(nodes=[E1, E2, E3, E4, E5, E6, E7, E8, E9, L1, L2, L3, L4, L5, L6, L7, L8, L9])
root.order.add_edge(E1, L1)
root.order.add_edge(E2, L2)
root.order.add_edge(E3, L3)
root.order.add_edge(E4, L4)
root.order.add_edge(E5, L5)
root.order.add_edge(E6, L6)
root.order.add_edge(E7, L7)
root.order.add_edge(E8, L8)
root.order.add_edge(E9, L9)