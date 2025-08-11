import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Acquisition = Transition(label='Site Acquisition')
Impact_Assess = Transition(label='Impact Assess')
Modular_Setup = Transition(label='Modular Setup')
Crop_Planting = Transition(label='Crop Planting')
Nutrient_Control = Transition(label='Nutrient Control')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Community_Engage = Transition(label='Community Engage')
Yield_Forecast = Transition(label='Yield Forecast')
Supply_Coordinate = Transition(label='Supply Coordinate')
Compliance_Check = Transition(label='Compliance Check')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Optimize = Transition(label='Energy Optimize')
Market_Strategy = Transition(label='Market Strategy')
Performance_Review = Transition(label='Performance Review')

# Define silent transitions
skip = SilentTransition()

# Define the loop for infrastructure setup
loop_infrastructure = OperatorPOWL(operator=Operator.LOOP, children=[Modular_Setup, skip])

# Define the XOR for pest control
xor_pest_control = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, skip])

# Define the loop for nutrient control
loop_nutrient_control = OperatorPOWL(operator=Operator.LOOP, children=[Nutrient_Control, skip])

# Define the XOR for community engagement
xor_community_engage = OperatorPOWL(operator=Operator.XOR, children=[Community_Engage, skip])

# Define the XOR for market strategy
xor_market_strategy = OperatorPOWL(operator=Operator.XOR, children=[Market_Strategy, skip])

# Define the loop for performance review
loop_performance_review = OperatorPOWL(operator=Operator.LOOP, children=[Performance_Review, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_infrastructure, loop_nutrient_control, xor_pest_control, xor_community_engage, xor_market_strategy, loop_performance_review])
root.order.add_edge(loop_infrastructure, loop_nutrient_control)
root.order.add_edge(loop_infrastructure, xor_pest_control)
root.order.add_edge(loop_nutrient_control, xor_community_engage)
root.order.add_edge(loop_nutrient_control, xor_market_strategy)
root.order.add_edge(xor_pest_control, loop_performance_review)
root.order.add_edge(xor_community_engage, loop_performance_review)
root.order.add_edge(xor_market_strategy, loop_performance_review)

# Print the root POWL model
print(root)