import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
climate_scan     = Transition(label='Climate Scan')
module_setup     = Transition(label='Module Setup')
crop_choice      = Transition(label='Crop Choice')
nutrient_feed    = Transition(label='Nutrient Feed')
pest_control     = Transition(label='Pest Control')
energy_audit     = Transition(label='Energy Audit')
waste_cycle      = Transition(label='Waste Cycle')
growth_track     = Transition(label='Growth Track')
demand_plan      = Transition(label='Demand Plan')
community_link   = Transition(label='Community Link')
regulation_check = Transition(label='Regulation Check')
supply_sync      = Transition(label='Supply Sync')
system_upgrade   = Transition(label='System Upgrade')
data_backup      = Transition(label='Data Backup')

# Build the loop body for continuous monitoring and optimization
body = StrictPartialOrder(nodes=[growth_track, demand_plan, community_link,
                                 regulation_check, supply_sync, system_upgrade, data_backup])
body.order.add_edge(growth_track, demand_plan)
body.order.add_edge(demand_plan, community_link)
body.order.add_edge(community_link, regulation_check)
body.order.add_edge(regulation_check, supply_sync)
body.order.add_edge(supply_sync, system_upgrade)
body.order.add_edge(system_upgrade, data_backup)

# Define the loop: do Module Setup, then optionally do the body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[module_setup, body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[site_survey, climate_scan, loop,
                                 nutrient_feed, pest_control, energy_audit,
                                 waste_cycle])
root.order.add_edge(site_survey, climate_scan)
root.order.add_edge(climate_scan, loop)
root.order.add_edge(loop, nutrient_feed)
root.order.add_edge(nutrient_feed, pest_control)
root.order.add_edge(pest_control, energy_audit)
root.order.add_edge(energy_audit, waste_cycle)