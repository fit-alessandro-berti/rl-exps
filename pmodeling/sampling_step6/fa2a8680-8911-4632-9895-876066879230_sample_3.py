import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
client_meet = Transition(label='Client Meet')
requirement_gather = Transition(label='Requirement Gather')
module_design = Transition(label='Module Design')
supplier_vetting = Transition(label='Supplier Vetting')
component_order = Transition(label='Component Order')
prototype_build = Transition(label='Prototype Build')
field_testing = Transition(label='Field Testing')
test_analysis = Transition(label='Test Analysis')
software_setup = Transition(label='Software Setup')
data_integration = Transition(label='Data Integration')
pilot_train = Transition(label='Pilot Train')
compliance_check = Transition(label='Compliance Check')
fleet_deploy = Transition(label='Fleet Deploy')
remote_monitor = Transition(label='Remote Monitor')
maintenance_plan = Transition(label='Maintenance Plan')
performance_tune = Transition(label='Performance Tune')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    client_meet,
    requirement_gather,
    module_design,
    supplier_vetting,
    component_order,
    prototype_build,
    field_testing,
    test_analysis,
    software_setup,
    data_integration,
    pilot_train,
    compliance_check,
    fleet_deploy,
    remote_monitor,
    maintenance_plan,
    performance_tune
])

# No additional dependencies or loops are needed for this sequence of activities.
# If there were dependencies, they would be added here using `root.order.add_edge`.

# Note: The above code assumes that the dependencies between the activities are defined implicitly by the sequence of activities.
# If there are explicit dependencies, they should be added using `root.order.add_edge` as shown in the example code.