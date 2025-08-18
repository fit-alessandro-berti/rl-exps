import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
impact_review = Transition(label='Impact Review')
modular_design = Transition(label='Modular Design')
system_integration = Transition(label='System Integration')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
light_config = Transition(label='Light Config')
staff_training = Transition(label='Staff Training')
pest_monitor = Transition(label='Pest Monitor')
drone_deploy = Transition(label='Drone Deploy')
health_scan = Transition(label='Health Scan')
data_logging = Transition(label='Data Logging')
supply_sync = Transition(label='Supply Sync')
maintenance_plan = Transition(label='Maintenance Plan')
waste_manage = Transition(label='Waste Manage')

# Define silent transitions for loops
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define exclusive choice for staff training and pest monitoring
xor1 = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_monitor, skip2])

# Define exclusive choice for data logging and waste management
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_logging, skip3])

# Define loop for drone deployment and health scan
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[drone_deploy, health_scan])

# Define loop for maintenance plan and waste management
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, waste_manage])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_analysis, impact_review, modular_design, system_integration, climate_setup, nutrient_mix, light_config, xor1, xor2, loop1, loop2, supply_sync, xor3])
root.order.add_edge(site_analysis, impact_review)
root.order.add_edge(impact_review, modular_design)
root.order.add_edge(modular_design, system_integration)
root.order.add_edge(system_integration, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, light_config)
root.order.add_edge(light_config, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, loop1)
root.order.add_edge(loop1, xor3)
root.order.add_edge(xor3, supply_sync)
root.order.add_edge(supply_sync, loop2)
root.order.add_edge(loop2, maintenance_plan)
root.order.add_edge(maintenance_plan, waste_manage)