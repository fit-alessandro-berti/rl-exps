from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Site_Survey = Transition(label='Site Survey')
Env_Assessment = Transition(label='Env Assessment')
Reg_Compliance = Transition(label='Reg Compliance')
Modular_Setup = Transition(label='Modular Setup')
Crop_Selection = Transition(label='Crop Selection')
IoT_Integration = Transition(label='IoT Integration')
Nutrient_Flow = Transition(label='Nutrient Flow')
Light_Calibration = Transition(label='Light Calibration')
Staff_Training = Transition(label='Staff Training')
Pest_Control = Transition(label='Pest Control')
Market_Strategy = Transition(label='Market Strategy')
Logistics_Plan = Transition(label='Logistics Plan')
Yield_Analysis = Transition(label='Yield Analysis')
Data_Review = Transition(label='Data Review')
Community_Engage = Transition(label='Community Engage')

# Define the POWL model
root = StrictPartialOrder(nodes=[Site_Survey, Env_Assessment, Reg_Compliance, Modular_Setup, Crop_Selection, IoT_Integration, Nutrient_Flow, Light_Calibration, Staff_Training, Pest_Control, Market_Strategy, Logistics_Plan, Yield_Analysis, Data_Review, Community_Engage])

# Define the dependencies
root.order.add_edge(Site_Survey, Env_Assessment)
root.order.add_edge(Env_Assessment, Reg_Compliance)
root.order.add_edge(Reg_Compliance, Modular_Setup)
root.order.add_edge(Modular_Setup, Crop_Selection)
root.order.add_edge(Crop_Selection, IoT_Integration)
root.order.add_edge(IoT_Integration, Nutrient_Flow)
root.order.add_edge(Nutrient_Flow, Light_Calibration)
root.order.add_edge(Light_Calibration, Staff_Training)
root.order.add_edge(Staff_Training, Pest_Control)
root.order.add_edge(Pest_Control, Market_Strategy)
root.order.add_edge(Market_Strategy, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Yield_Analysis)
root.order.add_edge(Yield_Analysis, Data_Review)
root.order.add_edge(Data_Review, Community_Engage)

# The final result is in the variable 'root'