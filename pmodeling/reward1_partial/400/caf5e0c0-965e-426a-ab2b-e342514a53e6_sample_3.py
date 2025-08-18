import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
climate_sim = Transition(label='Climate Sim')
seed_select = Transition(label='Seed Select')
module_setup = Transition(label='Module Setup')
nutrient_mix = Transition(label='Nutrient Mix')
water_cycle = Transition(label='Water Cycle')
energy_link = Transition(label='Energy Link')
sensor_install = Transition(label='Sensor Install')
pest_detect = Transition(label='Pest Detect')
growth_scan = Transition(label='Growth Scan')
data_sync = Transition(label='Data Sync')
community_meet = Transition(label='Community Meet')
reg_compliance = Transition(label='Reg Compliance')
system_test = Transition(label='System Test')
maintenance_plan = Transition(label='Maintenance Plan')

# Define partial order
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
    pest_detect,
    growth_scan,
    data_sync,
    community_meet,
    reg_compliance,
    system_test,
    maintenance_plan
])

# Define dependencies
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, climate_sim)
root.order.add_edge(climate_sim, seed_select)
root.order.add_edge(seed_select, module_setup)
root.order.add_edge(module_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, water_cycle)
root.order.add_edge(water_cycle, energy_link)
root.order.add_edge(energy_link, sensor_install)
root.order.add_edge(sensor_install, pest_detect)
root.order.add_edge(pest_detect, growth_scan)
root.order.add_edge(growth_scan, data_sync)
root.order.add_edge(data_sync, community_meet)
root.order.add_edge(community_meet, reg_compliance)
root.order.add_edge(reg_compliance, system_test)
root.order.add_edge(system_test, maintenance_plan)

print(root)