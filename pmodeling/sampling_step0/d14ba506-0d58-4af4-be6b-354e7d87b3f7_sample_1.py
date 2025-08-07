import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_analysis = Transition(label='Site Analysis')
structural_check = Transition(label='Structural Check')
rack_install = Transition(label='Rack Install')
system_setup = Transition(label='System Setup')
hydroponics_config = Transition(label='Hydroponics Config')
aeroponics_tune = Transition(label='Aeroponics Tune')
lighting_setup = Transition(label='Lighting Setup')
enviro_control = Transition(label='Enviro Control')
sensor_deploy = Transition(label='Sensor Deploy')
waste_recycle = Transition(label='Waste Recycle')
water_reuse = Transition(label='Water Reuse')
staff_training = Transition(label='Staff Training')
test_grow = Transition(label='Test Grow')
data_analytics = Transition(label='Data Analytics')
yield_optimize = Transition(label='Yield Optimize')

skip = SilentTransition()

# Establish a partial order for site analysis, structural check, and rack install
site_analysis_and_structural_check = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, structural_check])
rack_install_and_system_setup = OperatorPOWL(operator=Operator.XOR, children=[rack_install, system_setup])

# Establish a loop for system setup and test grow
loop = OperatorPOWL(operator=Operator.LOOP, children=[system_setup, test_grow])

# Establish a loop for yield optimization
yield_optimize_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_optimize])

# Establish a partial order for hydroponics configuration, aeroponics tuning, lighting setup, and environment control
hydroponics_config_and_aeroponics_tune = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_config, aeroponics_tune])
lighting_setup_and_enviro_control = OperatorPOWL(operator=Operator.XOR, children=[lighting_setup, enviro_control])
sensor_deploy_and_waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, waste_recycle])
water_reuse_and_staff_training = OperatorPOWL(operator=Operator.XOR, children=[water_reuse, staff_training])

# Establish a partial order for data analytics
data_analytics_and_yield_optimize = OperatorPOWL(operator=Operator.XOR, children=[data_analytics, yield_optimize_loop])

# Create the root partial order
root = StrictPartialOrder(nodes=[
    site_analysis_and_structural_check,
    rack_install_and_system_setup,
    loop,
    hydroponics_config_and_aeroponics_tune,
    lighting_setup_and_enviro_control,
    sensor_deploy_and_waste_recycle,
    water_reuse_and_staff_training,
    data_analytics_and_yield_optimize
])
root.order.add_edge(site_analysis_and_structural_check, rack_install_and_system_setup)
root.order.add_edge(rack_install_and_system_setup, loop)
root.order.add_edge(loop, hydroponics_config_and_aeroponics_tune)
root.order.add_edge(hydroponics_config_and_aeroponics_tune, lighting_setup_and_enviro_control)
root.order.add_edge(lighting_setup_and_enviro_control, sensor_deploy_and_waste_recycle)
root.order.add_edge(sensor_deploy_and_waste_recycle, water_reuse_and_staff_training)
root.order.add_edge(water_reuse_and_staff_training, data_analytics_and_yield_optimize)
root.order.add_edge(data_analytics_and_yield_optimize, yield_optimize_loop)