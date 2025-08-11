import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
Site_Analysis = Transition(label='Site Analysis')
Env_Scanning = Transition(label='Env Scanning')
Farm_Design = Transition(label='Farm Design')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Automation = Transition(label='Seed Automation')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
AI_Diagnostics = Transition(label='AI Diagnostics')
Harvest_Plan = Transition(label='Harvest Plan')
Robotic_Sort = Transition(label='Robotic Sort')
Packaging_Line = Transition(label='Packaging Line')
Community_Input = Transition(label='Community Input')
Data_Aggregation = Transition(label='Data Aggregation')
Waste_Recycle = Transition(label='Waste Recycle')
Sustainability = Transition(label='Sustainability')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Site_Analysis, Env_Scanning, Farm_Design, Nutrient_Mix,
    Seed_Automation, Growth_Monitor, Pest_Control, AI_Diagnostics,
    Harvest_Plan, Robotic_Sort, Packaging_Line, Community_Input,
    Data_Aggregation, Waste_Recycle, Sustainability
])

# Define the dependencies
root.order.add_edge(Site_Analysis, Env_Scanning)
root.order.add_edge(Env_Scanning, Farm_Design)
root.order.add_edge(Farm_Design, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Seed_Automation)
root.order.add_edge(Seed_Automation, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Pest_Control)
root.order.add_edge(Pest_Control, AI_Diagnostics)
root.order.add_edge(AI_Diagnostics, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Robotic_Sort)
root.order.add_edge(Robotic_Sort, Packaging_Line)
root.order.add_edge(Packaging_Line, Community_Input)
root.order.add_edge(Community_Input, Data_Aggregation)
root.order.add_edge(Data_Aggregation, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Sustainability)

print(root)