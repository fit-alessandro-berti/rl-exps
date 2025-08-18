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

# Define transitions for loop and choice
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, drone_deploy, health_scan, data_logging, staff_training])
xor = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, waste_manage])

# Define the root node
root = StrictPartialOrder(nodes=[site_analysis, impact_review, modular_design, system_integration, climate_setup, nutrient_mix, light_config, loop, xor])
root.order.add_edge(site_analysis, impact_review)
root.order.add_edge(impact_review, modular_design)
root.order.add_edge(modular_design, system_integration)
root.order.add_edge(system_integration, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, light_config)
root.order.add_edge(light_config, loop)
root.order.add_edge(loop, xor)

print(root)