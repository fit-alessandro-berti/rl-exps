from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Structure_Design = Transition(label='Structure Design')
System_Install = Transition(label='System Install')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Config = Transition(label='Climate Config')
AI_Integration = Transition(label='AI Integration')
Nutrient_Sourcing = Transition(label='Nutrient Sourcing')
Waste_Planning = Transition(label='Waste Planning')
Staff_Training = Transition(label='Staff Training')
Crop_Seeding = Transition(label='Crop Seeding')
Growth_Monitoring = Transition(label='Growth Monitoring')
Quality_Testing = Transition(label='Quality Testing')
Harvest_Scheduling = Transition(label='Harvest Scheduling')
Distribution_Plan = Transition(label='Distribution Plan')
Data_Analysis = Transition(label='Data Analysis')

# Define the partial order for the process
root = StrictPartialOrder(nodes=[Site_Survey, Permit_Filing, Structure_Design, System_Install, Hydroponic_Setup, Climate_Config, AI_Integration, Nutrient_Sourcing, Waste_Planning, Staff_Training, Crop_Seeding, Growth_Monitoring, Quality_Testing, Harvest_Scheduling, Distribution_Plan, Data_Analysis])

# Define the order of the nodes
root.order.add_edge(Site_Survey, Permit_Filing)
root.order.add_edge(Permit_Filing, Structure_Design)
root.order.add_edge(Structure_Design, System_Install)
root.order.add_edge(System_Install, Hydroponic_Setup)
root.order.add_edge(Hydroponic_Setup, Climate_Config)
root.order.add_edge(Climate_Config, AI_Integration)
root.order.add_edge(AI_Integration, Nutrient_Sourcing)
root.order.add_edge(Nutrient_Sourcing, Waste_Planning)
root.order.add_edge(Waste_Planning, Staff_Training)
root.order.add_edge(Staff_Training, Crop_Seeding)
root.order.add_edge(Crop_Seeding, Growth_Monitoring)
root.order.add_edge(Growth_Monitoring, Quality_Testing)
root.order.add_edge(Quality_Testing, Harvest_Scheduling)
root.order.add_edge(Harvest_Scheduling, Distribution_Plan)
root.order.add_edge(Distribution_Plan, Data_Analysis)

print(root)