import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_analysis     = Transition(label='Site Analysis')
structural_check  = Transition(label='Structural Check')
rack_install      = Transition(label='Rack Install')
system_setup      = Transition(label='System Setup')
hydro_config      = Transition(label='Hydroponics Config')
aero_tune         = Transition(label='Aeroponics Tune')
lighting_setup    = Transition(label='Lighting Setup')
enviro_control    = Transition(label='Enviro Control')
sensor_deploy     = Transition(label='Sensor Deploy')
waste_recycle     = Transition(label='Waste Recycle')
water_reuse       = Transition(label='Water Reuse')
staff_training    = Transition(label='Staff Training')
test_grow         = Transition(label='Test Grow')
data_analytics    = Transition(label='Data Analytics')
yield_optimize    = Transition(label='Yield Optimize')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis, structural_check, rack_install,
    system_setup, hydro_config, aero_tune,
    lighting_setup, enviro_control, sensor_deploy,
    waste_recycle, water_reuse, staff_training,
    test_grow, data_analytics, yield_optimize
])

# Define the control-flow dependencies
root.order.add_edge(site_analysis,   structural_check)
root.order.add_edge(structural_check, rack_install)
root.order.add_edge(rack_install,    system_setup)
root.order.add_edge(system_setup,    hydro_config)
root.order.add_edge(system_setup,    aero_tune)
root.order.add_edge(system_setup,    lighting_setup)
root.order.add_edge(system_setup,    enviro_control)
root.order.add_edge(system_setup,    sensor_deploy)
root.order.add_edge(hydro_config,    waste_recycle)
root.order.add_edge(hydro_config,    water_reuse)
root.order.add_edge(aero_tune,       waste_recycle)
root.order.add_edge(aero_tune,       water_reuse)
root.order.add_edge(lighting_setup,  waste_recycle)
root.order.add_edge(lighting_setup,  water_reuse)
root.order.add_edge(enviro_control,  waste_recycle)
root.order.add_edge(enviro_control,  water_reuse)
root.order.add_edge(sensor_deploy,   waste_recycle)
root.order.add_edge(sensor_deploy,   water_reuse)
root.order.add_edge(waste_recycle,   staff_training)
root.order.add_edge(water_reuse,     staff_training)
root.order.add_edge(staff_training,  test_grow)
root.order.add_edge(test_grow,       data_analytics)
root.order.add_edge(data_analytics,  yield_optimize)

print(root)