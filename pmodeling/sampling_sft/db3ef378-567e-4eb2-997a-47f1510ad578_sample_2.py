import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Define the loop for aging: do Initial Aging, then either exit or do Humidity Control -> Temperature Check -> Flavor Testing -> repeat
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ia, OperatorPOWL(operator=Operator.XOR, children=[Transition(), StrictPartialOrder(nodes=[hc, tc, ft])])
    ]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    mc, cp, cf, ws, mcg, sp, aging_loop, pa, lp, iaudit, of, ss, em
])

# Add ordering constraints
root.order.add_edge(mc, cp)
root.order.add_edge(cp, cf)
root.order.add_edge(cf, ws)
root.order.add_edge(ws, mcg)
root.order.add_edge(mcg, sp)
root.order.add_edge(sp, aging_loop)
root.order.add_edge(aging_loop, pa)
root.order.add_edge(pa, lp)
root.order.add_edge(lp, iaudit)
root.order.add_edge(iaudit, of)
root.order.add_edge(of, ss)
root.order.add_edge(ss, em)

print(root)