import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, nutrient_control])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, growth_monitor])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[community_engagement, yield_forecast])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[supply_coordinate, compliance_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, energy_optimize])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[market_strategy, performance_review])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])

# Define the root node as a partial order
root = StrictPartialOrder(nodes=[site_acquisition, impact_assessment, modular_setup, loop1, loop2, loop3, xor1, xor2, xor3, xor4, xor5, xor6, skip])

# Define the partial order dependencies
root.order.add_edge(site_acquisition, impact_assessment)
root.order.add_edge(site_acquisition, modular_setup)
root.order.add_edge(impact_assessment, modular_setup)
root.order.add_edge(modular_setup, loop1)
root.order.add_edge(modular_setup, loop2)
root.order.add_edge(modular_setup, loop3)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop3, xor5)
root.order.add_edge(loop3, xor6)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor1)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor5)
root.order.add_edge(skip, xor1)
root.order.add_edge(skip, xor2)
root.order.add_edge(skip, xor3)
root.order.add_edge(skip, xor4)
root.order.add_edge(skip, xor5)
root.order.add_edge(skip, xor6)

# Print the root node
print(root)