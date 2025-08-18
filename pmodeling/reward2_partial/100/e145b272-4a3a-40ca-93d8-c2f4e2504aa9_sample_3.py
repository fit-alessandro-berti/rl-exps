import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
System_Design = Transition(label='System Design')
Permit_Filing = Transition(label='Permit Filing')
Modular_Build = Transition(label='Modular Build')
Sensor_Install = Transition(label='Sensor Install')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Waste_Setup = Transition(label='Waste Setup')
IoT_Deploy = Transition(label='IoT Deploy')
AI_Scheduling = Transition(label='AI Scheduling')
Energy_Audit = Transition(label='Energy Audit')
Compliance_Check = Transition(label='Compliance Check')
Crop_Planting = Transition(label='Crop Planting')
Yield_Monitor = Transition(label='Yield Monitor')
Data_Analysis = Transition(label='Data Analysis')
System_Upgrade = Transition(label='System Upgrade')

# Define the partial order of the process
root = StrictPartialOrder(nodes=[Site_Survey, System_Design, Permit_Filing, Modular_Build, Sensor_Install, Climate_Setup, Nutrient_Mix, Waste_Setup, IoT_Deploy, AI_Scheduling, Energy_Audit, Compliance_Check, Crop_Planting, Yield_Monitor, Data_Analysis, System_Upgrade])

# Define the order of the partial order
root.order.add_edge(Site_Survey, System_Design)
root.order.add_edge(System_Design, Permit_Filing)
root.order.add_edge(Permit_Filing, Modular_Build)
root.order.add_edge(Modular_Build, Sensor_Install)
root.order.add_edge(Sensor_Install, Climate_Setup)
root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Waste_Setup)
root.order.add_edge(Waste_Setup, IoT_Deploy)
root.order.add_edge(IoT_Deploy, AI_Scheduling)
root.order.add_edge(AI_Scheduling, Energy_Audit)
root.order.add_edge(Energy_Audit, Compliance_Check)
root.order.add_edge(Compliance_Check, Crop_Planting)
root.order.add_edge(Crop_Planting, Yield_Monitor)
root.order.add_edge(Yield_Monitor, Data_Analysis)
root.order.add_edge(Data_Analysis, System_Upgrade)