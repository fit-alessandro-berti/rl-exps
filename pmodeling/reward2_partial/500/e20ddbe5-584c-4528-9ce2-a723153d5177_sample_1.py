import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Analysis, Load_Test, Sunlight_Map, Medium_Select, Hydro_Design, Procure_Seeds, Install_Irrigation, Setup_Climate, Create_Schedule, Pest_Control, Monitor_Growth, Adjust_Systems, Harvest_Crops, Package_Produce, Engage_Community, Host_Workshops
])

# Define the dependencies
root.order.add_edge(Site_Analysis, Load_Test)
root.order.add_edge(Site_Analysis, Sunlight_Map)
root.order.add_edge(Load_Test, Medium_Select)
root.order.add_edge(Sunlight_Map, Medium_Select)
root.order.add_edge(Medium_Select, Hydro_Design)
root.order.add_edge(Hydro_Design, Procure_Seeds)
root.order.add_edge(Procure_Seeds, Install_Irrigation)
root.order.add_edge(Install_Irrigation, Setup_Climate)
root.order.add_edge(Setup_Climate, Create_Schedule)
root.order.add_edge(Create_Schedule, Pest_Control)
root.order.add_edge(Pest_Control, Monitor_Growth)
root.order.add_edge(Monitor_Growth, Adjust_Systems)
root.order.add_edge(Adjust_Systems, Harvest_Crops)
root.order.add_edge(Harvest_Crops, Package_Produce)
root.order.add_edge(Package_Produce, Engage_Community)
root.order.add_edge(Engage_Community, Host_Workshops)

# Print the result
print(root)