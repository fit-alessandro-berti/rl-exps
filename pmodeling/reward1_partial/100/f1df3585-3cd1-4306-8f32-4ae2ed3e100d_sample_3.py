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
Select_Seed = Transition(label='Select Seeds')
Monitor_Germinate = Transition(label='Monitor Germinate')
Apply_Bio_controls = Transition(label='Apply Bio-controls')
Maintain_Systems = Transition(label='Maintain Systems')
Analyze_Data = Transition(label='Analyze Data')
Harvest_Crops = Transition(label='Harvest Crops')
Quality_Check = Transition(label='Quality Check')
Package_Produce = Transition(label='Package Produce')
Distribute_Goods = Transition(label='Distribute Goods')

# Define silent transitions for concurrent activities
Concurrent_Mix_Nutrients_Calibrate_Sensors = SilentTransition()
Concurrent_Select_Seed_Monitor_Germinate = SilentTransition()
Concurrent_Apply_Bio_controls_Maintain_Systems = SilentTransition()
Concurrent_Analyze_Data_Harvest_Crops = SilentTransition()
Concurrent_Quality_Check_Package_Produce = SilentTransition()

# Define loop for pest management
Pest_Management = OperatorPOWL(operator=Operator.LOOP, children=[Apply_Bio_controls, Maintain_Systems])

# Define choices for concurrent activities
Concurrent_Mix_Nutrients_Calibrate_Sensors = OperatorPOWL(operator=Operator.XOR, children=[Concurrent_Mix_Nutrients_Calibrate_Sensors])
Concurrent_Select_Seed_Monitor_Germinate = OperatorPOWL(operator=Operator.XOR, children=[Concurrent_Select_Seed_Monitor_Germinate])
Concurrent_Apply_Bio_controls_Maintain_Systems = OperatorPOWL(operator=Operator.XOR, children=[Concurrent_Apply_Bio_controls_Maintain_Systems])
Concurrent_Analyze_Data_Harvest_Crops = OperatorPOWL(operator=Operator.XOR, children=[Concurrent_Analyze_Data_Harvest_Crops])
Concurrent_Quality_Check_Package_Produce = OperatorPOWL(operator=Operator.XOR, children=[Concurrent_Quality_Check_Package_Produce])

# Define root POWL model
root = StrictPartialOrder(nodes=[Site_Assess, Plan_Layout, Install_Racks, Concurrent_Mix_Nutrients_Calibrate_Sensors, Concurrent_Select_Seed_Monitor_Germinate, Concurrent_Apply_Bio_controls_Maintain_Systems, Concurrent_Analyze_Data_Harvest_Crops, Concurrent_Quality_Check_Package_Produce, Distribute_Goods, Pest_Management])
root.order.add_edge(Site_Assess, Plan_Layout)
root.order.add_edge(Plan_Layout, Install_Racks)
root.order.add_edge(Install_Racks, Concurrent_Mix_Nutrients_Calibrate_Sensors)
root.order.add_edge(Concurrent_Mix_Nutrients_Calibrate_Sensors, Concurrent_Select_Seed_Monitor_Germinate)
root.order.add_edge(Concurrent_Select_Seed_Monitor_Germinate, Concurrent_Apply_Bio_controls_Maintain_Systems)
root.order.add_edge(Concurrent_Apply_Bio_controls_Maintain_Systems, Concurrent_Analyze_Data_Harvest_Crops)
root.order.add_edge(Concurrent_Analyze_Data_Harvest_Crops, Concurrent_Quality_Check_Package_Produce)
root.order.add_edge(Concurrent_Quality_Check_Package_Produce, Distribute_Goods)
root.order.add_edge(Distribute_Goods, Pest_Management)