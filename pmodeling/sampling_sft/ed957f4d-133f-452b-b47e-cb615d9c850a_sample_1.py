import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
source = Transition(label='Source Materials')
vet = Transition(label='Vet Suppliers')
design = Transition(label='Design Modules')
prototype = Transition(label='Prototype Build')
test = Transition(label='Test Durability')
secure = Transition(label='Secure Permits')
map_hab = Transition(label='Map Habitats')
micro = Transition(label='Micro Warehouse')
inv_sync = Transition(label='Inventory Sync')
pack = Transition(label='Pack Sustainably')
route = Transition(label='Route Optimize')
engage = Transition(label='Engage Community')
feedback = Transition(label='Collect Feedback')
adjust = Transition(label='Adjust Production')
partner = Transition(label='Partner NGOs')
launch = Transition(label='Launch Campaign')
monitor = Transition(label='Monitor Sensors')
report = Transition(label='Report Impact')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for continuous feedback and production adjustments
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[feedback, adjust]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    source, vet, design, prototype, test, secure,
    map_hab, micro, inv_sync, pack, route,
    engage, partner, launch, monitor, report,
    feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(source, vet)
root.order.add_edge(vet, design)
root.order.add_edge(design, prototype)
root.order.add_edge(prototype, test)
root.order.add_edge(test, secure)
root.order.add_edge(secure, map_hab)
root.order.add_edge(map_hab, micro)
root.order.add_edge(micro, inv_sync)
root.order.add_edge(inv_sync, pack)
root.order.add_edge(pack, route)
root.order.add_edge(route, engage)
root.order.add_edge(engage, partner)
root.order.add_edge(partner, launch)
root.order.add_edge(launch, monitor)
root.order.add_edge(monitor, report)
root.order.add_edge(report, feedback_loop)

# Finalize the loop dependency
root.order.add_edge(feedback_loop, skip)

# Finalize the feedback loop dependency
root.order.add_edge(feedback_loop, feedback_loop)

# The final root POWL model
print(root)