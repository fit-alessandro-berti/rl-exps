import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
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

# Define the loop nodes
climate_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_scan, module_setup])
crop_choice_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_choice, nutrient_feed, pest_control])
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, waste_cycle, growth_track])
demand_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_plan, community_link, regulation_check])
supply_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_sync, system_upgrade, data_backup])

# Define the exclusive choices
climate_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_scan_loop, data_backup])
crop_choice_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_choice_loop, data_backup])
energy_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit_loop, data_backup])
demand_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[demand_plan_loop, data_backup])
supply_sync_xor = OperatorPOWL(operator=Operator.XOR, children=[supply_sync_loop, data_backup])

# Define the root node
root = StrictPartialOrder(nodes=[climate_scan, climate_scan_loop, climate_scan_xor, crop_choice, crop_choice_loop, crop_choice_xor, energy_audit, energy_audit_loop, energy_audit_xor, demand_plan, demand_plan_loop, demand_plan_xor, supply_sync, supply_sync_loop, supply_sync_xor, system_upgrade, data_backup])
root.order.add_edge(climate_scan, climate_scan_loop)
root.order.add_edge(climate_scan_loop, climate_scan_xor)
root.order.add_edge(crop_choice, crop_choice_loop)
root.order.add_edge(crop_choice_loop, crop_choice_xor)
root.order.add_edge(energy_audit, energy_audit_loop)
root.order.add_edge(energy_audit_loop, energy_audit_xor)
root.order.add_edge(demand_plan, demand_plan_loop)
root.order.add_edge(demand_plan_loop, demand_plan_xor)
root.order.add_edge(supply_sync, supply_sync_loop)
root.order.add_edge(supply_sync_loop, supply_sync_xor)
root.order.add_edge(system_upgrade, data_backup)