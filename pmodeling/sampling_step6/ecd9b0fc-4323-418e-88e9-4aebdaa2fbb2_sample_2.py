import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
hydroponic_install = Transition(label='Hydroponic Install')
lighting_setup = Transition(label='Lighting Setup')
climate_control = Transition(label='Climate Control')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
water_recycling = Transition(label='Water Recycling')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
packaging_prep = Transition(label='Packaging Prep')
delivery_route = Transition(label='Delivery Route')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')

root = StrictPartialOrder(nodes=[
    site_survey,
    structure_check,
    hydroponic_install,
    lighting_setup,
    climate_control,
    seed_selection,
    nutrient_mix,
    water_recycling,
    sensor_deploy,
    pest_control,
    growth_monitor,
    harvest_plan,
    packaging_prep,
    delivery_route,
    data_analysis,
    yield_forecast
])