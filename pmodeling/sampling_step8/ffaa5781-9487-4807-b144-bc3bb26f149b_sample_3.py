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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        provenance_check,
        radiocarbon_test,
        material_analysis,
        microscopic_scan,
        expert_review,
        context_validation,
        legal_audit,
        export_verify,
        digital_imaging,
        three_d_modeling,
        consensus_meeting,
        final_approval,
        catalog_entry,
        virtual_setup,
        archival_backup
    ]
)

# Define the dependencies between nodes
root.order.add_edge(provenance_check, radiocarbon_test)
root.order.add_edge(provenance_check, material_analysis)
root.order.add_edge(provenance_check, microscopic_scan)
root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(provenance_check, context_validation)
root.order.add_edge(provenance_check, legal_audit)
root.order.add_edge(provenance_check, export_verify)
root.order.add_edge(provenance_check, digital_imaging)
root.order.add_edge(provenance_check, three_d_modeling)
root.order.add_edge(provenance_check, consensus_meeting)
root.order.add_edge(provenance_check, final_approval)
root.order.add_edge(provenance_check, catalog_entry)
root.order.add_edge(provenance_check, virtual_setup)
root.order.add_edge(provenance_check, archival_backup)