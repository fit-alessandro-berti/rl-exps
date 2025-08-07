import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define dependencies if any
# For example, if site acquisition must happen before impact assessment:
# root.order.add_edge(site_acquisition, impact_assess)

# If the process is sequential, no need to define dependencies as they are implied by the order of nodes in the root.