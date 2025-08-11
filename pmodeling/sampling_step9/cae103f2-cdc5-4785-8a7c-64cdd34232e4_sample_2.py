import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_acquisition = Transition(label='Site Acquisition')
impact_assessment = Transition(label='Impact Assess')
modular_setup = Transition(label='Modular Setup')
crop_planting = Transition(label='Crop Planting')
nutrient_control = Transition(label='Nutrient Control')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
community_engagement = Transition(label='Community Engage')
yield_forecast = Transition(label='Yield Forecast')
supply_coordinate = Transition(label='Supply Coordinate')
compliance_check = Transition(label='Compliance Check')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
market_strategy = Transition(label='Market Strategy')
performance_review = Transition(label='Performance Review')

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[modular_setup, crop_planting])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_control, pest_control])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, community_engagement])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, supply_coordinate])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, waste_recycle])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[energy_optimize, market_strategy])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[performance_review, skip])

# Define the XOR nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])

# Define the root model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

# Save the final result in the variable 'root'