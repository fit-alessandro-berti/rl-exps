import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
farm = Transition(label='Farm Sourcing')
lot = Transition(label='Lot Selection')
sort = Transition(label='Bean Sorting')
ferm = Transition(label='Fermentation')
dry = Transition(label='Drying Process')
qc = Transition(label='Quality Control')
chem = Transition(label='Chemical Testing')
sens = Transition(label='Sensory Analysis')
roast = Transition(label='Roast Profiling')
pack = Transition(label='Eco Packaging')
trace = Transition(label='Traceability QR')
cold = Transition(label='Cold Transport')
env = Transition(label='Env Monitoring')
cust = Transition(label='Customer Feedback')
adjust = Transition(label='Subscription Adjust')

# Build the loop body for quality control and feedback
qc_body = StrictPartialOrder(nodes=[chem, sens])
qc_body.order.add_edge(chem, sens)

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[qc_body, cust])

# Build the packaging branch with traceability and monitoring
pack_branch = StrictPartialOrder(nodes=[trace, env])
pack_branch.order.add_edge(trace, env)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    farm, lot, sort,
    ferm, dry,
    feedback_loop,
    roast,
    pack_branch
])

# Define the control-flow edges
root.order.add_edge(farm, lot)
root.order.add_edge(lot, sort)
root.order.add_edge(sort, ferm)
root.order.add_edge(sort, dry)
root.order.add_edge(ferm, feedback_loop)
root.order.add_edge(dry, feedback_loop)
root.order.add_edge(feedback_loop, roast)
root.order.add_edge(roast, pack_branch)
root.order.add_edge(pack_branch, trace)
root.order.add_edge(pack_branch, env)