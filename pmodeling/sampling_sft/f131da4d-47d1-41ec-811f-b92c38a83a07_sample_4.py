import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
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
asetup = Transition(label='Aging Setup')
qc = Transition(label='Quality Check')
pp = Transition(label='Packaging Prep')
ld = Transition(label='Label Design')
dp = Transition(label='Distribution Plan')
rd = Transition(label='Retail Delivery')
cf = Transition(label='Customer Feedback')

# Build the main production sequence as a partial order
prod = StrictPartialOrder(nodes=[
    ms, cs, mt, fs, tc, pm, cc, wd, mc, sp, asetup, qc, pp, ld, dp, rd, cf
])
seq_order = [
    (ms, cs), (ms, mt), (cs, fs), (mt, fs), (fs, tc), (fs, pm),
    (tc, cc), (tc, wd), (pm, cc), (pm, wd), (cc, mc), (wd, mc),
    (mc, sp), (sp, asetup), (asetup, qc), (qc, pp), (pp, ld),
    (ld, dp), (dp, rd), (rd, cf)
]
for src, trg in seq_order:
    prod.order.add_edge(src, trg)

# Loop for repeated quality checks and packaging prep
qc_loop = OperatorPOWL(operator=Operator.LOOP, children=[qc, pp])

# Assemble the full process
root = StrictPartialOrder(nodes=[
    ms, cs, mt, fs, tc, pm, cc, wd, mc, sp, asetup, qc_loop, ld, dp, rd, cf
])
loop_order = [
    (ms, cs), (ms, mt), (cs, fs), (mt, fs), (fs, tc), (fs, pm),
    (tc, cc), (tc, wd), (pm, cc), (pm, wd), (cc, mc), (wd, mc),
    (mc, sp), (sp, asetup), (asetup, qc_loop), (qc_loop, ld),
    (ld, dp), (dp, rd), (rd, cf)
]
for src, trg in loop_order:
    root.order.add_edge(src, trg)