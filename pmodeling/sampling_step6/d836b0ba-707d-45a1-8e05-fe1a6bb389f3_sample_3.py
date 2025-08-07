import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root POWL model as a strict partial order
root = StrictPartialOrder(nodes=[
    Site_Select,
    Design_Layout,
    Sensor_Integrate,
    Crop_Choose,
    Soil_Prepare,
    Irrigation_Setup,
    Pest_Control,
    Lighting_Install,
    Staff_Train,
    Compliance_Check,
    Market_Analyze,
    Package_Design,
    Logistics_Plan,
    Data_Analyze,
    Feedback_Loop
])

# Print the root model
print(root)