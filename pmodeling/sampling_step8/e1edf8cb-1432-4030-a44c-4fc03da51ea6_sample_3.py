import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loop for environmental control
env_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_control, structural_check])

# Define the xor for crop selection
crop_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_select, waste_manage])

# Define the xor for water cycle
water_xor = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, energy_audit])

# Define the xor for lighting adjustment
lighting_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_adjust, market_align])

# Define the xor for harvesting plan
harvest_xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, delivery_setup])

# Define the xor for IoT installation
iot_xor = OperatorPOWL(operator=Operator.XOR, children=[iot_install, sensor_calibrate])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, env_control_loop, crop_xor, iot_xor, water_xor, lighting_xor, harvest_xor])
root.order.add_edge(site_survey, env_control_loop)
root.order.add_edge(env_control_loop, crop_xor)
root.order.add_edge(crop_xor, iot_xor)
root.order.add_edge(iot_xor, water_xor)
root.order.add_edge(water_xor, lighting_xor)
root.order.add_edge(lighting_xor, harvest_xor)