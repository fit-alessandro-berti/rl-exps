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

skip = SilentTransition()

site_survey_to_structure_check = OperatorPOWL(operator=Operator.XOR, children=[structure_check, skip])
structure_check_to_hydroponic_install = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_install, skip])
hydroponic_install_to_lighting_setup = OperatorPOWL(operator=Operator.XOR, children=[lighting_setup, skip])
lighting_setup_to_climate_control = OperatorPOWL(operator=Operator.XOR, children=[climate_control, skip])
climate_control_to_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, skip])
seed_selection_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
nutrient_mix_to_water_recycling = OperatorPOWL(operator=Operator.XOR, children=[water_recycling, skip])
water_recycling_to_sensor_deploy = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, skip])
sensor_deploy_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
pest_control_to_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])
growth_monitor_to_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, skip])
harvest_plan_to_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
packaging_prep_to_delivery_route = OperatorPOWL(operator=Operator.XOR, children=[delivery_route, skip])
delivery_route_to_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip])
data_analysis_to_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])

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

root.order.add_edge(site_survey, structure_check)
root.order.add_edge(structure_check, hydroponic_install)
root.order.add_edge(hydroponic_install, lighting_setup)
root.order.add_edge(lighting_setup, climate_control)
root.order.add_edge(climate_control, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, water_recycling)
root.order.add_edge(water_recycling, sensor_deploy)
root.order.add_edge(sensor_deploy, pest_control)
root.order.add_edge(pest_control, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, packaging_prep)
root.order.add_edge(packaging_prep, delivery_route)
root.order.add_edge(delivery_route, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)