import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    site_survey, design_plan, permit_acquire, structural_retrofit, system_install, lighting_setup, sensor_deploy, seed_sourcing, nutrient_prep, staff_training, data_monitor, yield_analyze, compliance_check, community_meet, market_launch, logistics_plan
])

# Define the dependencies between activities
root.order.add_edge(site_survey, design_plan)
root.order.add_edge(design_plan, permit_acquire)
root.order.add_edge(permit_acquire, structural_retrofit)
root.order.add_edge(structural_retrofit, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(lighting_setup, sensor_deploy)
root.order.add_edge(sensor_deploy, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(nutrient_prep, staff_training)
root.order.add_edge(staff_training, data_monitor)
root.order.add_edge(data_monitor, yield_analyze)
root.order.add_edge(yield_analyze, compliance_check)
root.order.add_edge(compliance_check, community_meet)
root.order.add_edge(community_meet, market_launch)
root.order.add_edge(market_launch, logistics_plan)

# Print the POWL model
print(root)