from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
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

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, design_plan, permit_acquire, structural_retrofit, system_install, lighting_setup, sensor_deploy, seed_sourcing, nutrient_prep, staff_training, data_monitor, yield_analyze, compliance_check, community_meet, market_launch, logistics_plan])

# Define the dependencies between the nodes
root.order.add_edge(site_survey, design_plan)
root.order.add_edge(site_survey, permit_acquire)
root.order.add_edge(site_survey, structural_retrofit)
root.order.add_edge(site_survey, system_install)
root.order.add_edge(site_survey, lighting_setup)
root.order.add_edge(site_survey, sensor_deploy)
root.order.add_edge(site_survey, seed_sourcing)
root.order.add_edge(site_survey, nutrient_prep)
root.order.add_edge(site_survey, staff_training)
root.order.add_edge(site_survey, data_monitor)
root.order.add_edge(site_survey, yield_analyze)
root.order.add_edge(site_survey, compliance_check)
root.order.add_edge(site_survey, community_meet)
root.order.add_edge(site_survey, market_launch)
root.order.add_edge(site_survey, logistics_plan)

# The final POWL model is defined in 'root'