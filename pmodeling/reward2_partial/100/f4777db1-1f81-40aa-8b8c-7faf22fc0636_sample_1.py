import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Survey = Transition(label='Site Survey')
Impact_Study = Transition(label='Impact Study')
Structure_Check = Transition(label='Structure Check')
Soil_Testing = Transition(label='Soil Testing')
System_Design = Transition(label='System Design')
Seed_Selection = Transition(label='Seed Selection')
Irrigation_Setup = Transition(label='Irrigation Setup')
Lighting_Install = Transition(label='Lighting Install')
Pest_Control = Transition(label='Pest Control')
Community_Meet = Transition(label='Community Meet')
Regulation_Review = Transition(label='Regulation Review')
Waste_Plan = Transition(label='Waste Plan')
Crop_Monitor = Transition(label='Crop Monitor')
Harvest_Prep = Transition(label='Harvest Prep')
Market_Launch = Transition(label='Market Launch')

# Define the partial order
root = StrictPartialOrder(nodes=[Site_Survey, Impact_Study, Structure_Check, Soil_Testing, System_Design, Seed_Selection, Irrigation_Setup, Lighting_Install, Pest_Control, Community_Meet, Regulation_Review, Waste_Plan, Crop_Monitor, Harvest_Prep, Market_Launch])

# Define the dependencies between activities
root.order.add_edge(Site_Survey, Impact_Study)
root.order.add_edge(Impact_Study, Structure_Check)
root.order.add_edge(Structure_Check, Soil_Testing)
root.order.add_edge(Soil_Testing, System_Design)
root.order.add_edge(System_Design, Seed_Selection)
root.order.add_edge(Seed_Selection, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Lighting_Install)
root.order.add_edge(Lighting_Install, Pest_Control)
root.order.add_edge(Pest_Control, Community_Meet)
root.order.add_edge(Community_Meet, Regulation_Review)
root.order.add_edge(Regulation_Review, Waste_Plan)
root.order.add_edge(Waste_Plan, Crop_Monitor)
root.order.add_edge(Crop_Monitor, Harvest_Prep)
root.order.add_edge(Harvest_Prep, Market_Launch)

print(root)