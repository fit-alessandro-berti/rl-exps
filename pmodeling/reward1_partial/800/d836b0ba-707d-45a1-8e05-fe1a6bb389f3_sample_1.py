import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Site_Select = Transition(label='Site Select')
Design_Layout = Transition(label='Design Layout')
Sensor_Integrate = Transition(label='Sensor Integrate')
Crop_Choose = Transition(label='Crop Choose')
Soil_Prepare = Transition(label='Soil Prepare')
Irrigation_Setup = Transition(label='Irrigation Setup')
Pest_Control = Transition(label='Pest Control')
Lighting_Install = Transition(label='Lighting Install')
Staff_Train = Transition(label='Staff Train')
Compliance_Check = Transition(label='Compliance Check')
Market_Analyze = Transition(label='Market Analyze')
Package_Design = Transition(label='Package Design')
Logistics_Plan = Transition(label='Logistics Plan')
Data_Analyze = Transition(label='Data Analyze')
Feedback_Loop = Transition(label='Feedback Loop')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    Site_Select, Design_Layout, Sensor_Integrate, Crop_Choose, Soil_Prepare, Irrigation_Setup,
    Pest_Control, Lighting_Install, Staff_Train, Compliance_Check, Market_Analyze, Package_Design,
    Logistics_Plan, Data_Analyze, Feedback_Loop
])

# Define the dependencies between activities
root.order.add_edge(Site_Select, Design_Layout)
root.order.add_edge(Design_Layout, Sensor_Integrate)
root.order.add_edge(Sensor_Integrate, Crop_Choose)
root.order.add_edge(Crop_Choose, Soil_Prepare)
root.order.add_edge(Soil_Prepare, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Pest_Control)
root.order.add_edge(Pest_Control, Lighting_Install)
root.order.add_edge(Lighting_Install, Staff_Train)
root.order.add_edge(Staff_Train, Compliance_Check)
root.order.add_edge(Compliance_Check, Market_Analyze)
root.order.add_edge(Market_Analyze, Package_Design)
root.order.add_edge(Package_Design, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Data_Analyze)
root.order.add_edge(Data_Analyze, Feedback_Loop)

print(root)