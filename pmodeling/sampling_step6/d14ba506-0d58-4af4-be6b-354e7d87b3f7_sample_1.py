import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[site_analysis, structural_check, rack_install, system_setup, hydroponics_config, aeroponics_tune, lighting_setup, enviro_control, sensor_deploy, waste_recycle, water_reuse, staff_training, test_grow, data_analytics, yield_optimize])

# Add dependencies between activities
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(site_analysis, rack_install)
root.order.add_edge(site_analysis, system_setup)
root.order.add_edge(system_setup, hydroponics_config)
root.order.add_edge(system_setup, aeroponics_tune)
root.order.add_edge(system_setup, lighting_setup)
root.order.add_edge(system_setup, enviro_control)
root.order.add_edge(system_setup, sensor_deploy)
root.order.add_edge(system_setup, waste_recycle)
root.order.add_edge(system_setup, water_reuse)
root.order.add_edge(system_setup, staff_training)
root.order.add_edge(system_setup, test_grow)
root.order.add_edge(system_setup, data_analytics)
root.order.add_edge(system_setup, yield_optimize)

# Print the root model
print(root)