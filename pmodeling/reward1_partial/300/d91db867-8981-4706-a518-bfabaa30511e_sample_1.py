import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
context_review = Transition(label='Context Review')
expert_consult = Transition(label='Expert Consult')
image_capture = Transition(label='Image Capture')
condition_test = Transition(label='Condition Test')
forger_risk = Transition(label='Forgery Risk')
registry_crosscheck = Transition(label='Registry Crosscheck')
legal_verify = Transition(label='Legal Verify')
ethics_review = Transition(label='Ethics Review')
report_draft = Transition(label='Report Draft')
certificate_issue = Transition(label='Certificate Issue')
digital_archive = Transition(label='Digital Archive')
transfer_setup = Transition(label='Transfer Setup')
final_approval = Transition(label='Final Approval')

# Define the loop for each artifact
artifact_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    provenance_check, material_scan, context_review, expert_consult,
    image_capture, condition_test, forger_risk, registry_crosscheck,
    legal_verify, ethics_review, report_draft, certificate_issue, digital_archive,
    transfer_setup, final_approval
])

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_loop])
root.order.add_edge(artifact_loop, artifact_loop)

# Print the final POWL model
print(root)