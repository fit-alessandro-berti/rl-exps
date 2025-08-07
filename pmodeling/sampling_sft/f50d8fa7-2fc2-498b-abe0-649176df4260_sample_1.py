import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
design_plan     = Transition(label='Design Plan')
permit_acquire  = Transition(label='Permit Acquire')
structural_ret  = Transition(label='Structural Retrofit')
system_install  = Transition(label='System Install')
lighting_setup  = Transition(label='Lighting Setup')
sensor_deploy   = Transition(label='Sensor Deploy')
seed_sourcing   = Transition(label='Seed Sourcing')
nutrient_prep   = Transition(label='Nutrient Prep')
staff_training  = Transition(label='Staff Training')
community_meet  = Transition(label='Community Meet')
data_monitor    = Transition(label='Data Monitor')
yield_analyze   = Transition(label='Yield Analyze')
compliance_check= Transition(label='Compliance Check')
market_launch   = Transition(label='Market Launch')
logistics_plan  = Transition(label='Logistics Plan')

# Silent transition for loop exit
skip = SilentTransition()

# Loop: Data Monitor then either exit or do Yield Analyze then Monitor again
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, yield_analyze])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_plan,
    permit_acquire,
    structural_ret,
    system_install,
    lighting_setup,
    sensor_deploy,
    seed_sourcing,
    nutrient_prep,
    staff_training,
    community_meet,
    data_loop,
    compliance_check,
    market_launch,
    logistics_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_plan)
root.order.add_edge(design_plan, permit_acquire)
root.order.add_edge(permit_acquire, structural_ret)
root.order.add_edge(structural_ret, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(lighting_setup, sensor_deploy)
root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(staff_training, community_meet)
root.order.add_edge(community_meet, data_loop)
root.order.add_edge(data_loop, compliance_check)
root.order.add_edge(compliance_check, market_launch)
root.order.add_edge(market_launch, logistics_plan)