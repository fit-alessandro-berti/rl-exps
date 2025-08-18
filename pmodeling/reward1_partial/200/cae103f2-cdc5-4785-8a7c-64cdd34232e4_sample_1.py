import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names as given
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting, nutrient_control, pest_control, growth_monitor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[community_engage, yield_forecast, supply_coordinate])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, waste_recycle, energy_optimize])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[market_strategy, performance_review])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])

root = StrictPartialOrder(nodes=[site_acquisition, impact_assess, modular_setup, xor1, xor2, xor3, xor4])
root.order.add_edge(site_acquisition, impact_assess)
root.order.add_edge(impact_assess, modular_setup)
root.order.add_edge(modular_setup, xor1)
root.order.add_edge(modular_setup, xor2)
root.order.add_edge(modular_setup, xor3)
root.order.add_edge(modular_setup, xor4)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop4)