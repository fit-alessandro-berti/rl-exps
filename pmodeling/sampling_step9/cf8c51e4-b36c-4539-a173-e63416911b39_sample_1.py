import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Site_Analysis = Transition(label='Site Analysis')
Zoning_Approval = Transition(label='Zoning Approval')
Structural_Check = Transition(label='Structural Check')
Building_Retrofit = Transition(label='Building Retrofit')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Control = Transition(label='Climate Control')
Nutrient_Design = Transition(label='Nutrient Design')
Staff_Hiring = Transition(label='Staff Hiring')
Staff_Training = Transition(label='Staff Training')
Software_Install = Transition(label='Software Install')
System_Testing = Transition(label='System Testing')
Crop_Planting = Transition(label='Crop Planting')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')

# Define the transitions between activities
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Structural_Check, Building_Retrofit])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Hydroponic_Setup, Climate_Control, Nutrient_Design])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Staff_Hiring, Staff_Training])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Software_Install, System_Testing])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Planting, Growth_Monitor])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, Harvest_Plan])

# Create the root POWL model
root = StrictPartialOrder(nodes=[Site_Analysis, Zoning_Approval, loop1, xor1, loop2, xor2, loop3, xor3])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)