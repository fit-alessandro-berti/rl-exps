import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_acquisition,
    impact_assessment,
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
# No additional dependencies defined in the given process description
# Therefore, no edges are added in the partial order

# Save the final result in the variable 'root'
print("POWL model for urban vertical farming process:")
print(root)