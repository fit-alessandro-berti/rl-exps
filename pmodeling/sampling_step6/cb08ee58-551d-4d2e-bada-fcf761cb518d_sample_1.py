import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
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
    energy_audit,
    staff_training,
    installation,
    system_testing,
    yield_analysis,
    resource_audit,
    impact_review
])

# Define the dependencies (if any, not specified in the problem statement)
# Here we assume no dependencies for simplicity, but they could be added as needed

print(root)