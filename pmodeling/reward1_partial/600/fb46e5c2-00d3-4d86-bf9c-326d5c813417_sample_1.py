import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
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

# Create a strict partial order graph
root = StrictPartialOrder()

# Define the process flow
root.add_transition(site_analysis)
root.add_transition(impact_review)
root.add_transition(modular_design)
root.add_transition(system_integration)
root.add_transition(climate_setup)
root.add_transition(nutrient_mix)
root.add_transition(light_config)
root.add_transition(staff_training)
root.add_transition(pest_monitor)
root.add_transition(drone_deploy)
root.add_transition(health_scan)
root.add_transition(data_logging)
root.add_transition(supply_sync)
root.add_transition(maintenance_plan)
root.add_transition(waste_manage)

# Define the dependencies
root.add_edge(site_analysis, impact_review)
root.add_edge(impact_review, modular_design)
root.add_edge(modular_design, system_integration)
root.add_edge(system_integration, climate_setup)
root.add_edge(climate_setup, nutrient_mix)
root.add_edge(nutrient_mix, light_config)
root.add_edge(light_config, staff_training)
root.add_edge(staff_training, pest_monitor)
root.add_edge(pest_monitor, drone_deploy)
root.add_edge(drone_deploy, health_scan)
root.add_edge(health_scan, data_logging)
root.add_edge(data_logging, supply_sync)
root.add_edge(supply_sync, maintenance_plan)
root.add_edge(maintenance_plan, waste_manage)

# Print the root to see the POWL model
print(root)