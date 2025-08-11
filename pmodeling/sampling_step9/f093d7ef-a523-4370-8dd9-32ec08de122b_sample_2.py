import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Module_Build = Transition(label='Module Build')
System_Install = Transition(label='System Install')
Water_Prepare = Transition(label='Water Prep')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Scan = Transition(label='Pest Scan')
Growth_Monitor = Transition(label='Growth Monitor')
Data_Sync = Transition(label='Data Sync')
Energy_Manage = Transition(label='Energy Manage')
Harvest_Plan = Transition(label='Harvest Plan')
Community_Link = Transition(label='Community Link')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Design_Layout])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Module_Build, System_Install])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Water_Prepare, Seed_Selection])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Nutrient_Mix, Climate_Setup])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Sensor_Deploy, Pest_Scan])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, Data_Sync])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Energy_Manage, Harvest_Plan])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Community_Link, skip])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop5, loop6])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop7, loop8])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor1)