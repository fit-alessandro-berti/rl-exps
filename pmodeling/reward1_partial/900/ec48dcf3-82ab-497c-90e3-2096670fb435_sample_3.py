import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the loop nodes
planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_phase, sensor_deploy, pest_control, water_monitor, data_analyze])
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_train])

# Define the exclusive choice nodes
setup_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_prep, seed_germinate])
nutrient_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, seed_germinate])
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, water_monitor])
monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, staff_train])
forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, community_meet])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, design_layout, structure_build, system_install, setup_choice, planting_loop, nutrient_choice, pest_choice, monitor_choice, forecast_choice, staff_training_loop])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, system_install)
root.order.add_edge(system_install, setup_choice)
root.order.add_edge(setup_choice, nutrient_choice)
root.order.add_edge(nutrient_choice, pest_choice)
root.order.add_edge(pest_choice, monitor_choice)
root.order.add_edge(monitor_choice, forecast_choice)
root.order.add_edge(forecast_choice, staff_training_loop)
root.order.add_edge(staff_training_loop, planting_loop)