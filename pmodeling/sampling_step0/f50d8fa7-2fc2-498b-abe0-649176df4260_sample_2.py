import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = {
    'Site Survey': Transition('Site Survey'),
    'Design Plan': Transition('Design Plan'),
    'Permit Acquire': Transition('Permit Acquire'),
    'Structural Retrofit': Transition('Structural Retrofit'),
    'System Install': Transition('System Install'),
    'Lighting Setup': Transition('Lighting Setup'),
    'Sensor Deploy': Transition('Sensor Deploy'),
    'Seed Sourcing': Transition('Seed Sourcing'),
    'Nutrient Prep': Transition('Nutrient Prep'),
    'Staff Training': Transition('Staff Training'),
    'Data Monitor': Transition('Data Monitor'),
    'Yield Analyze': Transition('Yield Analyze'),
    'Compliance Check': Transition('Compliance Check'),
    'Community Meet': Transition('Community Meet'),
    'Market Launch': Transition('Market Launch'),
    'Logistics Plan': Transition('Logistics Plan')
}

# Define exclusive choices
site_survey = OperatorPOWL(operator=Operator.XOR, children=[activities['Site Survey'], activities['Design Plan']])
permit_acquire = OperatorPOWL(operator=Operator.XOR, children=[activities['Permit Acquire'], activities['Structural Retrofit']])
system_install = OperatorPOWL(operator=Operator.XOR, children=[activities['System Install'], activities['Lighting Setup']])
sensor_deploy = OperatorPOWL(operator=Operator.XOR, children=[activities['Sensor Deploy'], activities['Seed Sourcing']])
seed_sourcing = OperatorPOWL(operator=Operator.XOR, children=[activities['Seed Sourcing'], activities['Nutrient Prep']])
data_monitor = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Monitor'], activities['Yield Analyze']])
compliance_check = OperatorPOWL(operator=Operator.XOR, children=[activities['Compliance Check'], activities['Community Meet']])
market_launch = OperatorPOWL(operator=Operator.XOR, children=[activities['Market Launch'], activities['Logistics Plan']])

# Define loops
staff_training = OperatorPOWL(operator=Operator.LOOP, children=[activities['Staff Training']])
seed_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[activities['Seed Sourcing'], activities['Nutrient Prep']])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, permit_acquire, system_install, sensor_deploy, seed_sourcing, data_monitor, compliance_check, market_launch, staff_training, seed_sourcing_loop])
root.order.add_edge(site_survey, permit_acquire)
root.order.add_edge(permit_acquire, system_install)
root.order.add_edge(system_install, sensor_deploy)
root.order.add_edge(sensor_deploy, seed_sourcing)
root.order.add_edge(seed_sourcing, data_monitor)
root.order.add_edge(data_monitor, compliance_check)
root.order.add_edge(compliance_check, market_launch)
root.order.add_edge(market_launch, staff_training)
root.order.add_edge(staff_training, seed_sourcing_loop)

# Print the root model
print(root)