import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Structure_Reinforce, Hydroponic_Setup, Climate_Install, AI_Integration, Seed_Sourcing, Nutrient_Prep, System_Testing, Staff_Training, Crop_Planting, Growth_Monitor, Pest_Control, Harvest_Schedule, Quality_Check, Market_Dispatch, Waste_Recycle, Data_Analysis])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop, skip])
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, loop)