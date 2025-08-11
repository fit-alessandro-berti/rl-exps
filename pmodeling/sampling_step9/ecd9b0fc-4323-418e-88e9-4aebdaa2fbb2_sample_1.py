import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process structure
loop_climate_control = OperatorPOWL(operator=Operator.LOOP, children=[climate_control])
loop_pest_control = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
loop_growth_monitor = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor])
loop_data_analysis = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis])

xor_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, skip])
xor_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])

xor_delivery_route = OperatorPOWL(operator=Operator.XOR, children=[delivery_route, skip])

xor_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, skip])

xor_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])

loop_water_recycling = OperatorPOWL(operator=Operator.LOOP, children=[water_recycling])

loop_sensor_deploy = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy])

loop_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])

loop_hydroponic_install = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_install])

xor_lighting_setup = OperatorPOWL(operator=Operator.XOR, children=[lighting_setup, skip])

loop_structure_check = OperatorPOWL(operator=Operator.LOOP, children=[structure_check])

loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])

root = StrictPartialOrder(nodes=[loop_site_survey, loop_structure_check, loop_hydroponic_install, loop_lighting_setup, xor_lighting_setup, loop_climate_control, loop_pest_control, loop_growth_monitor, loop_data_analysis, xor_data_analysis, loop_water_recycling, loop_sensor_deploy, loop_nutrient_mix, loop_hydroponic_install, xor_harvest_plan, xor_yield_forecast, xor_packaging_prep, xor_delivery_route])

root.order.add_edge(loop_site_survey, loop_structure_check)
root.order.add_edge(loop_structure_check, loop_hydroponic_install)
root.order.add_edge(loop_hydroponic_install, xor_lighting_setup)
root.order.add_edge(xor_lighting_setup, loop_climate_control)
root.order.add_edge(loop_climate_control, loop_pest_control)
root.order.add_edge(loop_pest_control, loop_growth_monitor)
root.order.add_edge(loop_growth_monitor, loop_data_analysis)
root.order.add_edge(loop_data_analysis, xor_data_analysis)
root.order.add_edge(xor_data_analysis, loop_water_recycling)
root.order.add_edge(loop_water_recycling, loop_sensor_deploy)
root.order.add_edge(loop_sensor_deploy, loop_nutrient_mix)
root.order.add_edge(loop_nutrient_mix, loop_hydroponic_install)
root.order.add_edge(loop_hydroponic_install, xor_harvest_plan)
root.order.add_edge(xor_harvest_plan, xor_yield_forecast)
root.order.add_edge(xor_yield_forecast, xor_packaging_prep)
root.order.add_edge(xor_packaging_prep, xor_delivery_route)