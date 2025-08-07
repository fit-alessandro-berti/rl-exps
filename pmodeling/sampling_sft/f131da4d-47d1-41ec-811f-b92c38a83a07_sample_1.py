import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
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

# Build the loop for aging and quality check
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[asup, qc])

# Build the main production sequence as a partial order
production_seq = StrictPartialOrder(nodes=[
    ms, cs, mt, fs, tc, pm, cc, wd, mc, sp, aging_loop, pp, ld, dp, rd, cf
])
# Sequential flow within the production loop
production_seq.order.add_edge(ms, cs)
production_seq.order.add_edge(cs, mt)
production_seq.order.add_edge(mt, fs)
production_seq.order.add_edge(fs, tc)
production_seq.order.add_edge(tc, pm)
production_seq.order.add_edge(pm, cc)
production_seq.order.add_edge(cc, wd)
production_seq.order.add_edge(wd, mc)
production_seq.order.add_edge(mc, sp)
production_seq.order.add_edge(sp, aging_loop)
# Packaging and distribution follow the main production sequence
production_seq.order.add_edge(aging_loop, pp)
production_seq.order.add_edge(pp, ld)
production_seq.order.add_edge(ld, dp)
production_seq.order.add_edge(dp, rd)
production_seq.order.add_edge(rd, cf)

# Final root model is the complete production sequence
root = production_seq