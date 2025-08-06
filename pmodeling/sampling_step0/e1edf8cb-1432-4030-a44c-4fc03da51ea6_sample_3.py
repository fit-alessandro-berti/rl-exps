import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the transitions
xor1 = OperatorPOWL(operator=Operator.XOR, children=[env_control, structural_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[hydro_setup, sensor_calibrate])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, nutrient_mix])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[lighting_adjust, staff_train])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, energy_audit])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, delivery_setup])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[market_align, site_survey])

# Define the loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor4])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor5])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[xor6])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[xor7])

# Define the root
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop3, xor4)
root.order.add_edge(loop4, xor5)
root.order.add_edge(loop5, xor6)
root.order.add_edge(loop6, xor7)
root.order.add_edge(loop7, xor1)

# Print the root
print(root)