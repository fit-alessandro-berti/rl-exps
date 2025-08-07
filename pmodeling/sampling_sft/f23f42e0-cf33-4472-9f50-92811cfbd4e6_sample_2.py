import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Milk Sourcing')
cs = Transition(label='Culture Selection')
mt = Transition(label='Milk Testing')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
mi = Transition(label='Mold Inoculation')
fc = Transition(label='Forming Cheese')
ss = Transition(label='Salting Stage')
asup = Transition(label='Aging Setup')
ccs = Transition(label='Climate Control')
qt = Transition(label='Quality Tasting')
pp = Transition(label='Packaging Prep')
lp = Transition(label='Label Printing')
dp = Transition(label='Distribution Plan')
rd = Transition(label='Retail Delivery')
ec = Transition(label='Event Coordination')
ra = Transition(label='Regulatory Audit')

# Loop for aging: repeat Climate Control and Quality Tasting until exit
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[ccs, qt])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, cs, mt,
    cc, wd, mi,
    fc, ss,
    aging_loop,
    pp, lp, dp,
    rd, ec, ra
])

# Sequence for cheese production
root.order.add_edge(ms, mt)
root.order.add_edge(mt, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, fc)
root.order.add_edge(fc, ss)

# After salting, start aging
root.order.add_edge(ss, aging_loop)

# After aging, proceed to packaging and distribution
root.order.add_edge(aging_loop, pp)
root.order.add_edge(pp, lp)
root.order.add_edge(lp, dp)

# Final steps after packaging
root.order.add_edge(dp, rd)
root.order.add_edge(rd, ec)
root.order.add_edge(ec, ra)

# Regulatory audit after all steps
root.order.add_edge(ra, ra)  # loop back to audit for compliance

print(root)