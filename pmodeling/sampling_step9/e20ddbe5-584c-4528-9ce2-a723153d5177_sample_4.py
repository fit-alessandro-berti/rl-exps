import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Analysis = Transition(label='Site Analysis')
Load_Test = Transition(label='Load Test')
Sunlight_Map = Transition(label='Sunlight Map')
Medium_Select = Transition(label='Medium Select')
Hydro_Design = Transition(label='Hydro Design')
Procure_Seeds = Transition(label='Procure Seeds')
Install_Irrigation = Transition(label='Install Irrigation')
Setup_Climate = Transition(label='Setup Climate')
Create_Schedule = Transition(label='Create Schedule')
Pest_Control = Transition(label='Pest Control')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Systems = Transition(label='Adjust Systems')
Harvest_Crops = Transition(label='Harvest Crops')
Package_Produce = Transition(label='Package Produce')
Engage_Community = Transition(label='Engage Community')
Host_Workshops = Transition(label='Host Workshops')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_site_analysis = OperatorPOWL(operator=Operator.LOOP, children=[Site_Analysis, Load_Test, Sunlight_Map])
loop_medium_select = OperatorPOWL(operator=Operator.LOOP, children=[Medium_Select, Hydro_Design, Procure_Seeds, Install_Irrigation, Setup_Climate, Create_Schedule, Pest_Control, Monitor_Growth, Adjust_Systems])
loop_harvest = OperatorPOWL(operator=Operator.LOOP, children=[Harvest_Crops, Package_Produce, Engage_Community, Host_Workshops])

# Define partial order
root = StrictPartialOrder(nodes=[loop_site_analysis, loop_medium_select, loop_harvest])
root.order.add_edge(loop_site_analysis, loop_medium_select)
root.order.add_edge(loop_medium_select, loop_harvest)

# Print the final result
print(root)