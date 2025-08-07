import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
artifact_intake      = Transition(label='Artifact Intake')
condition_check      = Transition(label='Condition Check')
material_test        = Transition(label='Material Test')
style_compare        = Transition(label='Style Compare')
carbon_dating        = Transition(label='Carbon Dating')
document_review      = Transition(label='Document Review')
provenance_check     = Transition(label='Provenance Check')
digital_imaging      = Transition(label='Digital Imaging')
forgery_scan         = Transition(label='Forgery Scan')
expert_consult       = Transition(label='Expert Consult')
historical_research  = Transition(label='Historical Research')
panel_review         = Transition(label='Panel Review')
report_draft         = Transition(label='Report Draft')
final_approval       = Transition(label='Final Approval')
catalog_entry        = Transition(label='Catalog Entry')

# Build the partial order for the verification steps
verify_po = StrictPartialOrder(nodes=[
    condition_check, material_test, style_compare, carbon_dating,
    document_review, provenance_check, digital_imaging, forgery_scan,
    expert_consult, historical_research, panel_review, report_draft,
    final_approval
])

# Define the control-flow dependencies
verify_po.order.add_edge(artifact_intake, condition_check)
verify_po.order.add_edge(condition_check, material_test)
verify_po.order.add_edge(condition_check, style_compare)
verify_po.order.add_edge(condition_check, carbon_dating)
verify_po.order.add_edge(material_test, document_review)
verify_po.order.add_edge(style_compare, document_review)
verify_po.order.add_edge(carbon_dating, document_review)
verify_po.order.add_edge(document_review, provenance_check)
verify_po.order.add_edge(document_review, digital_imaging)
verify_po.order.add_edge(document_review, forgery_scan)
verify_po.order.add_edge(provenance_check, expert_consult)
verify_po.order.add_edge(provenance_check, historical_research)
verify_po.order.add_edge(digital_imaging, expert_consult)
verify_po.order.add_edge(forgery_scan, expert_consult)
verify_po.order.add_edge(historical_research, expert_consult)
verify_po.order.add_edge(expert_consult, panel_review)
verify_po.order.add_edge(panel_review, report_draft)
verify_po.order.add_edge(report_draft, final_approval)
verify_po.order.add_edge(final_approval, catalog_entry)

# Final root partial order
root = verify_po