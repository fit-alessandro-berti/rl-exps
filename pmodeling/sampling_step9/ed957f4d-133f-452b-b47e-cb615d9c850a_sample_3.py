import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
source_materials = Transition(label='Source Materials')
vet_suppliers = Transition(label='Vet Suppliers')
design_modules = Transition(label='Design Modules')
prototype_build = Transition(label='Prototype Build')
test_durability = Transition(label='Test Durability')
secure_permits = Transition(label='Secure Permits')
map_habitats = Transition(label='Map Habitats')
micro_warehouse = Transition(label='Micro Warehouse')
inventory_sync = Transition(label='Inventory Sync')
pack_sustainably = Transition(label='Pack Sustainably')
route_optimize = Transition(label='Route Optimize')
engage_community = Transition(label='Engage Community')
collect_feedback = Transition(label='Collect Feedback')
adjust_production = Transition(label='Adjust Production')
partner_ngo = Transition(label='Partner NGOs')
launch_campaign = Transition(label='Launch Campaign')
monitor_sensors = Transition(label='Monitor Sensors')
report_impact = Transition(label='Report Impact')

# Define silent transitions for skipping activities
skip = SilentTransition()

# Define exclusive choice for vetting suppliers and designing modules
vet_or_design = OperatorPOWL(operator=Operator.XOR, children=[vet_suppliers, design_modules])

# Define loop for prototype build, test durability, secure permits, map habitats, and micro warehouse
prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, test_durability, secure_permits, map_habitats, micro_warehouse])

# Define exclusive choice for engaging community and collecting feedback
engage_or_collect = OperatorPOWL(operator=Operator.XOR, children=[engage_community, collect_feedback])

# Define exclusive choice for adjusting production, partnering with NGOs, launching campaigns, and monitoring sensors
adjust_or_partner_or_launch_or_monitor = OperatorPOWL(operator=Operator.XOR, children=[adjust_production, partner_ngo, launch_campaign, monitor_sensors])

# Define exclusive choice for reporting impact and launching campaigns
report_or_launch = OperatorPOWL(operator=Operator.XOR, children=[report_impact, launch_campaign])

# Define the root POWL model
root = StrictPartialOrder(nodes=[source_materials, vet_or_design, prototype_loop, engage_or_collect, adjust_or_partner_or_launch_or_monitor, report_or_launch])
root.order.add_edge(source_materials, vet_or_design)
root.order.add_edge(vet_or_design, prototype_loop)
root.order.add_edge(prototype_loop, engage_or_collect)
root.order.add_edge(engage_or_collect, adjust_or_partner_or_launch_or_monitor)
root.order.add_edge(adjust_or_partner_or_launch_or_monitor, report_or_launch)