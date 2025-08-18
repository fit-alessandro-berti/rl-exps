from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the process flow
artifact_intake_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_check, material_test, style_compare, carbon_dating])
provenance_check_choice = OperatorPOWL(operator=Operator.XOR, children=[document_review, provenance_check])
digital_imaging_choice = OperatorPOWL(operator=Operator.XOR, children=[forgery_scan, digital_imaging])
expert_consult_choice = OperatorPOWL(operator=Operator.XOR, children=[historical_research, expert_consult])
panel_review_choice = OperatorPOWL(operator=Operator.XOR, children=[panel_review])
report_draft_choice = OperatorPOWL(operator=Operator.XOR, children=[report_draft])
final_approval_choice = OperatorPOWL(operator=Operator.XOR, children=[final_approval])
catalog_entry_choice = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry])

# Define the loop for the expert consultation
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult_choice, historical_research])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check_choice, digital_imaging_choice, expert_consult_loop, panel_review_choice, report_draft_choice, final_approval_choice, catalog_entry_choice])
root.order.add_edge(artifact_intake, provenance_check_choice)
root.order.add_edge(artifact_intake, digital_imaging_choice)
root.order.add_edge(provenance_check_choice, panel_review_choice)
root.order.add_edge(digital_imaging_choice, report_draft_choice)
root.order.add_edge(expert_consult_loop, report_draft_choice)
root.order.add_edge(report_draft_choice, final_approval_choice)
root.order.add_edge(final_approval_choice, catalog_entry_choice)

# Print the root POWL model
print(root)