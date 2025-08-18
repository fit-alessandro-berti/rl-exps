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

site_survey_structure_check = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structure_check])
structure_check_hydroponic_install = OperatorPOWL(operator=Operator.XOR, children=[structure_check, hydroponic_install])
hydroponic_install_lighting_setup = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_install, lighting_setup])
lighting_setup_climate_control = OperatorPOWL(operator=Operator.XOR, children=[lighting_setup, climate_control])
climate_control_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[climate_control, seed_selection])
seed_selection_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])
nutrient_mix_water_recycling = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, water_recycling])
water_recycling_sensor_deploy = OperatorPOWL(operator=Operator.XOR, children=[water_recycling, sensor_deploy])
sensor_deploy_pest_control = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, pest_control])
pest_control_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, growth_monitor])
growth_monitor_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, harvest_plan])
harvest_plan_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, packaging_prep])
packaging_prep_delivery_route = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, delivery_route])
delivery_route_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[delivery_route, data_analysis])
data_analysis_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, yield_forecast])

root = StrictPartialOrder(nodes=[
    site_survey_structure_check,
    structure_check_hydroponic_install,
    hydroponic_install_lighting_setup,
    lighting_setup_climate_control,
    climate_control_seed_selection,
    seed_selection_nutrient_mix,
    nutrient_mix_water_recycling,
    water_recycling_sensor_deploy,
    sensor_deploy_pest_control,
    pest_control_growth_monitor,
    growth_monitor_harvest_plan,
    harvest_plan_packaging_prep,
    packaging_prep_delivery_route,
    delivery_route_data_analysis,
    data_analysis_yield_forecast
])
root.order.add_edge(site_survey_structure_check, structure_check_hydroponic_install)
root.order.add_edge(structure_check_hydroponic_install, hydroponic_install_lighting_setup)
root.order.add_edge(hydroponic_install_lighting_setup, lighting_setup_climate_control)
root.order.add_edge(lighting_setup_climate_control, climate_control_seed_selection)
root.order.add_edge(climate_control_seed_selection, seed_selection_nutrient_mix)
root.order.add_edge(seed_selection_nutrient_mix, nutrient_mix_water_recycling)
root.order.add_edge(nutrient_mix_water_recycling, water_recycling_sensor_deploy)
root.order.add_edge(water_recycling_sensor_deploy, sensor_deploy_pest_control)
root.order.add_edge(sensor_deploy_pest_control, pest_control_growth_monitor)
root.order.add_edge(pest_control_growth_monitor, growth_monitor_harvest_plan)
root.order.add_edge(growth_monitor_harvest_plan, harvest_plan_packaging_prep)
root.order.add_edge(harvest_plan_packaging_prep, packaging_prep_delivery_route)
root.order.add_edge(packaging_prep_delivery_route, delivery_route_data_analysis)
root.order.add_edge(delivery_route_data_analysis, data_analysis_yield_forecast)

print(root)