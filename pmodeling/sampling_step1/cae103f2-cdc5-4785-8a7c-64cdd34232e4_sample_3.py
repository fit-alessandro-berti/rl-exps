from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the activities
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

# Define the partial order
root.nodes.extend([site_acquisition, impact_assessment, modular_setup, crop_planting, nutrient_control, pest_control, growth_monitor, community_engagement, yield_forecast, supply_coordinate, compliance_check, waste_recycle, energy_optimize, market_strategy, performance_review])

# Define the order of activities
root.order.add_edge(site_acquisition, impact_assessment)
root.order.add_edge(impact_assessment, modular_setup)
root.order.add_edge(modular_setup, crop_planting)
root.order.add_edge(crop_planting, nutrient_control)
root.order.add_edge(nutrient_control, pest_control)
root.order.add_edge(pest_control, growth_monitor)
root.order.add_edge(growth_monitor, community_engagement)
root.order.add_edge(community_engagement, yield_forecast)
root.order.add_edge(yield_forecast, supply_coordinate)
root.order.add_edge(supply_coordinate, compliance_check)
root.order.add_edge(compliance_check, waste_recycle)
root.order.add_edge(waste_recycle, energy_optimize)
root.order.add_edge(energy_optimize, market_strategy)
root.order.add_edge(market_strategy, performance_review)

# Print the final POWL model
print(root)