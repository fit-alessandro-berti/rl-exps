import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
provenance_check = Transition(label='Provenance Check')
material_test = Transition(label='Material Test')
archive_search = Transition(label='Archive Search')
expert_review = Transition(label='Expert Review')
three_d_scanning = Transition(label='3D Scanning')
wear_analysis = Transition(label='Wear Analysis')
database_cross = Transition(label='Database Cross')
law_consult = Transition(label='Law Consult')
forgeries_detect = Transition(label='Forgery Detect')
certification = Transition(label='Certification')
document_prep = Transition(label='Document Prep')
client_brief = Transition(label='Client Brief')
secure_storage = Transition(label='Secure Storage')
risk_assessment = Transition(label='Risk Assessment')
final_approval = Transition(label='Final Approval')

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_test])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[three_d_scanning, wear_analysis])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[database_cross, law_consult])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[forgeries_detect, certification])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[document_prep, client_brief])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[secure_storage, risk_assessment])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, xor1])

# Define the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor2, xor3, xor4, xor5, xor6, xor7])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, loop])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)
root.order.add_edge(loop, xor8)

# Print the POWL model
print(root)