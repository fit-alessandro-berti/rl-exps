import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
light_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_mapping, water_testing])
water_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_testing, light_mapping])
modules_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_modules, light_loop, water_loop])
iot_loop = OperatorPOWL(operator=Operator.LOOP, children=[iot_setup, sensor_calibration, nutrient_mix, climate_control])
regulatory_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_check, community_meet])
energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, staff_training, installation, system_testing, yield_analysis, resource_audit, impact_review])

# Define partial order
root = StrictPartialOrder(nodes=[light_loop, water_loop, modules_loop, iot_loop, regulatory_loop, energy_loop])
root.order.add_edge(light_loop, water_loop)
root.order.add_edge(water_loop, light_loop)
root.order.add_edge(modules_loop, iot_loop)
root.order.add_edge(iot_loop, regulatory_loop)
root.order.add_edge(regulatory_loop, energy_loop)

# Print the result
print(root)