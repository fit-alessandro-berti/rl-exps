import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Install_Lighting = Transition(label='Install Lighting')
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Select_Crops = Transition(label='Select Crops')
Mix_Nutrients = Transition(label='Mix Nutrients')
Deploy_IoT = Transition(label='Deploy IoT')
Energy_Audit = Transition(label='Energy Audit')
Train_Staff = Transition(label='Train Staff')
Pest_Control = Transition(label='Pest Control')
Legal_Review = Transition(label='Legal Review')
Market_Analysis = Transition(label='Market Analysis')
Plan_Logistics = Transition(label='Plan Logistics')
Yield_Review = Transition(label='Yield Review')

# Define the partial order
root = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Install_Lighting, Setup_Hydroponics, Calibrate_Sensors, Select_Crops, Mix_Nutrients, Deploy_IoT, Energy_Audit, Train_Staff, Pest_Control, Legal_Review, Market_Analysis, Plan_Logistics, Yield_Review])
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Install_Lighting)
root.order.add_edge(Install_Lighting, Setup_Hydroponics)
root.order.add_edge(Setup_Hydroponics, Calibrate_Sensors)
root.order.add_edge(Calibrate_Sensors, Select_Crops)
root.order.add_edge(Select_Crops, Mix_Nutrients)
root.order.add_edge(Mix_Nutrients, Deploy_IoT)
root.order.add_edge(Deploy_IoT, Energy_Audit)
root.order.add_edge(Energy_Audit, Train_Staff)
root.order.add_edge(Train_Staff, Pest_Control)
root.order.add_edge(Pest_Control, Legal_Review)
root.order.add_edge(Legal_Review, Market_Analysis)
root.order.add_edge(Market_Analysis, Plan_Logistics)
root.order.add_edge(Plan_Logistics, Yield_Review)