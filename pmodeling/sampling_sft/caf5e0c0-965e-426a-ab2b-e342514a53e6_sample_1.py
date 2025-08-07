import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
system_design    = Transition(label='System Design')
climate_sim      = Transition(label='Climate Sim')
seed_select      = Transition(label='Seed Select')
module_setup     = Transition(label='Module Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
water_cycle      = Transition(label='Water Cycle')
energy_link      = Transition(label='Energy Link')
sensor_install   = Transition(label='Sensor Install')
pest_detect      = Transition(label='Pest Detect')
growth_scan      = Transition(label='Growth Scan')
data_sync        = Transition(label='Data Sync')
community_meet   = Transition(label='Community Meet')
reg_compliance   = Transition(label='Reg Compliance')
system_test      = Transition(label='System Test')
maintenance_plan = Transition(label='Maintenance Plan')

# Define the maintenance loop: repeat Maintenance Plan until exit
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, maintenance_plan])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, system_design, climate_sim, seed_select,
    module_setup, nutrient_mix, water_cycle, energy_link,
    sensor_install, pest_detect, growth_scan, data_sync,
    community_meet, reg_compliance, system_test,
    maintenance_loop
])

# Sequence of Site Survey -> System Design -> Climate Sim -> Seed Select
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, climate_sim)
root.order.add_edge(climate_sim, seed_select)

# After seed selection, proceed with all subsequent steps in parallel
for next_step in [module_setup, nutrient_mix, water_cycle, energy_link, sensor_install]:
    root.order.add_edge(seed_select, next_step)

# After setup, all environmental and monitoring steps are concurrent
for next_step in [pest_detect, growth_scan, data_sync]:
    root.order.add_edge(module_setup, next_step)

# Data sync and community meet are concurrent
root.order.add_edge(data_sync, community_meet)

# After community meet, compliance and test must happen sequentially
root.order.add_edge(community_meet, reg_compliance)
root.order.add_edge(reg_compliance, system_test)

# Finally, run the maintenance loop
root.order.add_edge(system_test, maintenance_loop)