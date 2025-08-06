import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_acq = Transition(label='Site Acquisition')
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

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[impact_assess, modular_setup])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, nutrient_control])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, growth_monitor])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[community_engage, yield_forecast])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[supply_coordinate, compliance_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, energy_optimize])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[market_strategy, performance_review])

root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, loop4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, loop3)
root.order.add_edge(loop3, xor3)
root.order.add_edge(xor3, loop4)