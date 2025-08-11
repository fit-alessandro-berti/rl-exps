import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_acquisition = Transition(label='Site Acquisition')
impact_assessment = Transition(label='Impact Assess')
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

# Define the silent activities
skip = SilentTransition()

# Define the loop nodes
modular_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_setup, crop_planting, nutrient_control, pest_control, growth_monitor, community_engage])
supply_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_coordinate, compliance_check, waste_recycle, energy_optimize])
market_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_strategy, performance_review])

# Define the exclusive choices
xor_modular = OperatorPOWL(operator=Operator.XOR, children=[modular_loop, skip])
xor_supply = OperatorPOWL(operator=Operator.XOR, children=[supply_loop, skip])
xor_market = OperatorPOWL(operator=Operator.XOR, children=[market_loop, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_acquisition, impact_assessment, xor_modular, xor_supply, xor_market])
root.order.add_edge(site_acquisition, xor_modular)
root.order.add_edge(site_acquisition, xor_supply)
root.order.add_edge(site_acquisition, xor_market)
root.order.add_edge(impact_assessment, xor_modular)
root.order.add_edge(impact_assessment, xor_supply)
root.order.add_edge(impact_assessment, xor_market)
root.order.add_edge(xor_modular, xor_supply)
root.order.add_edge(xor_modular, xor_market)
root.order.add_edge(xor_supply, xor_market)