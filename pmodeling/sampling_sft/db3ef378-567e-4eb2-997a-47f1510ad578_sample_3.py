import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
mc = Transition(label='Milk Collection')
cp = Transition(label='Culture Prep')
cf = Transition(label='Curd Formation')
ws = Transition(label='Whey Separation')
mcg = Transition(label='Molding Cheese')
sp = Transition(label='Salting Process')
ia = Transition(label='Initial Aging')
hc = Transition(label='Humidity Control')
tc = Transition(label='Temperature Check')
ft = Transition(label='Flavor Testing')
fa = Transition(label='Final Aging')
pa = Transition(label='Packaging Artisanal')
lp = Transition(label='Label Printing')
iaudit = Transition(label='Inventory Audit')
of = Transition(label='Order Fulfillment')
ss = Transition(label='Subscription Setup')
em = Transition(label='Event Marketing')

# Define the aging loop: repeat Humidity Control and Temperature Check until Flavor Testing passes
loop_aging = OperatorPOWL(
    operator=Operator.LOOP,
    children=[hc, tc]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    mc, cp, cf, ws, mcg, sp, ia, loop_aging, ft, fa, pa, lp, iaudit, of, ss, em
])

# Sequential edges from milk collection to the cheese production
root.order.add_edge(mc, cp)
root.order.add_edge(cp, cf)
root.order.add_edge(cf, ws)
root.order.add_edge(ws, mcg)
root.order.add_edge(mcg, sp)

# Concurrent edges after salting
root.order.add_edge(sp, ia)
root.order.add_edge(sp, loop_aging)

# After initial aging, either Flavor Testing passes or the loop repeats
root.order.add_edge(ia, ft)
root.order.add_edge(loop_aging, ft)

# After Flavor Testing, move to packaging and labeling
root.order.add_edge(ft, pa)
root.order.add_edge(ft, lp)

# After packaging and labeling, perform inventory audit and fulfillment
root.order.add_edge(pa, iaudit)
root.order.add_edge(lp, iaudit)
root.order.add_edge(iaudit, of)

# After fulfillment, set up subscriptions and event marketing
root.order.add_edge(of, ss)
root.order.add_edge(of, em)