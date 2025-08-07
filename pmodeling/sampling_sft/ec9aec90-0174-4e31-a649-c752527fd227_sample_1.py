import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
assess = Transition(label='Assess Artifact')
verify = Transition(label='Verify Provenance')
analyze = Transition(label='Analyze Condition')
plan = Transition(label='Plan Conservation')
clean = Transition(label='Clean Surface')
stabilize = Transition(label='Stabilize Structure')
source = Transition(label='Source Materials')
fabricate = Transition(label='Fabricate Parts')
repairs = Transition(label='Perform Repairs')
patina = Transition(label='Apply Patina')
colors = Transition(label='Match Colors')
document = Transition(label='Document Process')
review = Transition(label='Review Quality')
approve = Transition(label='Obtain Approval')
package = Transition(label='Package Securely')
transport = Transition(label='Arrange Transport')

# Silent transition for optional fabricate -> repairs
skip = SilentTransition()

# Optional fabrication loop: fabricate, then either exit or perform repairs
fabric_loop = OperatorPOWL(operator=Operator.LOOP, children=[fabricate, skip])

# Choice of applying either patina or colors
patina_xor = OperatorPOWL(operator=Operator.XOR, children=[patina, colors])

# Build the partial order
root = StrictPartialOrder(nodes=[
    assess, verify, analyze, plan,
    clean, stabilize, fabric_loop,
    repairs, patina_xor,
    document, review, approve,
    package, transport
])

# Define the control-flow dependencies
root.order.add_edge(assess, verify)
root.order.add_edge(verify, analyze)
root.order.add_edge(analyze, plan)

root.order.add_edge(plan, clean)
root.order.add_edge(plan, stabilize)
root.order.add_edge(clean, stabilize)

root.order.add_edge(stabilize, fabric_loop)
root.order.add_edge(stabilize, repairs)

root.order.add_edge(fabric_loop, document)
root.order.add_edge(repairs, document)

root.order.add_edge(document, patina_xor)

root.order.add_edge(patina_xor, review)
root.order.add_edge(patina_xor, approve)

root.order.add_edge(review, approve)
root.order.add_edge(approve, package)
root.order.add_edge(package, transport)