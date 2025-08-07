import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
discover = Transition(label='Discover Item')
doc_find = Transition(label='Document Find')
initial = Transition(label='Initial Survey')
image_cap = Transition(label='Image Capture')
material_test = Transition(label='Material Testing')
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

# Build the partial order
root = StrictPartialOrder(nodes=[
    discover,
    doc_find,
    initial,
    image_cap,
    material_test,
    style_compare,
    expert_consult,
    provenance_check,
    ownership_verify,
    legal_review,
    risk_assess,
    conservation_plan,
    certification,
    secure_transfer,
    dispute_resolve,
    final_archive
])

# Sequence: Discover -> Document Find -> Initial Survey -> Image Capture -> Material Testing -> Style Compare
root.order.add_edge(discover, doc_find)
root.order.add_edge(doc_find, initial)
root.order.add_edge(initial, image_cap)
root.order.add_edge(image_cap, material_test)
root.order.add_edge(material_test, style_compare)

# Expert consultation is optional after style compare
root.order.add_edge(style_compare, expert_consult)

# After expert consultation, provenance and ownership checks can occur in parallel
root.order.add_edge(expert_consult, provenance_check)
root.order.add_edge(expert_consult, ownership_verify)

# Parallel: provenance and ownership checks, then legal review, risk assessment, and conservation plan
root.order.add_edge(provenance_check, legal_review)
root.order.add_edge(ownership_verify, legal_review)
root.order.add_edge(provenance_check, risk_assess)
root.order.add_edge(ownership_verify, risk_assess)
root.order.add_edge(provenance_check, conservation_plan)
root.order.add_edge(ownership_verify, conservation_plan)

# After all reviews, either dispute resolution or direct certification and transfer
dispute_choice = OperatorPOWL(operator=Operator.XOR, children=[dispute_resolve, None])
root.order.add_edge(legal_review, dispute_choice)
root.order.add_edge(risk_assess, dispute_choice)
root.order.add_edge(conservation_plan, dispute_choice)

# Final choices: either dispute resolution or direct certification and transfer
root.order.add_edge(dispute_choice, certification)
root.order.add_edge(dispute_choice, secure_transfer)

# Always archive the final result
root.order.add_edge(certification, final_archive)
root.order.add_edge(secure_transfer, final_archive)

# Example loop for iterative risk assessment (not shown here)
# loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, None])
# root.order.add_edge(dispute_choice, loop)
# root.order.add_edge(loop, final_archive)