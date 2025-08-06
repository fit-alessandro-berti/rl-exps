import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for the modular infrastructure setup
modular_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_setup])

# Define the exclusive choice for nutrient control and pest control
nutrient_pest_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_control, pest_control])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    site_acquisition,
    impact_assess,
    modular_loop,
    crop_planting,
    nutrient_pest_choice,
    growth_monitor,
    community_engage,
    yield_forecast,
    supply_coordinate,
    compliance_check,
    waste_recycle,
    energy_optimize,
    market_strategy,
    performance_review
])

# Add edges to define the order of execution
root.order.add_edge(site_acquisition, impact_assess)
root.order.add_edge(impact_assess, modular_loop)
root.order.add_edge(modular_loop, crop_planting)
root.order.add_edge(crop_planting, nutrient_pest_choice)
root.order.add_edge(nutrient_pest_choice, growth_monitor)
root.order.add_edge(growth_monitor, community_engage)
root.order.add_edge(community_engage, yield_forecast)
root.order.add_edge(yield_forecast, supply_coordinate)
root.order.add_edge(supply_coordinate, compliance_check)
root.order.add_edge(compliance_check, waste_recycle)
root.order.add_edge(waste_recycle, energy_optimize)
root.order.add_edge(energy_optimize, market_strategy)
root.order.add_edge(market_strategy, performance_review)

# Print the root POWL model
print(root)