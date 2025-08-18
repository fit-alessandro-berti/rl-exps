import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
activities = ['Data Capture', 'Trend Scan', 'Idea Workshop', 'Concept Draft', 'Expert Review', 'Prototype Build', 'Regulation Check', 'IP Alignment', 'Supply Sync', 'Market Mapping', 'Pilot Launch', 'Feedback Loop', 'Design Iterate', 'Impact Measure', 'Strategy Adapt']
transitions = [Transition(label=activity) for activity in activities]

# Define the workflow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[transitions[0], transitions[1]])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[transitions[2], xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[transitions[3], xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[transitions[4], xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[transitions[5], xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[transitions[6], xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[transitions[7], xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[transitions[8], xor7])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[transitions[9], xor8])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[transitions[10], xor9])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[transitions[11], xor10])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[transitions[12], xor11])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[transitions[13], xor12])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[transitions[14], xor13])
xor15 = OperatorPOWL(operator=Operator.XOR, children=[transitions[15], xor14])

# Define the loop structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor15])

# Define the partial order
root = StrictPartialOrder(nodes=[loop, xor15])
root.order.add_edge(loop, xor15)

# Print the root POWL model
print(root)