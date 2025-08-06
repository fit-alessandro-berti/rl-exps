import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
A1 = Transition(label='Intake Document')
A2 = Transition(label='Visual Inspect')
A3 = Transition(label='Imaging Scan')
A4 = Transition(label='Material Test')
A5 = Transition(label='Database Cross')
A6 = Transition(label='Provenance Check')
A7 = Transition(label='Expert Consult')
A8 = Transition(label='Carbon Dating')
A9 = Transition(label='Forensic Analyze')
A10 = Transition(label='Anomaly Review')
A11 = Transition(label='Risk Assess')
A12 = Transition(label='Report Draft')
A13 = Transition(label='Insurance Quote')
A14 = Transition(label='Storage Plan')
A15 = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[A1, A2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[A3, A4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[A5, A6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[A7, A8])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[A9, A10])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[A11, A12])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[A13, A14])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[A15, skip])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop5, loop6])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop7, loop8])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, A15)