import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
Site_Survey = Transition(label='Site Survey')
Structure_Assess = Transition(label='Structure Assess')
System_Design = Transition(label='System Design')
Crop_Select = Transition(label='Crop Select')
Permit_Obtain = Transition(label='Permit Obtain')
Enviro_Setup = Transition(label='Enviro Setup')
Irrigation_Plan = Transition(label='Irrigation Plan')
Sensor_Install = Transition(label='Sensor Install')
AI_Calibration = Transition(label='AI Calibration')
Staff_Train = Transition(label='Staff Train')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Monitor = Transition(label='Pest Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Market_Align = Transition(label='Market Align')
Launch_Farm = Transition(label='Launch Farm')

root = StrictPartialOrder(nodes=[Site_Survey, Structure_Assess, System_Design, Crop_Select, Permit_Obtain, Enviro_Setup, Irrigation_Plan, Sensor_Install, AI_Calibration, Staff_Train, Nutrient_Mix, Pest_Monitor, Yield_Analyze, Market_Align, Launch_Farm])

# Define the dependencies between activities
root.order.add_edge(Site_Survey, Structure_Assess)
root.order.add_edge(Structure_Assess, System_Design)
root.order.add_edge(System_Design, Crop_Select)
root.order.add_edge(Crop_Select, Permit_Obtain)
root.order.add_edge(Permit_Obtain, Enviro_Setup)
root.order.add_edge(Enviro_Setup, Irrigation_Plan)
root.order.add_edge(Irrigation_Plan, Sensor_Install)
root.order.add_edge(Sensor_Install, AI_Calibration)
root.order.add_edge(AI_Calibration, Staff_Train)
root.order.add_edge(Staff_Train, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Pest_Monitor)
root.order.add_edge(Pest_Monitor, Yield_Analyze)
root.order.add_edge(Yield_Analyze, Market_Align)
root.order.add_edge(Market_Align, Launch_Farm)