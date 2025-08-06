import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define loop nodes
crop_planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting, nutrient_control, pest_control, growth_monitor])
yield_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, performance_review])

# Define XOR nodes
supply_coordinate_xor = OperatorPOWL(operator=Operator.XOR, children=[supply_coordinate, skip])
waste_recycle_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, skip])
energy_optimize_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_optimize, skip])

# Define partial order
root = StrictPartialOrder(nodes=[site_acquisition, impact_assess, modular_setup, crop_planting_loop, supply_coordinate_xor, waste_recycle_xor, energy_optimize_xor, yield_forecast_loop, community_engage, compliance_check, market_strategy, performance_review])
root.order.add_edge(site_acquisition, impact_assess)
root.order.add_edge(impact_assess, modular_setup)
root.order.add_edge(modular_setup, crop_planting_loop)
root.order.add_edge(crop_planting_loop, supply_coordinate_xor)
root.order.add_edge(supply_coordinate_xor, waste_recycle_xor)
root.order.add_edge(waste_recycle_xor, energy_optimize_xor)
root.order.add_edge(energy_optimize_xor, yield_forecast_loop)
root.order.add_edge(yield_forecast_loop, community_engage)
root.order.add_edge(community_engage, compliance_check)
root.order.add_edge(compliance_check, market_strategy)
root.order.add_edge(market_strategy, performance_review)