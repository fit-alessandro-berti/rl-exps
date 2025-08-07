import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Milk Sourcing')
cs = Transition(label='Culture Selection')
mt = Transition(label='Milk Testing')
fs = Transition(label='Fermentation Start')
tc = Transition(label='Temperature Control')
pm = Transition(label='pH Monitoring')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
mc = Transition(label='Molding Cheese')
sp = Transition(label='Salting Process')
asup = Transition(label='Aging Setup')
qc = Transition(label='Quality Check')
pp = Transition(label='Packaging Prep')
ld = Transition(label='Label Design')
dp = Transition(label='Distribution Plan')
rd = Transition(label='Retail Delivery')
cf = Transition(label='Customer Feedback')

# Define the aging loop: repeat aging setup, quality check, packaging, label design until exit
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[asup, qc, pp, ld])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    ms, cs, mt, fs, tc, pm, cc, wd, mc, sp, aging_loop,
    dp, rd, cf
])

# Sequential control-flow edges
root.order.add_edge(ms, cs)
root.order.add_edge(cs, mt)
root.order.add_edge(mt, fs)
root.order.add_edge(fs, tc)
root.order.add_edge(tc, pm)
root.order.add_edge(pm, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mc)
root.order.add_edge(mc, sp)
root.order.add_edge(sp, aging_loop)

# After the loop, continue to distribution and final delivery
root.order.add_edge(aging_loop, dp)
root.order.add_edge(dp, rd)
root.order.add_edge(rd, cf)