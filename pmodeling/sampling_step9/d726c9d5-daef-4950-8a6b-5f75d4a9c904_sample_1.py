import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
soil_sample = Transition(label='Soil Sample')
water_test = Transition(label='Water Test')
crop_selection = Transition(label='Crop Selection')
material_order = Transition(label='Material Order')
planter_setup = Transition(label='Planter Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy = Transition(label='Sensor Deploy')
solar_setup = Transition(label='Solar Setup')
data_integration = Transition(label='Data Integration')
community_meet = Transition(label='Community Meet')
training_session = Transition(label='Training Session')
yield_monitor = Transition(label='Yield Monitor')
adjust_plan = Transition(label='Adjust Plan')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structure_check, soil_sample, water_test, crop_selection])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[material_order, planter_setup, irrigation_install, sensor_deploy, solar_setup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[data_integration, community_meet, training_session, yield_monitor, adjust_plan])

xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop3, xor)

print(root)