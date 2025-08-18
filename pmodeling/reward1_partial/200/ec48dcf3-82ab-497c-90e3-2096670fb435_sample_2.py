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

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, structure_build, system_install])
climate_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_prep, seed_germinate])
planting_phase_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_phase, sensor_deploy, pest_control, water_monitor, data_analyze])
staff_train_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_train, yield_forecast, community_meet])

root = StrictPartialOrder(nodes=[site_survey_loop, climate_setup_loop, planting_phase_loop, staff_train_loop])
root.order.add_edge(site_survey_loop, climate_setup_loop)
root.order.add_edge(climate_setup_loop, planting_phase_loop)
root.order.add_edge(planting_phase_loop, staff_train_loop)