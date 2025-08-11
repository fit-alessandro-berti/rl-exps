import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_water_cycle = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle, nutrient_mix])
loop_lighting = OperatorPOWL(operator=Operator.LOOP, children=[lighting_adjust, energy_audit])

# Define exclusive choices
xor_setup = OperatorPOWL(operator=Operator.XOR, children=[delivery_setup, market_align])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    env_control,
    hydro_setup,
    crop_select,
    iot_install,
    sensor_calibrate,
    loop_water_cycle,
    loop_lighting,
    xor_setup,
    staff_train,
    waste_manage
])
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, env_control)
root.order.add_edge(env_control, hydro_setup)
root.order.add_edge(hydro_setup, crop_select)
root.order.add_edge(crop_select, iot_install)
root.order.add_edge(iot_install, sensor_calibrate)
root.order.add_edge(sensor_calibrate, loop_water_cycle)
root.order.add_edge(loop_water_cycle, loop_lighting)
root.order.add_edge(loop_lighting, xor_setup)
root.order.add_edge(xor_setup, staff_train)
root.order.add_edge(staff_train, waste_manage)

print(root)