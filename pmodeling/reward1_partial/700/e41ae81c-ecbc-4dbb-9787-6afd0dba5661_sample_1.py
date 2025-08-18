import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
Site_Survey = Transition(label='Site Survey')
Structure_Reinforce = Transition(label='Structure Reinforce')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Install = Transition(label='Climate Install')
AI_Integration = Transition(label='AI Integration')
Seed_Sourcing = Transition(label='Seed Sourcing')
Nutrient_Prep = Transition(label='Nutrient Prep')
System_Testing = Transition(label='System Testing')
Staff_Training = Transition(label='Staff Training')
Crop_Planting = Transition(label='Crop Planting')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Schedule = Transition(label='Harvest Schedule')
Quality_Check = Transition(label='Quality Check')
Market_Dispatch = Transition(label='Market Dispatch')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Analysis = Transition(label='Data Analysis')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Structure_Reinforce,
    Hydroponic_Setup,
    Climate_Install,
    AI_Integration,
    Seed_Sourcing,
    Nutrient_Prep,
    System_Testing,
    Staff_Training,
    Crop_Planting,
    Growth_Monitor,
    Pest_Control,
    Harvest_Schedule,
    Quality_Check,
    Market_Dispatch,
    Waste_Recycle,
    Data_Analysis
])

# Add dependencies between activities
root.order.add_edge(Site_Survey, Structure_Reinforce)
root.order.add_edge(Structure_Reinforce, Hydroponic_Setup)
root.order.add_edge(Hydroponic_Setup, Climate_Install)
root.order.add_edge(Climate_Install, AI_Integration)
root.order.add_edge(AI_Integration, Seed_Sourcing)
root.order.add_edge(Seed_Sourcing, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, System_Testing)
root.order.add_edge(System_Testing, Staff_Training)
root.order.add_edge(Staff_Training, Crop_Planting)
root.order.add_edge(Crop_Planting, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Pest_Control)
root.order.add_edge(Pest_Control, Harvest_Schedule)
root.order.add_edge(Harvest_Schedule, Quality_Check)
root.order.add_edge(Quality_Check, Market_Dispatch)
root.order.add_edge(Market_Dispatch, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Data_Analysis)

# Print the POWL model
print(root)