import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define transitions for each activity
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

# Define loops and choices
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
loop_analysis = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, material_analysis, microscopic_scan])
xor_validation = OperatorPOWL(operator=Operator.XOR, children=[expert_review, context_validation, legal_audit, export_verify])
xor_modeling = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, three_d_modeling])
loop_consensus = OperatorPOWL(operator=Operator.LOOP, children=[consensus_meeting])
xor_virtual = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, virtual_setup])
loop_archival = OperatorPOWL(operator=Operator.LOOP, children=[archival_backup])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop_provenance, loop_analysis, xor_validation, xor_modeling, loop_consensus, xor_virtual, loop_archival])
root.order.add_edge(loop_provenance, loop_analysis)
root.order.add_edge(loop_analysis, xor_validation)
root.order.add_edge(xor_validation, xor_modeling)
root.order.add_edge(xor_modeling, loop_consensus)
root.order.add_edge(loop_consensus, xor_virtual)
root.order.add_edge(xor_virtual, loop_archival)