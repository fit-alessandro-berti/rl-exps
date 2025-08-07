import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
isource = Transition(label='Ingredient Sourcing')
be = Transition(label='Botanical Extraction')
ib = Transition(label='Initial Blending')
st = Transition(label='Sensory Testing')
ca = Transition(label='Chemical Analysis')
ra = Transition(label='Recipe Refinement')
sc = Transition(label='Stability Check')
cs = Transition(label='Client Sampling')
fr = Transition(label='Feedback Review')
fa = Transition(label='Final Adjustment')
cp = Transition(label='Custom Packaging')
ld = Transition(label='Label Design')
hl = Transition(label='Hand Labeling')
raudit = Transition(label='Regulatory Audit')
bd = Transition(label='Batch Documentation')
lr = Transition(label='Limited Release')
ml = Transition(label='Market Launch')

# Loop for sensory and chemical refinement
sens_loop = OperatorPOWL(operator=Operator.LOOP, children=[st, ca])

# Build the partial order
root = StrictPartialOrder(nodes=[
    isource, be, ib, sens_loop, ra, cs, fa, cp, ld, hl, raudit, bd, lr, ml
])

# Define the control-flow dependencies
root.order.add_edge(isource, be)
root.order.add_edge(be, ib)
root.order.add_edge(ib, sens_loop)
root.order.add_edge(sens_loop, ra)
root.order.add_edge(ra, raudit)
root.order.add_edge(raudit, cs)
root.order.add_edge(cs, fa)
root.order.add_edge(fa, cp)
root.order.add_edge(cp, ld)
root.order.add_edge(ld, hl)
root.order.add_edge(hl, bd)
root.order.add_edge(bd, lr)
root.order.add_edge(lr, ml)