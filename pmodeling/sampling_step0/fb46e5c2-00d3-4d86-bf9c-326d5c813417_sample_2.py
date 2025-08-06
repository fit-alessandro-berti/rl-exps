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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_pest_monitor = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, drone_deploy])
loop_light_config = OperatorPOWL(operator=Operator.LOOP, children=[light_config, health_scan])
loop_data_logging = OperatorPOWL(operator=Operator.LOOP, children=[data_logging, waste_manage])

# Define XOR nodes
xor_pest_monitor_light_config = OperatorPOWL(operator=Operator.XOR, children=[loop_pest_monitor, loop_light_config])
xor_data_logging_waste_manage = OperatorPOWL(operator=Operator.XOR, children=[loop_data_logging, supply_sync])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_analysis, impact_review, modular_design, system_integration, climate_setup, nutrient_mix, staff_training, xor_pest_monitor_light_config, xor_data_logging_waste_manage, maintenance_plan, waste_manage])
root.order.add_edge(site_analysis, impact_review)
root.order.add_edge(impact_review, modular_design)
root.order.add_edge(modular_design, system_integration)
root.order.add_edge(system_integration, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, light_config)
root.order.add_edge(light_config, staff_training)
root.order.add_edge(staff_training, xor_pest_monitor_light_config)
root.order.add_edge(xor_pest_monitor_light_config, xor_data_logging_waste_manage)
root.order.add_edge(xor_data_logging_waste_manage, maintenance_plan)
root.order.add_edge(maintenance_plan, waste_manage)