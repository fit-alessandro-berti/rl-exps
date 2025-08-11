import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent activities
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Water_Prepare, Seed_Selection, Nutrient_Mix, Climate_Setup, Sensor_Deploy, Pest_Scan, Growth_Monitor, Data_Sync, Energy_Manage, Harvest_Plan, Community_Link])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Design_Layout, Module_Build, System_Install])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)

print(root)