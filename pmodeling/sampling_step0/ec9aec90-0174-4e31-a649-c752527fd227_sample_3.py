import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

assess = Transition(label='Assess Artifact')
verify = Transition(label='Verify Provenance')
analyze = Transition(label='Analyze Condition')
plan = Transition(label='Plan Conservation')
clean = Transition(label='Clean Surface')
stabilize = Transition(label='Stabilize Structure')
source = Transition(label='Source Materials')
fabricate = Transition(label='Fabricate Parts')
repair = Transition(label='Perform Repairs')
patina = Transition(label='Apply Patina')
match = Transition(label='Match Colors')
document = Transition(label='Document Process')
review = Transition(label='Review Quality')
approve = Transition(label='Obtain Approval')
package = Transition(label='Package Securely')
transport = Transition(label='Arrange Transport')

skip = SilentTransition()

# Sequential steps
sequential = OperatorPOWL(operator=Operator.SEQUENCE, children=[assess, verify, analyze, plan, clean, stabilize, source, fabricate, repair, patina, match, document, review, approve, package, transport])

# Partial Order
partial_order = StrictPartialOrder(nodes=[sequential, skip])
partial_order.order.add_edge(sequential, skip)

root = partial_order