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

site_survey_process = StrictPartialOrder(nodes=[site_survey, structure_check])
site_survey_process.order.add_edge(site_survey, structure_check)

structure_check_process = StrictPartialOrder(nodes=[structure_check, hydroponic_install, lighting_setup])
structure_check_process.order.add_edge(structure_check, hydroponic_install)
structure_check_process.order.add_edge(hydroponic_install, lighting_setup)

hydroponic_install_process = StrictPartialOrder(nodes=[hydroponic_install, climate_control, nutrient_mix, water_recycling])
hydroponic_install_process.order.add_edge(hydroponic_install, climate_control)
hydroponic_install_process.order.add_edge(climate_control, nutrient_mix)
hydroponic_install_process.order.add_edge(nutrient_mix, water_recycling)

climate_control_process = StrictPartialOrder(nodes=[climate_control, sensor_deploy, pest_control, growth_monitor])
climate_control_process.order.add_edge(climate_control, sensor_deploy)
climate_control_process.order.add_edge(sensor_deploy, pest_control)
climate_control_process.order.add_edge(pest_control, growth_monitor)

sensor_deploy_process = StrictPartialOrder(nodes=[sensor_deploy, harvest_plan, packaging_prep, delivery_route])
sensor_deploy_process.order.add_edge(sensor_deploy, harvest_plan)
sensor_deploy_process.order.add_edge(harvest_plan, packaging_prep)
sensor_deploy_process.order.add_edge(packaging_prep, delivery_route)

harvest_plan_process = StrictPartialOrder(nodes=[harvest_plan, data_analysis, yield_forecast])
harvest_plan_process.order.add_edge(harvest_plan, data_analysis)
harvest_plan_process.order.add_edge(data_analysis, yield_forecast)

root = StrictPartialOrder(nodes=[site_survey_process, structure_check_process, hydroponic_install_process, climate_control_process, sensor_deploy_process, harvest_plan_process])
root.order.add_edge(site_survey_process, structure_check_process)
root.order.add_edge(structure_check_process, hydroponic_install_process)
root.order.add_edge(hydroponic_install_process, climate_control_process)
root.order.add_edge(climate_control_process, sensor_deploy_process)
root.order.add_edge(sensor_deploy_process, harvest_plan_process)
root.order.add_edge(harvest_plan_process, data_analysis_process)
root.order.add_edge(data_analysis_process, yield_forecast_process)