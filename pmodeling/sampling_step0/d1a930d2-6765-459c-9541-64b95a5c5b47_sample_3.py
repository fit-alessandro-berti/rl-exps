import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgeriescan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define the silent transition
skip = SilentTransition()

# Define the POWL model
loop_artifact_intake = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, condition_check, material_test, style_compare, carbon_dating])
loop_document_review = OperatorPOWL(operator=Operator.LOOP, children=[document_review, provenance_check, digital_imaging, forgeriescan, expert_consult])
xor_artifact_intake = OperatorPOWL(operator=Operator.XOR, children=[loop_artifact_intake, loop_document_review])
xor_historical_research = OperatorPOWL(operator=Operator.XOR, children=[historical_research, xor_artifact_intake])
xor_panel_review = OperatorPOWL(operator=Operator.XOR, children=[panel_review, xor_historical_research])
xor_final_approval = OperatorPOWL(operator=Operator.XOR, children=[final_approval, xor_panel_review])
xor_catalog_entry = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, xor_final_approval])

# Set the root
root = xor_catalog_entry

# Print the root
print(root)