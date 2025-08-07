import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Sourcing')
cp = Transition(label='Culture Prep')
mp = Transition(label='Milk Pasteurize')
coag = Transition(label='Coagulation')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
hm = Transition(label='Hand Molding')
pr = Transition(label='Pressing')
sl = Transition(label='Salting')
rt = Transition(label='Rind Treatment')
asup = Transition(label='Aging Setup')
mctl = Transition(label='Microclimate Control')
fp = Transition(label='Flavor Profiling')
qc = Transition(label='Quality Check')
sr = Transition(label='Sensory Review')
ti = Transition(label='Texture Inspect')
ep = Transition(label='Eco Packaging')
bl = Transition(label='Blockchain Log')
bl2 = Transition(label='Batch Labeling')
ns = Transition(label='Niche Shipping')

# Define the quality control partial order: sensory review -> texture inspect
qc_po = StrictPartialOrder(nodes=[sr, ti])
qc_po.order.add_edge(sr, ti)

# Define the loop for aging: Microclimate Control then either exit or repeat
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[mctl, qc_po])

# Build the overall supply chain partial order
root = StrictPartialOrder(nodes=[
    ms, cp, mp, coag, cc, wd, hm, pr, sl, rt,
    asup, aging_loop,
    fp, qc, bl, bl2, ns
])

# Define the control-flow edges
root.order.add_edge(ms, cp)
root.order.add_edge(cp, mp)
root.order.add_edge(mp, coag)
root.order.add_edge(coag, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, hm)
root.order.add_edge(hm, pr)
root.order.add_edge(pr, sl)
root.order.add_edge(sl, rt)
root.order.add_edge(rt, asup)
root.order.add_edge(asup, aging_loop)
root.order.add_edge(aging_loop, fp)
root.order.add_edge(fp, qc)
root.order.add_edge(qc, bl)
root.order.add_edge(bl, bl2)
root.order.add_edge(bl2, ns)

# Print the root model for verification
print(root)