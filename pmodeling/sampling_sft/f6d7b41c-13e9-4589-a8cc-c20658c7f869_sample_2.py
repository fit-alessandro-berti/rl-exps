import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cc = Transition(label='Client Consult')
na = Transition(label='Needs Assess')
ic = Transition(label='Inventory Check')
asst = Transition(label='Art Selection')
ld = Transition(label='Legal Draft')
cs = Transition(label='Contract Sign')
isup = Transition(label='Insurance Setup')
tp = Transition(label='Transport Plan')
st = Transition(label='Secure Transit')
ai = Transition(label='Art Install')
ccn = Transition(label='Condition Check')
al = Transition(label='Appraisal Log')
lr = Transition(label='Lease Renew')
pp = Transition(label='Payment Process')
dp = Transition(label='Deinstall Art')
ri = Transition(label='Return Inspect')
po = Transition(label='Purchase Option')

# Silent transition for optional purchase
skip = SilentTransition()

# Loop for optional purchase: Purchase Option or skip
purchase_loop = OperatorPOWL(operator=Operator.LOOP, children=[po, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    cc, na, ic, asst, ld, cs, isup, tp, st, ai,
    ccn, al, lr, pp, dp, ri, purchase_loop
])

# Define the control-flow dependencies
root.order.add_edge(cc, na)
root.order.add_edge(na, ic)
root.order.add_edge(ic, asst)
root.order.add_edge(asst, ld)
root.order.add_edge(ld, cs)
root.order.add_edge(cs, isup)
root.order.add_edge(isup, tp)
root.order.add_edge(tp, st)
root.order.add_edge(st, ai)
root.order.add_edge(ai, ccn)
root.order.add_edge(ai, al)
root.order.add_edge(ccn, lr)
root.order.add_edge(al, lr)
root.order.add_edge(lr, pp)
root.order.add_edge(pp, dp)
root.order.add_edge(dp, ri)
root.order.add_edge(ri, purchase_loop)
# Purchase Loop: after any payment and inspection, either do purchase or exit
root.order.add_edge(lr, purchase_loop)
root.order.add_edge(pp, purchase_loop)
root.order.add_edge(ri, purchase_loop)
root.order.add_edge(purchase_loop, lr)
root.order.add_edge(purchase_loop, pp)
root.order.add_edge(purchase_loop, ri)
# Loop exit can happen at any time after purchase
root.order.add_edge(purchase_loop, purchase_loop)

print(root)