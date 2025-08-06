import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define loops and choices
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, material_analysis, microscopic_scan])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[legal_audit, export_verify, digital_imaging, three_d_modeling])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, context_validation])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, final_approval])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, virtual_setup])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[archival_backup, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[provenance_check, loop_1, xor_1, loop_2, xor_2, xor_3, xor_4])
root.order.add_edge(provenance_check, loop_1)
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(xor_1, loop_2)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, skip)