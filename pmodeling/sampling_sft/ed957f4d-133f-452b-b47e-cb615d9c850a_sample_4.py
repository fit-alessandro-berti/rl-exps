import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
source = Transition(label='Source Materials')
vet = Transition(label='Vet Suppliers')
design = Transition(label='Design Modules')
prototype = Transition(label='Prototype Build')
test = Transition(label='Test Durability')
secure = Transition(label='Secure Permits')
map_habitats = Transition(label='Map Habitats')
micro_warehouse = Transition(label='Micro Warehouse')
inventory = Transition(label='Inventory Sync')
pack = Transition(label='Pack Sustainably')
route = Transition(label='Route Optimize')
engage = Transition(label='Engage Community')
collect = Transition(label='Collect Feedback')
adjust = Transition(label='Adjust Production')
partner = Transition(label='Partner NGOs')
launch = Transition(label='Launch Campaign')
monitor = Transition(label='Monitor Sensors')
report = Transition(label='Report Impact')

# Silent transition for loop exit
skip = SilentTransition()

# Build the adaptation loop: Collect Feedback, then choose to exit or Adjust Production and repeat
adapt_loop = OperatorPOWL(operator=Operator.LOOP, children=[collect, adjust])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    source, vet, design, prototype, test, secure,
    map_habitats, micro_warehouse, inventory, pack, route, engage,
    adapt_loop, partner, launch, monitor, report
])

# Define the control-flow dependencies
root.order.add_edge(source, vet)
root.order.add_edge(vet, design)
root.order.add_edge(design, prototype)
root.order.add_edge(prototype, test)
root.order.add_edge(test, secure)
root.order.add_edge(secure, map_habitats)
root.order.add_edge(map_habitats, micro_warehouse)
root.order.add_edge(micro_warehouse, inventory)
root.order.add_edge(inventory, pack)
root.order.add_edge(pack, route)
root.order.add_edge(route, engage)
root.order.add_edge(engage, adapt_loop)
root.order.add_edge(adapt_loop, partner)
root.order.add_edge(partner, launch)
root.order.add_edge(launch, monitor)
root.order.add_edge(monitor, report)