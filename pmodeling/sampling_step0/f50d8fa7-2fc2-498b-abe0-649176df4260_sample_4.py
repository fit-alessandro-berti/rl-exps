import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for design and retrofit
xor_design_retrofit = OperatorPOWL(operator=Operator.XOR, children=[design_plan, structural_retrofit])

# Define the exclusive choice for permit and retrofit
xor_permit_retrofit = OperatorPOWL(operator=Operator.XOR, children=[permit_acquire, structural_retrofit])

# Define the exclusive choice for seed sourcing and nutrient prep
xor_seed_nutrient = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, nutrient_prep])

# Define the exclusive choice for staff training and data monitoring
xor_staff_data = OperatorPOWL(operator=Operator.XOR, children=[staff_training, data_monitor])

# Define the exclusive choice for yield analysis and compliance check
xor_yield_compliance = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, compliance_check])

# Define the exclusive choice for community meeting and market launch
xor_community_market = OperatorPOWL(operator=Operator.XOR, children=[community_meet, market_launch])

# Define the exclusive choice for logistics plan and community meeting
xor_logistics_community = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, community_meet])

# Define the loop for sensor deployment
loop_sensor = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy])

# Define the exclusive choice for lighting setup and sensor deployment
xor_lighting_sensor = OperatorPOWL(operator=Operator.XOR, children=[lighting_setup, loop_sensor])

# Define the loop for seed sourcing and nutrient prep
loop_seed_nutrient = OperatorPOWL(operator=Operator.LOOP, children=[seed_sourcing, nutrient_prep])

# Define the loop for staff training and data monitoring
loop_staff_data = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, data_monitor])

# Define the loop for yield analysis and compliance check
loop_yield_compliance = OperatorPOWL(operator=Operator.LOOP, children=[yield_analyze, compliance_check])

# Define the exclusive choice for community meeting and market launch
xor_community_market = OperatorPOWL(operator=Operator.XOR, children=[community_meet, market_launch])

# Define the exclusive choice for logistics plan and community meeting
xor_logistics_community = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, community_meet])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, xor_design_retrofit, xor_permit_retrofit, xor_seed_nutrient, xor_staff_data, xor_yield_compliance, xor_community_market, xor_logistics_community])
root.order.add_edge(site_survey, xor_design_retrofit)
root.order.add_edge(site_survey, xor_permit_retrofit)
root.order.add_edge(xor_design_retrofit, xor_seed_nutrient)
root.order.add_edge(xor_permit_retrofit, xor_staff_data)
root.order.add_edge(xor_seed_nutrient, xor_yield_compliance)
root.order.add_edge(xor_staff_data, xor_community_market)
root.order.add_edge(xor_yield_compliance, xor_logistics_community)
root.order.add_edge(xor_logistics_community, market_launch)