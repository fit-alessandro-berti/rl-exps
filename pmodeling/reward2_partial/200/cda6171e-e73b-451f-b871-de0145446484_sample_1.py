import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
Site_Analysis = Transition(label='Site Analysis')
Structure_Check = Transition(label='Structure Check')
Modify_Layout = Transition(label='Modify Layout')
Install_HVAC = Transition(label='Install HVAC')
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Prepare_Nutrients = Transition(label='Prepare Nutrients')
Select_Seeds = Transition(label='Select Seeds')
Automate_Planting = Transition(label='Automate Planting')
Deploy_Sensors = Transition(label='Deploy Sensors')
Pest_Control = Transition(label='Pest Control')
Optimize_Energy = Transition(label='Optimize Energy')
Recycle_Water = Transition(label='Recycle Water')
Automate_Harvest = Transition(label='Automate Harvest')
Package_Crops = Transition(label='Package Crops')
Coordinate_Delivery = Transition(label='Coordinate Delivery')
Analyze_Data = Transition(label='Analyze Data')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Site_Analysis, Structure_Check, Modify_Layout, Install_HVAC,
    Setup_Hydroponics, Prepare_Nutrients, Select_Seeds, Automate_Planting,
    Deploy_Sensors, Pest_Control, Optimize_Energy, Recycle_Water, Automate_Harvest,
    Package_Crops, Coordinate_Delivery, Analyze_Data
])

# Define the dependencies
root.order.add_edge(Site_Analysis, Structure_Check)
root.order.add_edge(Structure_Check, Modify_Layout)
root.order.add_edge(Modify_Layout, Install_HVAC)
root.order.add_edge(Install_HVAC, Setup_Hydroponics)
root.order.add_edge(Setup_Hydroponics, Prepare_Nutrients)
root.order.add_edge(Prepare_Nutrients, Select_Seeds)
root.order.add_edge(Select_Seeds, Automate_Planting)
root.order.add_edge(Automate_Planting, Deploy_Sensors)
root.order.add_edge(Deploy_Sensors, Pest_Control)
root.order.add_edge(Pest_Control, Optimize_Energy)
root.order.add_edge(Optimize_Energy, Recycle_Water)
root.order.add_edge(Recycle_Water, Automate_Harvest)
root.order.add_edge(Automate_Harvest, Package_Crops)
root.order.add_edge(Package_Crops, Coordinate_Delivery)
root.order.add_edge(Coordinate_Delivery, Analyze_Data)

print(root)