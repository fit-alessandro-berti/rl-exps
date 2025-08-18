import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loop for modular setup and nutrient control
loop_modular = OperatorPOWL(operator=Operator.LOOP, children=[modular_setup, nutrient_control])
loop_modular.order.add_edge(modular_setup, nutrient_control)

# Define exclusive choice for pest control and growth monitor
xor_pest_growth = OperatorPOWL(operator=Operator.XOR, children=[pest_control, growth_monitor])
xor_pest_growth.order.add_edge(pest_control, growth_monitor)

# Define exclusive choice for community engage and yield forecast
xor_community_yield = OperatorPOWL(operator=Operator.XOR, children=[community_engage, yield_forecast])
xor_community_yield.order.add_edge(community_engage, yield_forecast)

# Define exclusive choice for supply coordinate and compliance check
xor_supply_check = OperatorPOWL(operator=Operator.XOR, children=[supply_coordinate, compliance_check])
xor_supply_check.order.add_edge(supply_coordinate, compliance_check)

# Define exclusive choice for waste recycle and energy optimize
xor_waste_energy = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, energy_optimize])
xor_waste_energy.order.add_edge(waste_recycle, energy_optimize)

# Define exclusive choice for market strategy and performance review
xor_market_review = OperatorPOWL(operator=Operator.XOR, children=[market_strategy, performance_review])
xor_market_review.order.add_edge(market_strategy, performance_review)

# Define root with all activities
root = StrictPartialOrder(nodes=[site_acquisition, impact_assess, loop_modular, xor_pest_growth, xor_community_yield, xor_supply_check, xor_waste_energy, xor_market_review])
root.order.add_edge(site_acquisition, impact_assess)
root.order.add_edge(impact_assess, loop_modular)
root.order.add_edge(loop_modular, xor_pest_growth)
root.order.add_edge(xor_pest_growth, xor_community_yield)
root.order.add_edge(xor_community_yield, xor_supply_check)
root.order.add_edge(xor_supply_check, xor_waste_energy)
root.order.add_edge(xor_waste_energy, xor_market_review)
root.order.add_edge(xor_market_review, performance_review)

print(root)