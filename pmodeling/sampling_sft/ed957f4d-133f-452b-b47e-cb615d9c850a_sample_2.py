import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
source = Transition(label='Source Materials')
vet = Transition(label='Vet Suppliers')
design = Transition(label='Design Modules')
prototype = Transition(label='Prototype Build')
test = Transition(label='Test Durability')
secure = Transition(label='Secure Permits')
map_habitats = Transition(label='Map Habitats')
micro_warehouse = Transition(label='Micro Warehouse')
inventory_sync = Transition(label='Inventory Sync')
pack_sustainably = Transition(label='Pack Sustainably')
route_optimize = Transition(label='Route Optimize')
engage_community = Transition(label='Engage Community')
collect_feedback = Transition(label='Collect Feedback')
adjust_production = Transition(label='Adjust Production')
partner_ngos = Transition(label='Partner NGOs')
launch_campaign = Transition(label='Launch Campaign')
monitor_sensors = Transition(label='Monitor Sensors')
report_impact = Transition(label='Report Impact')

# Build the main production loop body: Prototype -> Test -> Pack Sustainably
body = StrictPartialOrder(nodes=[prototype, test, pack_sustainably])
body.order.add_edge(prototype, test)
body.order.add_edge(test, pack_sustainably)

# Define the feedback loop: Collect Feedback -> Adjust Production
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[collect_feedback, adjust_production])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    source, vet, design,
    body,
    secure, map_habitats,
    micro_warehouse, inventory_sync,
    route_optimize,
    engage_community, feedback_loop,
    partner_ngos, launch_campaign,
    monitor_sensors, report_impact
])

# Define the control-flow dependencies
root.order.add_edge(source, vet)
root.order.add_edge(vet, design)
root.order.add_edge(design, body)
root.order.add_edge(body, secure)
root.order.add_edge(secure, map_habitats)
root.order.add_edge(map_habitats, micro_warehouse)
root.order.add_edge(micro_warehouse, inventory_sync)
root.order.add_edge(inventory_sync, route_optimize)
root.order.add_edge(route_optimize, engage_community)
root.order.add_edge(engage_community, feedback_loop)
root.order.add_edge(feedback_loop, secure)
root.order.add_edge(secure, map_habitats)
root.order.add_edge(map_habitats, micro_warehouse)
root.order.add_edge(micro_warehouse, inventory_sync)
root.order.add_edge(inventory_sync, route_optimize)
root.order.add_edge(route_optimize, partner_ngos)
root.order.add_edge(partner_ngos, launch_campaign)
root.order.add_edge(launch_campaign, monitor_sensors)
root.order.add_edge(monitor_sensors, report_impact)