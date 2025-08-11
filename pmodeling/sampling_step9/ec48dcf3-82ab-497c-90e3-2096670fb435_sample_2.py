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

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[system_install, climate_setup, nutrient_prep])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[seed_germinate, planting_phase])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, pest_control, water_monitor])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, staff_train])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, community_meet])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[structure_build, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop3, loop5)
root.order.add_edge(loop4, loop1)
root.order.add_edge(loop5, loop2)

print(root)