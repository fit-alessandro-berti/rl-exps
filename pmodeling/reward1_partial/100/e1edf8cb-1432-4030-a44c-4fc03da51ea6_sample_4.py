import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define loops and XORs for the process
site_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_check])
env_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_control, hydro_setup])
crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_select, iot_install])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibrate, water_cycle])
nutrient_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, lighting_adjust])
staff_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_train, waste_manage])
energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, harvest_plan])
delivery_loop = OperatorPOWL(operator=Operator.LOOP, children=[delivery_setup, market_align])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    site_loop,
    env_loop,
    crop_loop,
    sensor_loop,
    nutrient_loop,
    staff_loop,
    energy_loop,
    delivery_loop
])

# Define the dependencies between nodes
root.order.add_edge(site_loop, env_loop)
root.order.add_edge(env_loop, crop_loop)
root.order.add_edge(crop_loop, sensor_loop)
root.order.add_edge(sensor_loop, nutrient_loop)
root.order.add_edge(nutrient_loop, staff_loop)
root.order.add_edge(staff_loop, energy_loop)
root.order.add_edge(energy_loop, delivery_loop)

# Print the root partial order
print(root)