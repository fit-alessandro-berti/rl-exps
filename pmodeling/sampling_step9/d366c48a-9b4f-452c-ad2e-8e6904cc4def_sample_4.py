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

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_scan, module_setup])
crop_choice_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_choice, nutrient_feed])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, energy_audit])
waste_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_cycle, community_link])
demand_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_plan, regulation_check])
supply_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_sync, system_upgrade])
data_backup_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_backup, skip])

# Define exclusive choices
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[climate_loop, demand_plan_loop])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[supply_sync_loop, data_backup_loop])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[exclusive_choice_1, exclusive_choice_2])

# Define the root POWL model
root = StrictPartialOrder(nodes=[exclusive_choice_3])
root.order.add_edge(climate_loop, crop_choice_loop)
root.order.add_edge(crop_choice_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, waste_cycle_loop)
root.order.add_edge(waste_cycle_loop, demand_plan_loop)
root.order.add_edge(demand_plan_loop, supply_sync_loop)
root.order.add_edge(supply_sync_loop, data_backup_loop)
root.order.add_edge(data_backup_loop, exclusive_choice_1)
root.order.add_edge(exclusive_choice_1, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)