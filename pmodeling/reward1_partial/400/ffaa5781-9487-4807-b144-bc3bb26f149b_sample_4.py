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

# Provenance Check --> Radiocarbon Test --> Material Analysis --> Microscopic Scan --> Expert Review --> Context Validation --> Legal Audit --> Export Verify
provenance_check_to_radiocarbon = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, skip])
radiocarbon_to_material = OperatorPOWL(operator=Operator.XOR, children=[material_analysis, skip])
material_to_microscopic = OperatorPOWL(operator=Operator.XOR, children=[microscopic_scan, skip])
microscopic_to_expert = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
expert_to_context = OperatorPOWL(operator=Operator.XOR, children=[context_validation, skip])
context_to_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])
legal_to_export = OperatorPOWL(operator=Operator.XOR, children=[export_verify, skip])

# Export Verify --> Digital Imaging --> 3D Modeling --> Consensus Meeting --> Final Approval
export_to_digital = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, skip])
digital_to_3d = OperatorPOWL(operator=Operator.XOR, children=[three_d_modeling, skip])
three_d_to_consensus = OperatorPOWL(operator=Operator.XOR, children=[consensus_meeting, skip])
consensus_to_final = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Consensus Meeting --> Catalog Entry --> Virtual Setup --> Archival Backup
consensus_to_catalog = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, skip])
catalog_to_virtual = OperatorPOWL(operator=Operator.XOR, children=[virtual_setup, skip])
virtual_to_archival = OperatorPOWL(operator=Operator.XOR, children=[archival_backup, skip])

# Define the workflow
root = StrictPartialOrder(nodes=[
    provenance_check_to_radiocarbon,
    radiocarbon_to_material,
    material_to_microscopic,
    microscopic_to_expert,
    expert_to_context,
    context_to_legal,
    legal_to_export,
    export_to_digital,
    digital_to_3d,
    three_d_to_consensus,
    consensus_to_final,
    consensus_to_catalog,
    catalog_to_virtual,
    virtual_to_archival
])

# Define the dependencies
root.order.add_edge(provenance_check, provenance_check_to_radiocarbon)
root.order.add_edge(radiocarbon_test, radiocarbon_to_material)
root.order.add_edge(material_analysis, material_to_microscopic)
root.order.add_edge(microscopic_scan, microscopic_to_expert)
root.order.add_edge(expert_review, expert_to_context)
root.order.add_edge(context_validation, context_to_legal)
root.order.add_edge(legal_audit, legal_to_export)
root.order.add_edge(export_verify, export_to_digital)
root.order.add_edge(digital_imaging, digital_to_3d)
root.order.add_edge(three_d_modeling, three_d_to_consensus)
root.order.add_edge(consensus_meeting, consensus_to_final)
root.order.add_edge(consensus_meeting, consensus_to_catalog)
root.order.add_edge(catalog_entry, catalog_to_virtual)
root.order.add_edge(virtual_setup, virtual_to_archival)

print(root)