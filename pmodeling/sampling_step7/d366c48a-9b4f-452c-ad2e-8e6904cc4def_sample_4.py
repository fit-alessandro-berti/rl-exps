import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
climate_scan = Transition(label='Climate Scan')
module_setup = Transition(label='Module Setup')
crop_choice = Transition(label='Crop Choice')
nutrient_feed = Transition(label='Nutrient Feed')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
waste_cycle = Transition(label='Waste Cycle')
growth_track = Transition(label='Growth Track')
demand_plan = Transition(label='Demand Plan')
community_link = Transition(label='Community Link')
regulation_check = Transition(label='Regulation Check')
supply_sync = Transition(label='Supply Sync')
system_upgrade = Transition(label='System Upgrade')
data_backup = Transition(label='Data Backup')

# Define partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    climate_scan,
    module_setup,
    crop_choice,
    nutrient_feed,
    pest_control,
    energy_audit,
    waste_cycle,
    growth_track,
    demand_plan,
    community_link,
    regulation_check,
    supply_sync,
    system_upgrade,
    data_backup
])

# Define dependencies
root.order.add_edge(site_survey, climate_scan)
root.order.add_edge(climate_scan, module_setup)
root.order.add_edge(module_setup, crop_choice)
root.order.add_edge(crop_choice, nutrient_feed)
root.order.add_edge(nutrient_feed, pest_control)
root.order.add_edge(pest_control, energy_audit)
root.order.add_edge(energy_audit, waste_cycle)
root.order.add_edge(waste_cycle, growth_track)
root.order.add_edge(growth_track, demand_plan)
root.order.add_edge(demand_plan, community_link)
root.order.add_edge(community_link, regulation_check)
root.order.add_edge(regulation_check, supply_sync)
root.order.add_edge(supply_sync, system_upgrade)
root.order.add_edge(system_upgrade, data_backup)

print(root)