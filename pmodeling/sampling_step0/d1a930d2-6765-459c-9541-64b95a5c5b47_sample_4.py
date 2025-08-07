from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define process tree
# Initial Artifact Intake
artifact_intake_tree = StrictPartialOrder(nodes=[artifact_intake])

# Condition Check and Material Test
condition_check_tree = StrictPartialOrder(nodes=[condition_check, material_test])
condition_check_tree.order.add_edge(condition_check, material_test)

# Style Compare and Carbon Dating
style_compare_tree = StrictPartialOrder(nodes=[style_compare, carbon_dating])
style_compare_tree.order.add_edge(style_compare, carbon_dating)

# Document Review and Provenance Check
document_review_tree = StrictPartialOrder(nodes=[document_review, provenance_check])
document_review_tree.order.add_edge(document_review, provenance_check)

# Digital Imaging and Forgeries Scan
digital_imaging_tree = StrictPartialOrder(nodes=[digital_imaging, forgeries_scan])
digital_imaging_tree.order.add_edge(digital_imaging, forgeries_scan)

# Expert Consult and Historical Research
expert_consult_tree = StrictPartialOrder(nodes=[expert_consult, historical_research])
expert_consult_tree.order.add_edge(expert_consult, historical_research)

# Panel Review
panel_review_tree = StrictPartialOrder(nodes=[panel_review])

# Report Draft and Final Approval
report_draft_tree = StrictPartialOrder(nodes=[report_draft, final_approval])
report_draft_tree.order.add_edge(report_draft, final_approval)

# Catalog Entry
catalog_entry_tree = StrictPartialOrder(nodes=[catalog_entry])

# Define parallel activities
parallel_activities = StrictPartialOrder(nodes=[document_review_tree, provenance_check_tree, digital_imaging_tree])

# Define sequential activities
sequential_activities = StrictPartialOrder(nodes=[condition_check_tree, material_test_tree, style_compare_tree, carbon_dating_tree])

# Define the root
root = StrictPartialOrder(nodes=[artifact_intake_tree, parallel_activities, sequential_activities, report_draft_tree, panel_review_tree, final_approval_tree, catalog_entry_tree])