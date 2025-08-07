import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root of the POWL model as a strict partial order
root = StrictPartialOrder(nodes=[
    Site_Assess,
    Plan_Layout,
    Install_Racks,
    Mix_Nutrients,
    Calibrate_Sensors,
    Setup_Lighting,
    Configure_Climate,
    Select_Seeds,
    Monitor_Germinate,
    Apply_Bio_controls,
    Maintain_Systems,
    Analyze_Data,
    Harvest_Crops,
    Quality_Check,
    Package_Produce,
    Distribute_Goods
])

# Add dependencies if any, for example, 'Plan Layout' depends on 'Site Assess'
root.order.add_edge(Site_Assess, Plan_Layout)
root.order.add_edge(Site_Assess, Install_Racks)
root.order.add_edge(Site_Assess, Mix_Nutrients)
root.order.add_edge(Site_Assess, Calibrate_Sensors)
root.order.add_edge(Site_Assess, Setup_Lighting)
root.order.add_edge(Site_Assess, Configure_Climate)
root.order.add_edge(Site_Assess, Select_Seeds)
root.order.add_edge(Site_Assess, Monitor_Germinate)
root.order.add_edge(Site_Assess, Apply_Bio_controls)
root.order.add_edge(Site_Assess, Maintain_Systems)
root.order.add_edge(Site_Assess, Analyze_Data)
root.order.add_edge(Site_Assess, Harvest_Crops)
root.order.add_edge(Site_Assess, Quality_Check)
root.order.add_edge(Site_Assess, Package_Produce)
root.order.add_edge(Site_Assess, Distribute_Goods)

# Now, 'root' contains the POWL model for the urban vertical farm process.