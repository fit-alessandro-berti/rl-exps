import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    provenance_check, radiocarbon_test, material_analysis, microscopic_scan,
    expert_review, context_validation, legal_audit, export_verify,
    digital_imaging, three_d_modeling, consensus_meeting, final_approval,
    catalog_entry, virtual_setup, archival_backup
])

# Define the dependencies between activities
root.order.add_edge(provenance_check, radiocarbon_test)
root.order.add_edge(provenance_check, material_analysis)
root.order.add_edge(radiocarbon_test, microscopic_scan)
root.order.add_edge(material_analysis, microscopic_scan)
root.order.add_edge(microscopic_scan, expert_review)
root.order.add_edge(expert_review, context_validation)
root.order.add_edge(context_validation, legal_audit)
root.order.add_edge(legal_audit, export_verify)
root.order.add_edge(export_verify, digital_imaging)
root.order.add_edge(digital_imaging, three_d_modeling)
root.order.add_edge(three_d_modeling, consensus_meeting)
root.order.add_edge(consensus_meeting, final_approval)
root.order.add_edge(final_approval, catalog_entry)
root.order.add_edge(catalog_entry, virtual_setup)
root.order.add_edge(virtual_setup, archival_backup)

# Print the final result
print(root)