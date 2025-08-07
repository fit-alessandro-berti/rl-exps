import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Define the monitoring‐analysis‐growth sub‐process (A)
A = StrictPartialOrder(nodes=[climate_scan, nutrient_feed, pest_control, energy_audit, waste_cycle, growth_track])
A.order.add_edge(climate_scan, nutrient_feed)
A.order.add_edge(climate_scan, pest_control)
A.order.add_edge(climate_scan, energy_audit)
A.order.add_edge(climate_scan, waste_cycle)
A.order.add_edge(nutrient_feed, growth_track)
A.order.add_edge(pest_control, growth_track)
A.order.add_edge(energy_audit, growth_track)
A.order.add_edge(waste_cycle, growth_track)

# Define the supply‐chain‐regulation sub‐process (B)
B = StrictPartialOrder(nodes=[demand_plan, community_link, regulation_check, supply_sync])
B.order.add_edge(demand_plan, community_link)
B.order.add_edge(demand_plan, regulation_check)
B.order.add_edge(community_link, supply_sync)
B.order.add_edge(regulation_check, supply_sync)

# Define the loop: do A, then optionally do B and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Assemble the overall process
root = StrictPartialOrder(nodes=[site_survey, loop, data_backup])
root.order.add_edge(site_survey, loop)
root.order.add_edge(loop, data_backup)