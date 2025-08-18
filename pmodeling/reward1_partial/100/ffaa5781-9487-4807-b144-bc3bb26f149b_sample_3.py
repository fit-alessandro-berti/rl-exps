from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, material_analysis, microscopic_scan])
xor = OperatorPOWL(operator=Operator.XOR, children=[expert_review, context_validation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, export_verify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, three_d_modeling])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, final_approval])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, virtual_setup, archival_backup])

# Define the partial order
root = StrictPartialOrder(nodes=[provenance_check, loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(provenance_check, loop)
root.order.add_edge(provenance_check, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, final_approval)
root.order.add_edge(xor5, virtual_setup)
root.order.add_edge(xor5, archival_backup)