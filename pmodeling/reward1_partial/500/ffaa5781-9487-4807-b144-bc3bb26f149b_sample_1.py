import pm4py
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

# Define the loop for scientific analysis
analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, material_analysis, microscopic_scan])

# Define the exclusive choice for expert consultations
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_review, SilentTransition()])

# Define the exclusive choice for legal audits
legal_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, SilentTransition()])

# Define the exclusive choice for export verification
export_choice = OperatorPOWL(operator=Operator.XOR, children=[export_verify, SilentTransition()])

# Define the exclusive choice for digital imaging and 3D modeling
imaging_choice = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, three_d_modeling])

# Define the exclusive choice for consensus meeting
consensus_choice = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, SilentTransition()])

# Define the exclusive choice for final approval
approval_choice = OperatorPOWL(operator=Operator.XOR, children=[final_approval, SilentTransition()])

# Define the exclusive choice for catalog entry
catalog_choice = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, SilentTransition()])

# Define the exclusive choice for virtual setup
virtual_choice = OperatorPOWL(operator=Operator.XOR, children=[virtual_setup, SilentTransition()])

# Define the exclusive choice for archival backup
backup_choice = OperatorPOWL(operator=Operator.XOR, children=[archival_backup, SilentTransition()])

# Define the strict partial order
root = StrictPartialOrder(nodes=[provenance_check, analysis_loop, expert_choice, legal_choice, export_choice, imaging_choice, consensus_choice, approval_choice, catalog_choice, virtual_choice, backup_choice])

# Define the dependencies
root.order.add_edge(provenance_check, analysis_loop)
root.order.add_edge(analysis_loop, expert_choice)
root.order.add_edge(expert_choice, legal_choice)
root.order.add_edge(legal_choice, export_choice)
root.order.add_edge(export_choice, imaging_choice)
root.order.add_edge(imaging_choice, consensus_choice)
root.order.add_edge(consensus_choice, approval_choice)
root.order.add_edge(approval_choice, catalog_choice)
root.order.add_edge(catalog_choice, virtual_choice)
root.order.add_edge(virtual_choice, backup_choice)

# Print the POWL model
print(root)