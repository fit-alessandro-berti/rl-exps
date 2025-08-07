import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
system_design   = Transition(label='System Design')
climate_sim     = Transition(label='Climate Sim')
seed_select     = Transition(label='Seed Select')
module_setup    = Transition(label='Module Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
water_cycle     = Transition(label='Water Cycle')
energy_link     = Transition(label='Energy Link')
sensor_install  = Transition(label='Sensor Install')
pest_detect     = Transition(label='Pest Detect')
growth_scan     = Transition(label='Growth Scan')
data_sync       = Transition(label='Data Sync')
community_meet  = Transition(label='Community Meet')
reg_compliance  = Transition(label='Reg Compliance')
system_test     = Transition(label='System Test')
maintenance_plan= Transition(label='Maintenance Plan')

# Build the monitoring & community‐engagement sub‐process
monitoring_po = StrictPartialOrder(nodes=[pest_detect, growth_scan, data_sync])
monitoring_po.order.add_edge(pest_detect, growth_scan)
monitoring_po.order.add_edge(growth_scan, data_sync)

community_po = StrictPartialOrder(nodes=[community_meet])
community_po.order.add_edge(community_meet, community_meet)  # loop back to itself

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    system_design,
    climate_sim,
    seed_select,
    module_setup,
    nutrient_mix,
    water_cycle,
    energy_link,
    sensor_install,
    monitoring_po,
    community_po,
    reg_compliance,
    system_test,
    maintenance_plan
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, climate_sim)
root.order.add_edge(climate_sim, seed_select)
root.order.add_edge(seed_select, module_setup)
root.order.add_edge(module_setup, nutrient_mix)
root.order.add_edge(module_setup, water_cycle)
root.order.add_edge(module_setup, energy_link)
root.order.add_edge(module_setup, sensor_install)

# Monitoring & community‐engagement are concurrent after setup
for node in [monitoring_po, community_po]:
    for child in monitoring_po.nodes:
        root.order.add_edge(module_setup, child)

# Post‐setup dependencies
root.order.add_edge(module_setup, monitoring_po)
root.order.add_edge(module_setup, community_po)

# Post‐monitoring & community‐engagement
root.order.add_edge(monitoring_po, reg_compliance)
root.order.add_edge(community_po, reg_compliance)

# After compliance, test & plan maintenance
root.order.add_edge(reg_compliance, system_test)
root.order.add_edge(system_test, maintenance_plan)