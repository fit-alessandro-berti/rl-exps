import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey    = Transition(label='Site Survey')
light_mapping  = Transition(label='Light Mapping')
water_testing  = Transition(label='Water Testing')
design_modules = Transition(label='Design Modules')
iot_setup      = Transition(label='IoT Setup')
sensor_cal     = Transition(label='Sensor Calibration')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_ctrl   = Transition(label='Climate Control')
regulatory_chk = Transition(label='Regulatory Check')
community_meet = Transition(label='Community Meet')
energy_audit   = Transition(label='Energy Audit')
staff_train    = Transition(label='Staff Training')
installation   = Transition(label='Installation')
system_test    = Transition(label='System Testing')
yield_analysis = Transition(label='Yield Analysis')
resource_audit = Transition(label='Resource Audit')
impact_review  = Transition(label='Impact Review')

# Define the resource audit loop: audit resources, then optionally review impact and repeat
loop_resource = OperatorPOWL(
    operator=Operator.LOOP,
    children=[resource_audit, impact_review]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, light_mapping, water_testing, design_modules,
    iot_setup, sensor_cal, nutrient_mix, climate_ctrl, regulatory_chk,
    community_meet, energy_audit, staff_train, installation, system_test,
    yield_analysis, loop_resource
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, light_mapping)
root.order.add_edge(site_survey, water_testing)
root.order.add_edge(light_mapping, design_modules)
root.order.add_edge(water_testing, design_modules)
root.order.add_edge(design_modules, iot_setup)
root.order.add_edge(iot_setup, sensor_cal)
root.order.add_edge(iot_setup, nutrient_mix)
root.order.add_edge(iot_setup, climate_ctrl)
root.order.add_edge(sensor_cal, regulatory_chk)
root.order.add_edge(nutrient_mix, regulatory_chk)
root.order.add_edge(climate_ctrl, regulatory_chk)
root.order.add_edge(regulatory_chk, community_meet)
root.order.add_edge(community_meet, energy_audit)
root.order.add_edge(energy_audit, staff_train)
root.order.add_edge(staff_train, installation)
root.order.add_edge(installation, system_test)
root.order.add_edge(system_test, yield_analysis)
root.order.add_edge(system_test, loop_resource)

# The loop_resource branch can occur after any system_test activity
for activity in [yield_analysis, system_test]:
    root.order.add_edge(activity, loop_resource)