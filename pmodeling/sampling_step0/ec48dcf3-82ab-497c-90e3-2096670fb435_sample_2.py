import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, structure_build, system_install])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_prep, seed_germinate])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[planting_phase, sensor_deploy, pest_control])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[water_monitor, data_analyze])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[staff_train, yield_forecast])
xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, xor])

# Add dependencies
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, xor)

# Print the root
print(root)