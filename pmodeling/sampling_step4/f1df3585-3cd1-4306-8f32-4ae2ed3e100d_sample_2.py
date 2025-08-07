from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
Site_Assess = Transition(label='Site Assess')
Plan_Layout = Transition(label='Plan Layout')
Install_Racks = Transition(label='Install Racks')
Mix_Nutrients = Transition(label='Mix Nutrients')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Setup_Lighting = Transition(label='Setup Lighting')
Configure_Climate = Transition(label='Configure Climate')
Select_Seeds = Transition(label='Select Seeds')
Monitor_Germinate = Transition(label='Monitor Germinate')
Apply_Bio_controls = Transition(label='Apply Bio-controls')
Maintain_Systems = Transition(label='Maintain Systems')
Analyze_Data = Transition(label='Analyze Data')
Harvest_Crops = Transition(label='Harvest Crops')
Quality_Check = Transition(label='Quality Check')
Package_Produce = Transition(label='Package Produce')
Distribute_Goods = Transition(label='Distribute Goods')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Assess, Plan_Layout, Install_Racks, Mix_Nutrients, Calibrate_Sensors,
    Setup_Lighting, Configure_Climate, Select_Seeds, Monitor_Germinate, Apply_Bio_controls,
    Maintain_Systems, Analyze_Data, Harvest_Crops, Quality_Check, Package_Produce, Distribute_Goods
])

# Define the order relationships between the nodes
root.order.add_edge(Site_Assess, Plan_Layout)
root.order.add_edge(Plan_Layout, Install_Racks)
root.order.add_edge(Install_Racks, Mix_Nutrients)
root.order.add_edge(Mix_Nutrients, Calibrate_Sensors)
root.order.add_edge(Calibrate_Sensors, Setup_Lighting)
root.order.add_edge(Setup_Lighting, Configure_Climate)
root.order.add_edge(Configure_Climate, Select_Seeds)
root.order.add_edge(Select_Seeds, Monitor_Germinate)
root.order.add_edge(Monitor_Germinate, Apply_Bio_controls)
root.order.add_edge(Apply_Bio_controls, Maintain_Systems)
root.order.add_edge(Maintain_Systems, Analyze_Data)
root.order.add_edge(Analyze_Data, Harvest_Crops)
root.order.add_edge(Harvest_Crops, Quality_Check)
root.order.add_edge(Quality_Check, Package_Produce)
root.order.add_edge(Package_Produce, Distribute_Goods)

print(root)