import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis      = Transition(label='Site Analysis')
impact_review      = Transition(label='Impact Review')
modular_design     = Transition(label='Modular Design')
system_integration = Transition(label='System Integration')
climate_setup      = Transition(label='Climate Setup')
nutrient_mix       = Transition(label='Nutrient Mix')
light_config       = Transition(label='Light Config')
staff_training     = Transition(label='Staff Training')
pest_monitor       = Transition(label='Pest Monitor')
drone_deploy       = Transition(label='Drone Deploy')
health_scan        = Transition(label='Health Scan')
data_logging       = Transition(label='Data Logging')
supply_sync        = Transition(label='Supply Sync')
maintenance_plan   = Transition(label='Maintenance Plan')
waste_manage       = Transition(label='Waste Manage')

# Loop for continuous monitoring and maintenance
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pest_monitor, drone_deploy, health_scan, data_logging]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    impact_review,
    modular_design,
    system_integration,
    climate_setup,
    nutrient_mix,
    light_config,
    staff_training,
    monitor_loop,
    supply_sync,
    maintenance_plan,
    waste_manage
])

# Define control-flow dependencies
root.order.add_edge(site_analysis, impact_review)
root.order.add_edge(impact_review, modular_design)
root.order.add_edge(modular_design, system_integration)
root.order.add_edge(system_integration, climate_setup)
root.order.add_edge(system_integration, nutrient_mix)
root.order.add_edge(system_integration, light_config)
root.order.add_edge(climate_setup, staff_training)
root.order.add_edge(nutrient_mix, staff_training)
root.order.add_edge(light_config, staff_training)
root.order.add_edge(staff_training, monitor_loop)
root.order.add_edge(monitor_loop, supply_sync)
root.order.add_edge(supply_sync, maintenance_plan)
root.order.add_edge(maintenance_plan, waste_manage)