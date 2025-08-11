import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the urban vertical farming process
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
env_control = Transition(label='Env Control')
hydro_setup = Transition(label='Hydro Setup')
crop_select = Transition(label='Crop Select')
iot_install = Transition(label='IoT Install')
sensor_calibrate = Transition(label='Sensor Calibrate')
water_cycle = Transition(label='Water Cycle')
nutrient_mix = Transition(label='Nutrient Mix')
lighting_adjust = Transition(label='Lighting Adjust')
staff_train = Transition(label='Staff Train')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')
harvest_plan = Transition(label='Harvest Plan')
delivery_setup = Transition(label='Delivery Setup')
market_align = Transition(label='Market Align')

# Define the POWL model
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_check])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[env_control, hydro_setup])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[crop_select, iot_install])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[sensor_calibrate, water_cycle])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, lighting_adjust])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[staff_train, waste_manage])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, harvest_plan])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[delivery_setup, market_align])
xor_8 = OperatorPOWL(operator=Operator.XOR, children=[xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_1, xor_8])
root.order.add_edge(loop_1, xor_8)

# Print the root of the POWL model
print(root)