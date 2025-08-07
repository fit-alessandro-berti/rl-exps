import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
site_analysis    = Transition(label='Site Analysis')
structural_check = Transition(label='Structural Check')
rack_install     = Transition(label='Rack Install')
system_setup     = Transition(label='System Setup')
hydro_setup      = Transition(label='Hydroponics Config')
aero_setup       = Transition(label='Aeroponics Tune')
lighting_setup   = Transition(label='Lighting Setup')
enviro_control   = Transition(label='Enviro Control')
sensor_deploy    = Transition(label='Sensor Deploy')
waste_recycle    = Transition(label='Waste Recycle')
water_reuse      = Transition(label='Water Reuse')
staff_training   = Transition(label='Staff Training')
test_grow        = Transition(label='Test Grow')
data_analytics   = Transition(label='Data Analytics')
yield_optimize   = Transition(label='Yield Optimize')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    structural_check,
    rack_install,
    system_setup,
    hydro_setup,
    aero_setup,
    lighting_setup,
    enviro_control,
    sensor_deploy,
    waste_recycle,
    water_reuse,
    staff_training,
    test_grow,
    data_analytics,
    yield_optimize
])

# Add control-flow edges
root.order.add_edge(site_analysis,    structural_check)
root.order.add_edge(structural_check, rack_install)
root.order.add_edge(rack_install,     system_setup)
root.order.add_edge(system_setup,     hydro_setup)
root.order.add_edge(system_setup,     aero_setup)
root.order.add_edge(hydro_setup,      lighting_setup)
root.order.add_edge(aero_setup,       lighting_setup)
root.order.add_edge(lighting_setup,   enviro_control)
root.order.add_edge(enviro_control,   sensor_deploy)
root.order.add_edge(sensor_deploy,    waste_recycle)
root.order.add_edge(sensor_deploy,    water_reuse)
root.order.add_edge(waste_recycle,    staff_training)
root.order.add_edge(water_reuse,      staff_training)
root.order.add_edge(staff_training,   test_grow)
root.order.add_edge(test_grow,        data_analytics)
root.order.add_edge(data_analytics,   yield_optimize)