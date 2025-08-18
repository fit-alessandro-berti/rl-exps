import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
site_survey = Transition(label='Site Survey')
design_plan = Transition(label='Design Plan')
permit_acquire = Transition(label='Permit Acquire')
structural_retrofit = Transition(label='Structural Retrofit')
system_install = Transition(label='System Install')
lighting_setup = Transition(label='Lighting Setup')
sensor_deploy = Transition(label='Sensor Deploy')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_prep = Transition(label='Nutrient Prep')
staff_training = Transition(label='Staff Training')
data_monitor = Transition(label='Data Monitor')
yield_analyze = Transition(label='Yield Analyze')
compliance_check = Transition(label='Compliance Check')
community_meet = Transition(label='Community Meet')
market_launch = Transition(label='Market Launch')
logistics_plan = Transition(label='Logistics Plan')

# Define the process steps as POWL operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[
    structural_retrofit, 
    system_install, 
    lighting_setup, 
    sensor_deploy, 
    seed_sourcing, 
    nutrient_prep, 
    staff_training, 
    data_monitor, 
    yield_analyze, 
    compliance_check, 
    community_meet, 
    market_launch, 
    logistics_plan
])

root = StrictPartialOrder(nodes=[exclusive_choice])
root.order.add_edge(exclusive_choice, exclusive_choice)

# Define the POWL model
root = StrictPartialOrder(nodes=[exclusive_choice])
root.order.add_edge(exclusive_choice, exclusive_choice)

# Print the final POWL model
print(root)