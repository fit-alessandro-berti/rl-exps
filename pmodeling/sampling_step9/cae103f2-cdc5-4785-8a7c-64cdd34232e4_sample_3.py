import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_acquisition = Transition(label='Site Acquisition')
impact_assess = Transition(label='Impact Assess')
modular_setup = Transition(label='Modular Setup')
crop_planting = Transition(label='Crop Planting')
nutrient_control = Transition(label='Nutrient Control')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
community_engage = Transition(label='Community Engage')
yield_forecast = Transition(label='Yield Forecast')
supply_coordinate = Transition(label='Supply Coordinate')
compliance_check = Transition(label='Compliance Check')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
market_strategy = Transition(label='Market Strategy')
performance_review = Transition(label='Performance Review')

# Define silent transitions
skip = SilentTransition()

# Define loops and XORs
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting, nutrient_control])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, growth_monitor])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[community_engage, yield_forecast])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[supply_coordinate, compliance_check])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, energy_optimize])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[market_strategy, performance_review])

xor_1 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_2, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, skip])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[loop_4, skip])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[loop_5, skip])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[loop_6, skip])

# Define root
root = StrictPartialOrder(nodes=[site_acquisition, impact_assess, modular_setup, xor_1, xor_2, xor_3, xor_4, xor_5, xor_6])
root.order.add_edge(site_acquisition, impact_assess)
root.order.add_edge(impact_assess, modular_setup)
root.order.add_edge(modular_setup, xor_1)
root.order.add_edge(modular_setup, xor_2)
root.order.add_edge(modular_setup, xor_3)
root.order.add_edge(modular_setup, xor_4)
root.order.add_edge(modular_setup, xor_5)
root.order.add_edge(modular_setup, xor_6)
root.order.add_edge(xor_1, loop_1)
root.order.add_edge(xor_2, loop_2)
root.order.add_edge(xor_3, loop_3)
root.order.add_edge(xor_4, loop_4)
root.order.add_edge(xor_5, loop_5)
root.order.add_edge(xor_6, loop_6)