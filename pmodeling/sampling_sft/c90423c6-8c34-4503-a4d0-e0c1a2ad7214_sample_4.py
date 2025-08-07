import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
farm = Transition(label='Farm Selection')
sample = Transition(label='Sample Testing')
negotiation = Transition(label='Trade Negotiation')
micro_lot = Transition(label='Micro-Lot Sorting')
fermentation = Transition(label='Fermentation Control')
profiling = Transition(label='Sensory Profiling')
roast = Transition(label='Roast Calibration')
blend = Transition(label='Blend Creation')
audit = Transition(label='Sustainability Audit')
pack = Transition(label='Packaging Design')
inspect = Transition(label='Quality Inspection')
sync = Transition(label='Inventory Sync')
plan = Transition(label='Logistics Planning')
train = Transition(label='Cafe Training')
price = Transition(label='Dynamic Pricing')
feedback = Transition(label='Customer Feedback')
trace = Transition(label='Traceability Logging')

# Loop for continuous quality and audit cycles
quality_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[inspect, audit]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    farm, sample, negotiation, micro_lot, fermentation, profiling,
    roast, blend, quality_loop, pack, sync, plan, train, price, feedback, trace
])

# Main flow
root.order.add_edge(farm, sample)
root.order.add_edge(sample, negotiation)
root.order.add_edge(negotiation, micro_lot)
root.order.add_edge(micro_lot, fermentation)
root.order.add_edge(fermentation, profiling)
root.order.add_edge(profiling, roast)
root.order.add_edge(roast, blend)
root.order.add_edge(blend, quality_loop)
root.order.add_edge(quality_loop, pack)
root.order.add_edge(pack, sync)
root.order.add_edge(sync, plan)
root.order.add_edge(plan, train)
root.order.add_edge(train, price)
root.order.add_edge(price, feedback)
root.order.add_edge(feedback, trace)

# Final edges for traceability and sustainability
root.order.add_edge(quality_loop, trace)
root.order.add_edge(quality_loop, audit)