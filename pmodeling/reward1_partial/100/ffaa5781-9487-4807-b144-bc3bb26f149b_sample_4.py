import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
provenance_check = Transition(label='Provenance Check')
radiocarbon_test = Transition(label='Radiocarbon Test')
material_analysis = Transition(label='Material Analysis')
microscopic_scan = Transition(label='Microscopic Scan')
expert_review = Transition(label='Expert Review')
context_validation = Transition(label='Context Validation')
legal_audit = Transition(label='Legal Audit')
export_verify = Transition(label='Export Verify')
digital_imaging = Transition(label='Digital Imaging')
three_d_modeling = Transition(label='3D Modeling')
consensus_meeting = Transition(label='Consensus Meeting')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')
virtual_setup = Transition(label='Virtual Setup')
archival_backup = Transition(label='Archival Backup')

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, export_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[context_validation, expert_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[three_d_modeling, digital_imaging])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, material_analysis, microscopic_scan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[consensus_meeting, final_approval])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, virtual_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[archival_backup, provenance_check])

# Define the POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, loop1, loop2, xor4, xor5])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, loop1)
root.order.add_edge(xor3, loop1)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(xor4, xor5)

print(root)