import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) using the given names
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

# Define the partial order (POWL model)
root = StrictPartialOrder(nodes=[
    site_acquisition,
    impact_assess,
    modular_setup,
    crop_planting,
    nutrient_control,
    pest_control,
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

# Print the root to see the defined POWL model
print(root)