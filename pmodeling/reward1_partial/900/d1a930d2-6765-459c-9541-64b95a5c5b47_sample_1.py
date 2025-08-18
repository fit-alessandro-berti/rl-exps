import pm4py
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
forgery_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define silent transitions (if any, in this case none)

# Define partial order
root = StrictPartialOrder(nodes=[
    artifact_intake, condition_check, material_test, style_compare, carbon_dating,
    document_review, provenance_check, digital_imaging, forgery_scan, expert_consult,
    historical_research, panel_review, report_draft, final_approval, catalog_entry
])

# Define dependencies (if any, in this case none)

# Save the final result in the variable 'root'