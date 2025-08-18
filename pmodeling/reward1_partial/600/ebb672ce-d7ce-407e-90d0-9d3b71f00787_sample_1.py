import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
modular_build = Transition(label='Modular Build')
install_pumps = Transition(label='Install Pumps')
setup_sensors = Transition(label='Setup Sensors')
calibrate_lights = Transition(label='Calibrate Lights')
nutrient_mix = Transition(label='Nutrient Mix')
plant_seeding = Transition(label='Plant Seeding')
water_cycling = Transition(label='Water Cycling')
energy_audit = Transition(label='Energy Audit')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')
supply_order = Transition(label='Supply Order')
waste_recycle = Transition(label='Waste Recycle')
system_upgrade = Transition(label='System Upgrade')

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, modular_build])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[setup_sensors, calibrate_lights, nutrient_mix, plant_seeding, water_cycling])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, energy_audit, growth_monitor, data_analysis, yield_forecast, supply_order, waste_recycle])
upgrade_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_upgrade])

root = StrictPartialOrder(nodes=[site_survey_loop, sensor_loop, pest_loop, upgrade_loop])
root.order.add_edge(site_survey_loop, sensor_loop)
root.order.add_edge(sensor_loop, pest_loop)
root.order.add_edge(pest_loop, upgrade_loop)

print(root)