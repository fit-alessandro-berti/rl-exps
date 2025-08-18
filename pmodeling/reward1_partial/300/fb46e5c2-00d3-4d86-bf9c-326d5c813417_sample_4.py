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

# Define exclusive choice for pest monitoring and drone deployment
pest_drones = OperatorPOWL(operator=Operator.XOR, children=[pest_monitor, drone_deploy])

# Define exclusive choice for health scan and data logging
scan_logging = OperatorPOWL(operator=Operator.XOR, children=[health_scan, data_logging])

# Define loop for maintenance plan
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan])

# Define partial order for the process
root = StrictPartialOrder(nodes=[
    site_analysis,
    impact_review,
    modular_design,
    system_integration,
    climate_setup,
    nutrient_mix,
    light_config,
    staff_training,
    pest_drones,
    scan_logging,
    supply_sync,
    maintenance_loop,
    waste_manage
])

# Define dependencies
root.order.add_edge(site_analysis, impact_review)
root.order.add_edge(impact_review, modular_design)
root.order.add_edge(modular_design, system_integration)
root.order.add_edge(system_integration, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, light_config)
root.order.add_edge(light_config, staff_training)
root.order.add_edge(staff_training, pest_drones)
root.order.add_edge(pest_drones, scan_logging)
root.order.add_edge(scan_logging, supply_sync)
root.order.add_edge(supply_sync, maintenance_loop)
root.order.add_edge(maintenance_loop, waste_manage)