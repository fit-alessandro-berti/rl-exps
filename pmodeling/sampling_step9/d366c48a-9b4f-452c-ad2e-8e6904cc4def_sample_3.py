import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Climate_Scan = Transition(label='Climate Scan')
Module_Setup = Transition(label='Module Setup')
Crop_Choice = Transition(label='Crop Choice')
Nutrient_Feed = Transition(label='Nutrient Feed')
Pest_Control = Transition(label='Pest Control')
Energy_Audit = Transition(label='Energy Audit')
Waste_Cycle = Transition(label='Waste Cycle')
Growth_Track = Transition(label='Growth Track')
Demand_Plan = Transition(label='Demand Plan')
Community_Link = Transition(label='Community Link')
Regulation_Check = Transition(label='Regulation Check')
Supply_Sync = Transition(label='Supply Sync')
System_Upgrade = Transition(label='System Upgrade')
Data_Backup = Transition(label='Data Backup')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Climate_Scan, Module_Setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Nutrient_Feed, Pest_Control, Energy_Audit, Waste_Cycle, Growth_Track, Demand_Plan])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Community_Link, Regulation_Check, Supply_Sync, System_Upgrade, Data_Backup])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop3)