import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgery_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check, material_test, style_compare, carbon_dating,
    document_review, provenance_check, digital_imaging, forgery_scan, expert_consult,
    historical_research, panel_review,
    report_draft, final_approval, catalog_entry
])

# Intake -> all tests in parallel
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(artifact_intake, material_test)
root.order.add_edge(artifact_intake, style_compare)
root.order.add_edge(artifact_intake, carbon_dating)

# All tests -> document review
root.order.add_edge(condition_check, document_review)
root.order.add_edge(material_test, document_review)
root.order.add_edge(style_compare, document_review)
root.order.add_edge(carbon_dating, document_review)

# Document review -> provenance check
root.order.add_edge(document_review, provenance_check)

# Provenance check -> digital imaging
root.order.add_edge(provenance_check, digital_imaging)

# Parallel branches from digital imaging
root.order.add_edge(digital_imaging, forgery_scan)
root.order.add_edge(digital_imaging, expert_consult)

# Both forgery scan and expert consult can proceed to historical research
root.order.add_edge(forgery_scan, historical_research)
root.order.add_edge(expert_consult, historical_research)

# Historical research can branch into either panel review or final approval
root.order.add_edge(historical_research, panel_review)
root.order.add_edge(historical_research, final_approval)

# Panel review or final approval can branch into report draft
root.order.add_edge(panel_review, report_draft)
root.order.add_edge(final_approval, report_draft)

# Report draft must be approved before catalog entry
root.order.add_edge(report_draft, final_approval)
root.order.add_edge(report_draft, catalog_entry)

# Final approval must be approved before catalog entry
root.order.add_edge(final_approval, catalog_entry)