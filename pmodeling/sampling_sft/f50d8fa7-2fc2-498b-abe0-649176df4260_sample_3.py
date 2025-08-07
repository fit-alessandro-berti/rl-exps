import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey       = Transition(label='Site Survey')
design_plan       = Transition(label='Design Plan')
permit_acquire    = Transition(label='Permit Acquire')
structural_retro  = Transition(label='Structural Retrofit')
system_install    = Transition(label='System Install')
lighting_setup    = Transition(label='Lighting Setup')
sensor_deploy     = Transition(label='Sensor Deploy')
seed_sourcing     = Transition(label='Seed Sourcing')
nutrient_prep     = Transition(label='Nutrient Prep')
staff_training    = Transition(label='Staff Training')
data_monitor      = Transition(label='Data Monitor')
yield_analyze     = Transition(label='Yield Analyze')
compliance_check  = Transition(label='Compliance Check')
community_meet    = Transition(label='Community Meet')
market_launch     = Transition(label='Market Launch')
logistics_plan    = Transition(label='Logistics Plan')

# Define the inner loop: data monitoring and yield analysis repeated until exit
loop_body = StrictPartialOrder(nodes=[data_monitor, yield_analyze])
loop_body.order.add_edge(data_monitor, yield_analyze)

# Loop operator: repeat the body sequence until exit
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, data_monitor])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_plan, permit_acquire,
    structural_retro, system_install, lighting_setup, sensor_deploy,
    seed_sourcing, nutrient_prep, staff_training,
    data_loop, compliance_check, community_meet,
    market_launch, logistics_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_plan)
root.order.add_edge(design_plan, permit_acquire)
root.order.add_edge(permit_acquire, structural_retro)
root.order.add_edge(structural_retro, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(lighting_setup, sensor_deploy)
root.order.add_edge(sensor_deploy, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(nutrient_prep, staff_training)
root.order.add_edge(staff_training, data_loop)
root.order.add_edge(data_loop, compliance_check)
root.order.add_edge(compliance_check, community_meet)
root.order.add_edge(community_meet, market_launch)
root.order.add_edge(market_launch, logistics_plan)