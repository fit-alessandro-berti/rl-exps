import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
site_survey      = Transition(label='Site Survey')
light_mapping    = Transition(label='Light Mapping')
water_testing    = Transition(label='Water Testing')
design_modules   = Transition(label='Design Modules')
iot_setup        = Transition(label='IoT Setup')
sensor_calibration = Transition(label='Sensor Calibration')
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

# Loop for continuous performance review & audit
loop_body = StrictPartialOrder(nodes=[yield_analysis, resource_audit, impact_review])
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey, light_mapping, water_testing, design_modules,
    iot_setup, sensor_calibration, nutrient_mix, climate_control,
    regulatory_check, community_meet, energy_audit, staff_training,
    installation, system_testing, loop
])

# Sequence of site survey, then testing, then design
root.order.add_edge(site_survey, light_mapping)
root.order.add_edge(site_survey, water_testing)
root.order.add_edge(light_mapping, design_modules)
root.order.add_edge(water_testing, design_modules)

# IoT and sensor setup after design
root.order.add_edge(design_modules, iot_setup)
root.order.add_edge(design_modules, sensor_calibration)

# Mix nutrients, then control climate
root.order.add_edge(iot_setup, nutrient_mix)
root.order.add_edge(sensor_calibration, climate_control)

# Regulatory, community, energy, training after setup
root.order.add_edge(nutrient_mix, regulatory_check)
root.order.add_edge(climate_control, regulatory_check)
root.order.add_edge(nutrient_mix, community_meet)
root.order.add_edge(climate_control, community_meet)
root.order.add_edge(nutrient_mix, energy_audit)
root.order.add_edge(climate_control, energy_audit)
root.order.add_edge(nutrient_mix, staff_training)
root.order.add_edge(climate_control, staff_training)

# Installation and testing after regulatory and training
root.order.add_edge(regulatory_check, installation)
root.order.add_edge(community_meet, installation)
root.order.add_edge(energy_audit, installation)
root.order.add_edge(staff_training, installation)
root.order.add_edge(installation, system_testing)

# Loop at the end
root.order.add_edge(system_testing, loop)