import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
discover = Transition(label='Discover Item')
doc_find = Transition(label='Document Find')
initial = Transition(label='Initial Survey')
image = Transition(label='Image Capture')
material = Transition(label='Material Testing')
style = Transition(label='Style Compare')
expert = Transition(label='Expert Consult')
provenance = Transition(label='Provenance Check')
ownership = Transition(label='Ownership Verify')
legal = Transition(label='Legal Review')
risk = Transition(label='Risk Assess')
conservation = Transition(label='Conservation Plan')
certify = Transition(label='Certification')
secure = Transition(label='Secure Transfer')
dispute = Transition(label='Dispute Resolve')
archive = Transition(label='Final Archive')

# Build the loop body: Risk Assess -> Conservation Plan
loop_body = StrictPartialOrder(nodes=[risk, conservation])
loop_body.order.add_edge(risk, conservation)

# Build the loop: repeat Dispute Resolve and Final Archive until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[dispute, archive])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    discover, doc_find, initial, image, material, style, expert,
    provenance, ownership, legal, loop_body, loop,
    certify, secure
])

# Initial survey precedes all imaging and testing
root.order.add_edge(initial, image)
root.order.add_edge(initial, material)
root.order.add_edge(initial, style)
root.order.add_edge(initial, expert)

# Image and testing precede provenance and ownership
root.order.add_edge(image, provenance)
root.order.add_edge(material, provenance)
root.order.add_edge(style, provenance)
root.order.add_edge(expert, provenance)
root.order.add_edge(provenance, ownership)

# Legal review follows provenance and ownership
root.order.add_edge(provenance, legal)
root.order.add_edge(ownership, legal)

# Conservation plan is inside the risk-assessment loop
root.order.add_edge(loop_body, loop)

# Certify and secure transfer are after the loop
root.order.add_edge(loop, certify)
root.order.add_edge(certify, secure)

# Final archive is triggered after certification
root.order.add_edge(secure, archive)

print(root)