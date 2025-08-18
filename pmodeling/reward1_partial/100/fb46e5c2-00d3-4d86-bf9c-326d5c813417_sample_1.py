import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the loop nodes
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix, light_config])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, drone_deploy, health_scan])

# Define the partial order
root = StrictPartialOrder(nodes=[site_analysis, impact_review, modular_design, system_integration, climate_loop, pest_loop, staff_training, data_logging, supply_sync, maintenance_plan, waste_manage])
root.order.add_edge(site_analysis, impact_review)
root.order.add_edge(site_analysis, modular_design)
root.order.add_edge(impact_review, modular_design)
root.order.add_edge(modular_design, system_integration)
root.order.add_edge(system_integration, climate_loop)
root.order.add_edge(system_integration, pest_loop)
root.order.add_edge(climate_loop, staff_training)
root.order.add_edge(pest_loop, staff_training)
root.order.add_edge(staff_training, data_logging)
root.order.add_edge(data_logging, supply_sync)
root.order.add_edge(supply_sync, maintenance_plan)
root.order.add_edge(maintenance_plan, waste_manage)

print(root)