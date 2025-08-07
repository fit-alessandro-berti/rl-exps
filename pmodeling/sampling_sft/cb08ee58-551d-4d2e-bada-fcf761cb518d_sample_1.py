import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
light_mapping    = Transition(label='Light Mapping')
water_testing    = Transition(label='Water Testing')
design_modules   = Transition(label='Design Modules')
iot_setup        = Transition(label='IoT Setup')
sensor_cal       = Transition(label='Sensor Calibration')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_control  = Transition(label='Climate Control')
regulatory_check = Transition(label='Regulatory Check')
community_meet   = Transition(label='Community Meet')
energy_audit     = Transition(label='Energy Audit')
staff_training   = Transition(label='Staff Training')
installation     = Transition(label='Installation')
system_testing   = Transition(label='System Testing')
yield_analysis   = Transition(label='Yield Analysis')
resource_audit   = Transition(label='Resource Audit')
impact_review    = Transition(label='Impact Review')

# Loop for continuous performance optimization after installation
# Body A: Yield Analysis -> Resource Audit -> Impact Review
body_A = StrictPartialOrder(nodes=[yield_analysis, resource_audit, impact_review])
body_A.order.add_edge(yield_analysis, resource_audit)
body_A.order.add_edge(resource_audit, impact_review)

# Body B: repeat: Yield Analysis -> Resource Audit -> Impact Review
#        then exit
body_B = StrictPartialOrder(nodes=[yield_analysis, resource_audit, impact_review])
body_B.order.add_edge(yield_analysis, resource_audit)
body_B.order.add_edge(resource_audit, impact_review)

# Loop: Installation -> Body A (then exit), then Body B repeated
loop = OperatorPOWL(operator=Operator.LOOP, children=[installation, body_A, body_B])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, light_mapping, water_testing, design_modules,
    iot_setup, sensor_cal, nutrient_mix, climate_control,
    regulatory_check, community_meet, energy_audit,
    staff_training, installation, loop
])

# Sequential dependencies
root.order.add_edge(site_survey, light_mapping)
root.order.add_edge(site_survey, water_testing)
root.order.add_edge(light_mapping, design_modules)
root.order.add_edge(water_testing, design_modules)
root.order.add_edge(design_modules, iot_setup)
root.order.add_edge(iot_setup, sensor_cal)
root.order.add_edge(sensor_cal, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_control)
root.order.add_edge(climate_control, regulatory_check)
root.order.add_edge(regulatory_check, community_meet)
root.order.add_edge(community_meet, energy_audit)
root.order.add_edge(energy_audit, staff_training)
root.order.add_edge(staff_training, installation)
root.order.add_edge(installation, loop)

print(root)