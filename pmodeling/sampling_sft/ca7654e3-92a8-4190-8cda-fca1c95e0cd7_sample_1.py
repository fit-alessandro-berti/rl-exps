import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
ms = Transition(label='Milk Sourcing')
cp = Transition(label='Curd Preparation')
sc = Transition(label='starter Culture')
tc = Transition(label='Temperature Control')
press = Transition(label='Pressing Cheese')
salt = Transition(label='Salting Stage')
ag = Transition(label='Aging Process')
mt = Transition(label='Microbial Test')
qc = Transition(label='Quality Check')
ep = Transition(label='Eco Packaging')
lp = Transition(label='Label Printing')
ia = Transition(label='Inventory Audit')
op = Transition(label='Order Processing')
rs = Transition(label='Retail Shipping')
cf = Transition(label='Customer Feedback')
ra = Transition(label='Recipe Update')
ma = Transition(label='Market Analysis')

# Build the feedback loop for continuous improvement
loop_body = StrictPartialOrder(nodes=[ra, ma])
loop_body.order.add_edge(ra, ma)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[qc, loop_body])

# Assemble the main supply chain as a strict partial order
main_chain = StrictPartialOrder(nodes=[
    ms, cp, sc, tc, press, salt, ag, mt,
    feedback_loop, ep, lp, ia, op, rs, cf
])

# Define the control-flow edges
main_chain.order.add_edge(ms, cp)
main_chain.order.add_edge(cp, sc)
main_chain.order.add_edge(sc, tc)
main_chain.order.add_edge(tc, press)
main_chain.order.add_edge(press, salt)
main_chain.order.add_edge(salt, ag)
main_chain.order.add_edge(ag, mt)
main_chain.order.add_edge(mt, feedback_loop)
main_chain.order.add_edge(feedback_loop, ep)
main_chain.order.add_edge(ep, lp)
main_chain.order.add_edge(lp, ia)
main_chain.order.add_edge(ia, op)
main_chain.order.add_edge(op, rs)
main_chain.order.add_edge(rs, cf)

# Final root model
root = main_chain