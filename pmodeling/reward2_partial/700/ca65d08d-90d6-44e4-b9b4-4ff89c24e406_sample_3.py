from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
System_Build = Transition(label='System Build')
Install_Sensors = Transition(label='Install Sensors')
Select_Crops = Transition(label='Select Crops')
Setup_Lighting = Transition(label='Setup Lighting')
Configure_Climate = Transition(label='Configure Climate')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automate_Watering = Transition(label='Automate Watering')
Test_Systems = Transition(label='Test Systems')
Train_Staff = Transition(label='Train Staff')
Waste_Plan = Transition(label='Waste Plan')
Market_Link = Transition(label='Market Link')
Data_Monitor = Transition(label='Data Monitor')
Optimize_Yield = Transition(label='Optimize Yield')

# Define the partial order
root = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, System_Build, Install_Sensors, Select_Crops, Setup_Lighting, Configure_Climate, Nutrient_Mix, Automate_Watering, Test_Systems, Train_Staff, Waste_Plan, Market_Link, Data_Monitor, Optimize_Yield])

# Define the dependencies between nodes
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, System_Build)
root.order.add_edge(System_Build, Install_Sensors)
root.order.add_edge(Install_Sensors, Select_Crops)
root.order.add_edge(Select_Crops, Setup_Lighting)
root.order.add_edge(Setup_Lighting, Configure_Climate)
root.order.add_edge(Configure_Climate, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Automate_Watering)
root.order.add_edge(Automate_Watering, Test_Systems)
root.order.add_edge(Test_Systems, Train_Staff)
root.order.add_edge(Train_Staff, Waste_Plan)
root.order.add_edge(Waste_Plan, Market_Link)
root.order.add_edge(Market_Link, Data_Monitor)
root.order.add_edge(Data_Monitor, Optimize_Yield)