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

# Define silent transitions for skipping certain activities
skip_1 = SilentTransition()
skip_2 = SilentTransition()
skip_3 = SilentTransition()

# Define exclusive choice for nutrient feed and pest control
nutrient_or_pest = OperatorPOWL(operator=Operator.XOR, children=[nutrient_feed, pest_control])

# Define loops for energy audit and waste cycle
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, waste_cycle])

# Define exclusive choice for growth track and demand plan
growth_or_demand = OperatorPOWL(operator=Operator.XOR, children=[growth_track, demand_plan])

# Define loops for community link and regulation check
community_link_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_link, regulation_check])

# Define loops for supply sync and system upgrade
supply_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_sync, system_upgrade])

# Define root node with all activities and loops
root = StrictPartialOrder(nodes=[
    site_survey,
    climate_scan,
    module_setup,
    crop_choice,
    nutrient_or_pest,
    energy_audit_loop,
    waste_cycle,
    growth_or_demand,
    community_link_loop,
    regulation_check,
    supply_sync_loop,
    system_upgrade,
    data_backup
])

# Define dependencies between activities
root.order.add_edge(site_survey, climate_scan)
root.order.add_edge(climate_scan, module_setup)
root.order.add_edge(module_setup, crop_choice)
root.order.add_edge(crop_choice, nutrient_or_pest)
root.order.add_edge(nutrient_or_pest, energy_audit_loop)
root.order.add_edge(energy_audit_loop, waste_cycle)
root.order.add_edge(waste_cycle, growth_or_demand)
root.order.add_edge(growth_or_demand, community_link_loop)
root.order.add_edge(community_link_loop, regulation_check)
root.order.add_edge(regulation_check, supply_sync_loop)
root.order.add_edge(supply_sync_loop, system_upgrade)
root.order.add_edge(system_upgrade, data_backup)

# Print the root node
print(root)