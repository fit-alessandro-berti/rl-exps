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
forgery_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define silent transitions
skip = SilentTransition()

# Define parallel processes
artifact_intake_and_material_test = OperatorPOWL(operator=Operator.AND, children=[artifact_intake, material_test])
condition_check_and_style_compare = OperatorPOWL(operator=Operator.AND, children=[condition_check, style_compare])
carbon_dating_and_document_review = OperatorPOWL(operator=Operator.AND, children=[carbon_dating, document_review])
provenance_check_and_digital_imaging = OperatorPOWL(operator=Operator.AND, children=[provenance_check, digital_imaging])
forgery_scan_and_expert_consult = OperatorPOWL(operator=Operator.AND, children=[forgery_scan, expert_consult])
historical_research_and_panel_review = OperatorPOWL(operator=Operator.AND, children=[historical_research, panel_review])

# Define loop for expert consultation
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, historical_research])

# Define the root process
root = StrictPartialOrder(nodes=[
    artifact_intake_and_material_test, 
    condition_check_and_style_compare, 
    carbon_dating_and_document_review, 
    provenance_check_and_digital_imaging, 
    forgery_scan_and_expert_consult, 
    expert_consult_loop, 
    report_draft, 
    final_approval, 
    catalog_entry
])

# Define dependencies
root.order.add_edge(artifact_intake_and_material_test, condition_check_and_style_compare)
root.order.add_edge(artifact_intake_and_material_test, carbon_dating_and_document_review)
root.order.add_edge(condition_check_and_style_compare, provenance_check_and_digital_imaging)
root.order.add_edge(carbon_dating_and_document_review, provenance_check_and_digital_imaging)
root.order.add_edge(provenance_check_and_digital_imaging, forgery_scan_and_expert_consult)
root.order.add_edge(forgery_scan_and_expert_consult, expert_consult_loop)
root.order.add_edge(expert_consult_loop, report_draft)
root.order.add_edge(report_draft, final_approval)
root.order.add_edge(final_approval, catalog_entry)