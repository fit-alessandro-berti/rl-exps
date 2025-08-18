import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgeries_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define silent transitions
skip = SilentTransition()

# Define the process tree structure
artifact_intake_node = OperatorPOWL(operator=Operator.LEAF, children=[artifact_intake])
condition_check_node = OperatorPOWL(operator=Operator.LEAF, children=[condition_check])
material_test_node = OperatorPOWL(operator=Operator.LEAF, children=[material_test])
style_compare_node = OperatorPOWL(operator=Operator.LEAF, children=[style_compare])
carbon_dating_node = OperatorPOWL(operator=Operator.LEAF, children=[carbon_dating])
document_review_node = OperatorPOWL(operator=Operator.LEAF, children=[document_review])
provenance_check_node = OperatorPOWL(operator=Operator.LEAF, children=[provenance_check])
digital_imaging_node = OperatorPOWL(operator=Operator.LEAF, children=[digital_imaging])
forgeries_scan_node = OperatorPOWL(operator=Operator.LEAF, children=[forgeries_scan])
expert_consult_node = OperatorPOWL(operator=Operator.LEAF, children=[expert_consult])
historical_research_node = OperatorPOWL(operator=Operator.LEAF, children=[historical_research])
panel_review_node = OperatorPOWL(operator=Operator.LEAF, children=[panel_review])
report_draft_node = OperatorPOWL(operator=Operator.LEAF, children=[report_draft])
final_approval_node = OperatorPOWL(operator=Operator.LEAF, children=[final_approval])
catalog_entry_node = OperatorPOWL(operator=Operator.LEAF, children=[catalog_entry])

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake_node,
    condition_check_node,
    material_test_node,
    style_compare_node,
    carbon_dating_node,
    document_review_node,
    provenance_check_node,
    digital_imaging_node,
    forgeries_scan_node,
    expert_consult_node,
    historical_research_node,
    panel_review_node,
    report_draft_node,
    final_approval_node,
    catalog_entry_node
])

# Define dependencies
root.order.add_edge(artifact_intake_node, condition_check_node)
root.order.add_edge(artifact_intake_node, material_test_node)
root.order.add_edge(artifact_intake_node, style_compare_node)
root.order.add_edge(artifact_intake_node, carbon_dating_node)
root.order.add_edge(artifact_intake_node, document_review_node)
root.order.add_edge(artifact_intake_node, provenance_check_node)
root.order.add_edge(artifact_intake_node, digital_imaging_node)
root.order.add_edge(artifact_intake_node, forgeries_scan_node)
root.order.add_edge(artifact_intake_node, expert_consult_node)
root.order.add_edge(artifact_intake_node, historical_research_node)
root.order.add_edge(artifact_intake_node, panel_review_node)
root.order.add_edge(artifact_intake_node, report_draft_node)
root.order.add_edge(artifact_intake_node, final_approval_node)
root.order.add_edge(artifact_intake_node, catalog_entry_node)

# Print the root model
print(root)