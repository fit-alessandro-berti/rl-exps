import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
discover = Transition(label='Discover Item')
doc_find = Transition(label='Document Find')
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

# Loop for iterative verification and dispute resolution
# A: Initial Survey -> Image Capture -> Material Testing -> Style Compare
A = StrictPartialOrder(nodes=[initial_survey, image_capture, material_testing, style_compare])
A.order.add_edge(initial_survey, image_capture)
A.order.add_edge(image_capture, material_testing)
A.order.add_edge(material_testing, style_compare)

# B: Expert Consult -> Provenance Check -> Ownership Verify -> Legal Review -> Risk Assess -> Conservation Plan
B = StrictPartialOrder(nodes=[expert_consult, provenance_check, ownership_verify, legal_review, risk_assess, conservation_plan])
B.order.add_edge(expert_consult, provenance_check)
B.order.add_edge(provenance_check, ownership_verify)
B.order.add_edge(ownership_verify, legal_review)
B.order.add_edge(legal_review, risk_assess)
B.order.add_edge(risk_assess, conservation_plan)

# Loop: repeat A then either exit or B then A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Exclusive choice: Dispute Resolve or Final Archive
xor = OperatorPOWL(operator=Operator.XOR, children=[dispute_resolve, final_archive])

# Build the root partial order
root = StrictPartialOrder(nodes=[discover, doc_find, loop, xor])
root.order.add_edge(discover, doc_find)
root.order.add_edge(doc_find, loop)
root.order.add_edge(loop, xor)

print(root)