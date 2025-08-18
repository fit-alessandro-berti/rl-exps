from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
light_mapping = Transition(label='Light Mapping')
water_testing = Transition(label='Water Testing')
design_modules = Transition(label='Design Modules')
iot_setup = Transition(label='IoT Setup')
sensor_calibration = Transition(label='Sensor Calibration')
nutrient_mix = Transition(label='Nutrient Mix')
climate_control = Transition(label='Climate Control')
regulatory_check = Transition(label='Regulatory Check')
community_meet = Transition(label='Community Meet')
energy_audit = Transition(label='Energy Audit')
staff_training = Transition(label='Staff Training')
installation = Transition(label='Installation')
system_testing = Transition(label='System Testing')
yield_analysis = Transition(label='Yield Analysis')
resource_audit = Transition(label='Resource Audit')
impact_review = Transition(label='Impact Review')

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[
    energy_audit,
    resource_audit
])
partial_order = StrictPartialOrder(nodes=[
    site_survey,
    light_mapping,
    water_testing,
    design_modules,
    iot_setup,
    sensor_calibration,
    nutrient_mix,
    climate_control,
    regulatory_check,
    community_meet,
    xor,
    staff_training,
    installation,
    system_testing,
    yield_analysis,
    impact_review
])

# Define the dependencies
partial_order.order.add_edge(site_survey, light_mapping)
partial_order.order.add_edge(site_survey, water_testing)
partial_order.order.add_edge(site_survey, design_modules)
partial_order.order.add_edge(light_mapping, iot_setup)
partial_order.order.add_edge(light_mapping, sensor_calibration)
partial_order.order.add_edge(water_testing, nutrient_mix)
partial_order.order.add_edge(water_testing, climate_control)
partial_order.order.add_edge(design_modules, regulatory_check)
partial_order.order.add_edge(design_modules, community_meet)
partial_order.order.add_edge(iot_setup, xor)
partial_order.order.add_edge(sensor_calibration, xor)
partial_order.order.add_edge(nutrient_mix, xor)
partial_order.order.add_edge(climate_control, xor)
partial_order.order.add_edge(regulatory_check, staff_training)
partial_order.order.add_edge(community_meet, staff_training)
partial_order.order.add_edge(xor, installation)
partial_order.order.add_edge(installation, system_testing)
partial_order.order.add_edge(system_testing, yield_analysis)
partial_order.order.add_edge(yield_analysis, resource_audit)
partial_order.order.add_edge(resource_audit, impact_review)

# Assign the root
root = partial_order