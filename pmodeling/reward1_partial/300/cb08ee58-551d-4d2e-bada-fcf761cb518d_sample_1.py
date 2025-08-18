import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
light_mapping = Transition(label='Light Mapping')
water_testing = Transition(label='Water Testing')
design_modules = Transition(label='Design Modules')
iot_setup = Transition(label='IoT Setup')
sensor_calibration = Transition(label='Sensor Calibration')
nutrient_mix = Transition(label='Nutrient Mix')
climate_control = Transition(label='Climate Control')
regulatory_check = Transition(label='Regulatory Check')
community_meet = Transition(label='Community Meet')
energy_audit = Transition(label='Energy Audit')
staff_training = Transition(label='Staff Training')
installation = Transition(label='Installation')
system_testing = Transition(label='System Testing')
yield_analysis = Transition(label='Yield Analysis')
resource_audit = Transition(label='Resource Audit')
impact_review = Transition(label='Impact Review')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, light_mapping, water_testing, design_modules, iot_setup, sensor_calibration, nutrient_mix, climate_control, regulatory_check])
xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet, energy_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[staff_training, installation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[system_testing, yield_analysis])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[resource_audit, impact_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[skip])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)

print(root)