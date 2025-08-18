from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Site_Survey = Transition(label='Site Survey')
Energy_Partner = Transition(label='Energy Partner')
Permit_Filing = Transition(label='Permit Filing')
Hydro_Unit = Transition(label='Hydro Unit')
AI_Setup = Transition(label='AI Setup')
Nutrient_Plan = Transition(label='Nutrient Plan')
System_Install = Transition(label='System Install')
Crop_Testing = Transition(label='Crop Testing')
Data_Analysis = Transition(label='Data Analysis')
Community_Meet = Transition(label='Community Meet')
Yield_Adjust = Transition(label='Yield Adjust')
Carbon_Audit = Transition(label='Carbon Audit')
Logistics_Plan = Transition(label='Logistics Plan')
Quality_Check = Transition(label='Quality Check')
Scale_Review = Transition(label='Scale Review')

skip = SilentTransition()

# Define the partial order
root = StrictPartialOrder(nodes=[Site_Survey, Energy_Partner, Permit_Filing, Hydro_Unit, AI_Setup, Nutrient_Plan, System_Install, Crop_Testing, Data_Analysis, Community_Meet, Yield_Adjust, Carbon_Audit, Logistics_Plan, Quality_Check, Scale_Review])

# Define the dependencies
root.order.add_edge(Site_Survey, Energy_Partner)
root.order.add_edge(Energy_Partner, Permit_Filing)
root.order.add_edge(Permit_Filing, Hydro_Unit)
root.order.add_edge(Hydro_Unit, AI_Setup)
root.order.add_edge(AI_Setup, Nutrient_Plan)
root.order.add_edge(Nutrient_Plan, System_Install)
root.order.add_edge(System_Install, Crop_Testing)
root.order.add_edge(Crop_Testing, Data_Analysis)
root.order.add_edge(Data_Analysis, Community_Meet)
root.order.add_edge(Community_Meet, Yield_Adjust)
root.order.add_edge(Yield_Adjust, Carbon_Audit)
root.order.add_edge(Carbon_Audit, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Quality_Check)
root.order.add_edge(Quality_Check, Scale_Review)

# Return the root
return root