import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
Seed_Select = Transition(label='Seed Select')
Germinate_Seeds = Transition(label='Germinate Seeds')
Transplant_Seedlings = Transition(label='Transplant Seedlings')
Mix_Nutrients = Transition(label='Mix Nutrients')
Adjust_pH = Transition(label='Adjust pH')
Monitor_Climate = Transition(label='Monitor Climate')
Control_Humidity = Transition(label='Control Humidity')
CO2_Regulation = Transition(label='CO2 Regulation')
Detect_Pests = Transition(label='Detect Pests')
Deploy_Biocontrols = Transition(label='Deploy Biocontrols')
Schedule_Harvest = Transition(label='Schedule Harvest')
Automate_Picking = Transition(label='Automate Picking')
Package_Produce = Transition(label='Package Produce')
Compost_Waste = Transition(label='Compost Waste')
Recycle_Water = Transition(label='Recycle Water')
Data_Logging = Transition(label='Data Logging')
System_Maintenance = Transition(label='System Maintenance')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Seed_Select, 
    Germinate_Seeds, 
    Transplant_Seedlings, 
    Mix_Nutrients, 
    Adjust_pH, 
    Monitor_Climate, 
    Control_Humidity, 
    CO2_Regulation, 
    Detect_Pests, 
    Deploy_Biocontrols, 
    Schedule_Harvest, 
    Automate_Picking, 
    Package_Produce, 
    Compost_Waste, 
    Recycle_Water, 
    Data_Logging, 
    System_Maintenance
])

# Define the order of execution
root.order.add_edge(Seed_Select, Germinate_Seeds)
root.order.add_edge(Germinate_Seeds, Transplant_Seedlings)
root.order.add_edge(Transplant_Seedlings, Mix_Nutrients)
root.order.add_edge(Mix_Nutrients, Adjust_pH)
root.order.add_edge(Adjust_pH, Monitor_Climate)
root.order.add_edge(Monitor_Climate, Control_Humidity)
root.order.add_edge(Control_Humidity, CO2_Regulation)
root.order.add_edge(CO2_Regulation, Detect_Pests)
root.order.add_edge(Detect_Pests, Deploy_Biocontrols)
root.order.add_edge(Deploy_Biocontrols, Schedule_Harvest)
root.order.add_edge(Schedule_Harvest, Automate_Picking)
root.order.add_edge(Automate_Picking, Package_Produce)
root.order.add_edge(Package_Produce, Compost_Waste)
root.order.add_edge(Compost_Waste, Recycle_Water)
root.order.add_edge(Recycle_Water, Data_Logging)
root.order.add_edge(Data_Logging, System_Maintenance)

print(root)