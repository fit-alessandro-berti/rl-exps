import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
provenance_check      = Transition(label='Provenance Check')
radiocarbon_test      = Transition(label='Radiocarbon Test')
material_analysis     = Transition(label='Material Analysis')
microscopic_scan      = Transition(label='Microscopic Scan')
expert_review         = Transition(label='Expert Review')
context_validation    = Transition(label='Context Validation')
legal_audit           = Transition(label='Legal Audit')
export_verify         = Transition(label='Export Verify')
digital_imaging       = Transition(label='Digital Imaging')
three_d_modeling      = Transition(label='3D Modeling')
consensus_meeting     = Transition(label='Consensus Meeting')
final_approval        = Transition(label='Final Approval')
catalog_entry         = Transition(label='Catalog Entry')
virtual_setup         = Transition(label='Virtual Setup')
archival_backup       = Transition(label='Archival Backup')

# Loop for expert review and context validation
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert_review, context_validation]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    radiocarbon_test,
    material_analysis,
    microscopic_scan,
    expert_loop,
    legal_audit,
    export_verify,
    digital_imaging,
    three_d_modeling,
    consensus_meeting,
    final_approval,
    catalog_entry,
    virtual_setup,
    archival_backup
])

# Add control-flow edges
root.order.add_edge(provenance_check, radiocarbon_test)
root.order.add_edge(provenance_check, material_analysis)
root.order.add_edge(provenance_check, microscopic_scan)

root.order.add_edge(radiocarbon_test, expert_loop)
root.order.add_edge(material_analysis, expert_loop)
root.order.add_edge(microscopic_scan, expert_loop)

root.order.add_edge(expert_loop, legal_audit)
root.order.add_edge(legal_audit, export_verify)

root.order.add_edge(export_verify, digital_imaging)
root.order.add_edge(export_verify, three_d_modeling)

root.order.add_edge(digital_imaging, consensus_meeting)
root.order.add_edge(three_d_modeling, consensus_meeting)

root.order.add_edge(consensus_meeting, final_approval)
root.order.add_edge(final_approval, catalog_entry)
root.order.add_edge(final_approval, virtual_setup)
root.order.add_edge(final_approval, archival_backup)

# Final edges to ensure all parallel branches complete before archival
root.order.add_edge(digital_imaging, catalog_entry)
root.order.add_edge(three_d_modeling, catalog_entry)
root.order.add_edge(digital_imaging, virtual_setup)
root.order.add_edge(three_d_modeling, virtual_setup)

# Silent transition to ensure all archival tasks complete
skip = SilentTransition()
root.order.add_edge(final_approval, skip)
root.order.add_edge(skip, archival_backup)