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

# Define the loop for the training process
training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, data_monitor, compliance_check, community_meet])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[site_survey, design_plan, permit_acquire, structural_retrofit, system_install, lighting_setup, sensor_deploy, seed_sourcing, nutrient_prep, training_loop, yield_analyze, market_launch, logistics_plan])
root.order.add_edge(site_survey, design_plan)
root.order.add_edge(site_survey, permit_acquire)
root.order.add_edge(design_plan, structural_retrofit)
root.order.add_edge(structural_retrofit, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(lighting_setup, sensor_deploy)
root.order.add_edge(sensor_deploy, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(nutrient_prep, training_loop)
root.order.add_edge(training_loop, yield_analyze)
root.order.add_edge(yield_analyze, market_launch)
root.order.add_edge(market_launch, logistics_plan)

print(root)