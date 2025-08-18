import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
structure_build = Transition(label='Structure Build')
system_install = Transition(label='System Install')
climate_setup = Transition(label='Climate Setup')
nutrient_prep = Transition(label='Nutrient Prep')
seed_germinate = Transition(label='Seed Germinate')
planting_phase = Transition(label='Planting Phase')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control = Transition(label='Pest Control')
water_monitor = Transition(label='Water Monitor')
data_analyze = Transition(label='Data Analyze')
staff_train = Transition(label='Staff Train')
yield_forecast = Transition(label='Yield Forecast')
community_meet = Transition(label='Community Meet')

skip = SilentTransition()

site_survey_xor_design_layout = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
structure_build_xor_system_install = OperatorPOWL(operator=Operator.XOR, children=[structure_build, system_install])
climate_setup_xor_nutrient_prep = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_prep])
seed_germinate_xor_planting_phase = OperatorPOWL(operator=Operator.XOR, children=[seed_germinate, planting_phase])
sensor_deploy_xor_pest_control = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, pest_control])
water_monitor_xor_data_analyze = OperatorPOWL(operator=Operator.XOR, children=[water_monitor, data_analyze])
staff_train_xor_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[staff_train, yield_forecast])
community_meet_xor_skip = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])

root = StrictPartialOrder(nodes=[site_survey_xor_design_layout, structure_build_xor_system_install, climate_setup_xor_nutrient_prep, seed_germinate_xor_planting_phase, sensor_deploy_xor_pest_control, water_monitor_xor_data_analyze, staff_train_xor_yield_forecast, community_meet_xor_skip])
root.order.add_edge(site_survey_xor_design_layout, structure_build_xor_system_install)
root.order.add_edge(structure_build_xor_system_install, climate_setup_xor_nutrient_prep)
root.order.add_edge(climate_setup_xor_nutrient_prep, seed_germinate_xor_planting_phase)
root.order.add_edge(seed_germinate_xor_planting_phase, sensor_deploy_xor_pest_control)
root.order.add_edge(sensor_deploy_xor_pest_control, water_monitor_xor_data_analyze)
root.order.add_edge(water_monitor_xor_data_analyze, staff_train_xor_yield_forecast)
root.order.add_edge(staff_train_xor_yield_forecast, community_meet_xor_skip)