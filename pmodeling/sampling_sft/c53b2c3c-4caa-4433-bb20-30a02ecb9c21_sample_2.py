import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
discover_item = Transition(label='Discover Item')
document_find = Transition(label='Document Find')
initial_survey = Transition(label='Initial Survey')
image_capture = Transition(label='Image Capture')
material_testing = Transition(label='Material Testing')
style_compare = Transition(label='Style Compare')
expert_consult = Transition(label='Expert Consult')
provenance_check = Transition(label='Provenance Check')
ownership_verify = Transition(label='Ownership Verify')
legal_review = Transition(label='Legal Review')
risk_assess = Transition(label='Risk Assess')
conservation_plan = Transition(label='Conservation Plan')
certification = Transition(label='Certification')
secure_transfer = Transition(label='Secure Transfer')
dispute_resolve = Transition(label='Dispute Resolve')
final_archive = Transition(label='Final Archive')

# Build the iterative verification loop:
#   1. Image Capture
#   2. Material Testing
#   3. Style Compare
#   4. Expert Consult
#   5. Provenance Check
#   6. Ownership Verify
#   7. Legal Review
#   8. Risk Assess
#   9. Conservation Plan
#  10. Certification
#  11. Secure Transfer
#  12. Dispute Resolve (optional)
#  13. Final Archive
loop_body = StrictPartialOrder(nodes=[
    image_capture,
    material_testing,
    style_compare,
    expert_consult,
    provenance_check,
    ownership_verify,
    legal_review,
    risk_assess,
    conservation_plan,
    certification,
    secure_transfer
])
loop_body.order.add_edge(image_capture, material_testing)
loop_body.order.add_edge(material_testing, style_compare)
loop_body.order.add_edge(style_compare, expert_consult)
loop_body.order.add_edge(expert_consult, provenance_check)
loop_body.order.add_edge(provenance_check, ownership_verify)
loop_body.order.add_edge(ownership_verify, legal_review)
loop_body.order.add_edge(legal_review, risk_assess)
loop_body.order.add_edge(risk_assess, conservation_plan)
loop_body.order.add_edge(conservation_plan, certification)
loop_body.order.add_edge(certification, secure_transfer)

loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, dispute_resolve])

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    discover_item,
    document_find,
    initial_survey,
    loop,
    final_archive
])
root.order.add_edge(discover_item, document_find)
root.order.add_edge(document_find, initial_survey)
root.order.add_edge(initial_survey, loop)
root.order.add_edge(loop, final_archive)