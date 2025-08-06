import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.petri.obj import PetriNet, Marking

# Define activities
activities = ['Provenance Check', 'Material Testing', 'Expert Review', 'Legal Verify', 'Risk Assess', 'Insurance Quote', 'Catalog Entry', 'Digital Scan', 'Condition Report', 'Transport Plan', 'Customs Clear', 'Certification', 'Exhibit Setup', 'Owner Notify', 'Final Audit']

# Define transitions
transitions = [Transition(label=activity) for activity in activities]
skip = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[transitions[0], transitions[1], transitions[2], transitions[3]])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[transitions[4], transitions[5], transitions[6]])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[transitions[7], transitions[8], transitions[9], transitions[10]])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[transitions[11], transitions[12], transitions[13]])

# Define XORs
xor1 = OperatorPOWL(operator=Operator.XOR, children=[transitions[14], skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[transitions[15], skip])

# Define root
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, xor1, xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor2)
root.order.add_edge(loop4, xor1)

# Print root
print(root)