import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
cp = Transition(label='Client Profiling')
isrc = Transition(label='Ingredient Sourcing')
qc = Transition(label='Quality Check')
be = Transition(label='Blend Experiment')
mc = Transition(label='Maturation Cycle')
sp = Transition(label='Sensory Panel')
rl = Transition(label='Refinement Loop')
st = Transition(label='Stability Test')
pd = Transition(label='Packaging Design')
bc = Transition(label='Batch Coordination')
ca = Transition(label='Compliance Audit')
ms = Transition(label='Market Survey')
fr = Transition(label='Feedback Review')
of = Transition(label='Order Finalize')
dp = Transition(label='Distribution Plan')
iu = Transition(label='Inventory Update')

# Build the refinement loop: Blend Experiment -> Sensory Panel -> Refinement Loop
refinement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[be, sp, rl]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    cp, isrc, qc, refinement_loop, st, pd, bc, ca, ms, fr, of, dp, iu
])

# Define the control-flow edges
root.order.add_edge(cp, isrc)
root.order.add_edge(isrc, qc)
root.order.add_edge(qc, refinement_loop)
root.order.add_edge(refinement_loop, st)
root.order.add_edge(st, pd)
root.order.add_edge(pd, bc)
root.order.add_edge(bc, ca)
root.order.add_edge(ca, ms)
root.order.add_edge(ms, fr)
root.order.add_edge(fr, of)
root.order.add_edge(of, dp)
root.order.add_edge(dp, iu)

# Print the root model (optional)
print(root)