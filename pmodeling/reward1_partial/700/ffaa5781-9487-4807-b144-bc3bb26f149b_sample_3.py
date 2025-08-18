import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, radiocarbon_test, material_analysis, microscopic_scan])
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, context_validation, legal_audit, export_verify])
digital_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_imaging, three_d_modeling])
virtual_loop = OperatorPOWL(operator=Operator.LOOP, children=[consensus_meeting, final_approval, catalog_entry, virtual_setup, archival_backup])

root = StrictPartialOrder(nodes=[provenance_loop, expert_loop, digital_loop, virtual_loop])
root.order.add_edge(provenance_loop, expert_loop)
root.order.add_edge(provenance_loop, digital_loop)
root.order.add_edge(provenance_loop, virtual_loop)
root.order.add_edge(expert_loop, digital_loop)
root.order.add_edge(expert_loop, virtual_loop)
root.order.add_edge(digital_loop, virtual_loop)