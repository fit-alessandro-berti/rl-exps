import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and choices
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, light_mapping, water_testing])
module_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_modules, iot_setup, sensor_calibration])
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, regulatory_check])
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, staff_training])
installation_loop = OperatorPOWL(operator=Operator.LOOP, children=[installation, system_testing])
resource_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[resource_audit, impact_review])

# Define partial order
root = StrictPartialOrder(nodes=[
    site_survey_loop,
    module_design_loop,
    climate_control_loop,
    energy_audit_loop,
    installation_loop,
    resource_audit_loop,
    community_meet
])

# Add dependencies between nodes
root.order.add_edge(site_survey_loop, module_design_loop)
root.order.add_edge(module_design_loop, climate_control_loop)
root.order.add_edge(climate_control_loop, energy_audit_loop)
root.order.add_edge(energy_audit_loop, installation_loop)
root.order.add_edge(installation_loop, resource_audit_loop)
root.order.add_edge(resource_audit_loop, community_meet)

print(root)