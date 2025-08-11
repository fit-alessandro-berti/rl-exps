import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop and XOR nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Permit_Filing, Structure_Design])
xor = OperatorPOWL(operator=Operator.XOR, children=[Hydroponic_Setup, Climate_Config, AI_Integration, Nutrient_Sourcing, Waste_Planning, Staff_Training, Crop_Seeding, Growth_Monitoring, Quality_Testing, Harvest_Scheduling, Distribution_Plan, Data_Analysis])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)