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
test = Transition(label='Chemical Testing')
sens = Transition(label='Sensory Analysis')
roast = Transition(label='Roast Profiling')
pack = Transition(label='Eco Packaging')
trace = Transition(label='Traceability QR')
cold = Transition(label='Cold Transport')
env = Transition(label='Env Monitoring')
feedback = Transition(label='Customer Feedback')
adjust = Transition(label='Subscription Adjust')

# Loop for continuous process refinement
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[feedback, adjust]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    farm, lot, sort,
    ferm, dry, qc, test, sens,
    roast, pack, trace, cold, env,
    loop
])

# Sequence of activities in the loop body
root.order.add_edge(farm, lot)
root.order.add_edge(lot, sort)
root.order.add_edge(sort, ferm)
root.order.add_edge(ferm, dry)
root.order.add_edge(dry, qc)
root.order.add_edge(qc, test)
root.order.add_edge(test, sens)
root.order.add_edge(sens, roast)
root.order.add_edge(roast, pack)
root.order.add_edge(pack, trace)
root.order.add_edge(trace, cold)
root.order.add_edge(cold, env)

# Loop execution: do the above sequence, then either exit or repeat
root.order.add_edge(env, loop)
root.order.add_edge(loop, env)