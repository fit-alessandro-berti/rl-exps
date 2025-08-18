import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow operators
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, export_verify])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, context_validation])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, material_analysis, microscopic_scan])
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_1, exclusive_choice_2, exclusive_choice_3])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, three_d_modeling])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, final_approval])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, virtual_setup])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[archival_backup])

# Define the root node
root = StrictPartialOrder(nodes=[provenance_check, loop_1, exclusive_choice_4, exclusive_choice_5, exclusive_choice_6, exclusive_choice_7])
root.order.add_edge(provenance_check, loop_1)
root.order.add_edge(loop_1, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)