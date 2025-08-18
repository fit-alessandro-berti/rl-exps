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

# Site Analysis and Structural Check
root = StrictPartialOrder(nodes=[site_analysis, structural_check])
root.order.add_edge(site_analysis, structural_check)

# Rack Install
root = StrictPartialOrder(nodes=[rack_install])
root.order.add_edge(site_analysis, rack_install)

# System Setup
root = StrictPartialOrder(nodes=[system_setup])
root.order.add_edge(structural_check, system_setup)

# Hydroponics Config
root = StrictPartialOrder(nodes=[hydroponics_config])
root.order.add_edge(system_setup, hydroponics_config)

# Aeroponics Tune
root = StrictPartialOrder(nodes=[aeroponics_tune])
root.order.add_edge(hydroponics_config, aeroponics_tune)

# Lighting Setup
root = StrictPartialOrder(nodes=[lighting_setup])
root.order.add_edge(aeroponics_tune, lighting_setup)

# Enviro Control
root = StrictPartialOrder(nodes=[enviro_control])
root.order.add_edge(lighting_setup, enviro_control)

# Sensor Deploy
root = StrictPartialOrder(nodes=[sensor_deploy])
root.order.add_edge(enviro_control, sensor_deploy)

# Waste Recycle
root = StrictPartialOrder(nodes=[waste_recycle])
root.order.add_edge(sensor_deploy, waste_recycle)

# Water Reuse
root = StrictPartialOrder(nodes=[water_reuse])
root.order.add_edge(waste_recycle, water_reuse)

# Staff Training
root = StrictPartialOrder(nodes=[staff_training])
root.order.add_edge(water_reuse, staff_training)

# Test Grow
root = StrictPartialOrder(nodes=[test_grow])
root.order.add_edge(staff_training, test_grow)

# Data Analytics
root = StrictPartialOrder(nodes=[data_analytics])
root.order.add_edge(test_grow, data_analytics)

# Yield Optimize
root = StrictPartialOrder(nodes=[yield_optimize])
root.order.add_edge(data_analytics, yield_optimize)