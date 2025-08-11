import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the silent transitions (tau labels)
skip = SilentTransition()

# Define the process tree for the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    provenance_check,
    material_scan,
    context_review,
    expert_consult,
    image_capture,
    condition_test,
    forger_risk,
    registry_crosscheck,
    legal_verify,
    ethics_review
])
xor = OperatorPOWL(operator=Operator.XOR, children=[
    report_draft,
    certificate_issue,
    skip
])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root of the process
print(root)