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
data_monitor    = Transition(label='Data Monitor')
yield_analyze   = Transition(label='Yield Analyze')
compliance_check= Transition(label='Compliance Check')
community_meet  = Transition(label='Community Meet')
market_launch   = Transition(label='Market Launch')
logistics_plan  = Transition(label='Logistics Plan')

# Build the monitoring/analysis partial order: Data Monitor -> Yield Analyze
monitor_po = StrictPartialOrder(nodes=[data_monitor, yield_analyze])
monitor_po.order.add_edge(data_monitor, yield_analyze)

# Build the compliance/monitoring loop: Compliance Check -> (Community Meet -> monitor_po -> Compliance Check)
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, monitor_po])

# Build the core process partial order: Site Survey -> Design Plan -> Permit Acquire -> Structural Retrofit -> System Install -> Lighting Setup -> Sensor Deploy
core_po = StrictPartialOrder(nodes=[
    site_survey, design_plan, permit_acquire,
    structural_ret, system_install, lighting_setup, sensor_deploy
])
core_po.order.add_edge(site_survey, design_plan)
core_po.order.add_edge(design_plan, permit_acquire)
core_po.order.add_edge(permit_acquire, structural_ret)
core_po.order.add_edge(structural_ret, system_install)
core_po.order.add_edge(system_install, lighting_setup)
core_po.order.add_edge(lighting_setup, sensor_deploy)

# Assemble the overall process
root = StrictPartialOrder(nodes=[
    site_survey, design_plan, permit_acquire, structural_ret,
    system_install, lighting_setup, sensor_deploy, seed_sourcing,
    nutrient_prep, staff_training, compliance_loop, community_meet,
    market_launch, logistics_plan
])
root.order.add_edge(site_survey, design_plan)
root.order.add_edge(design_plan, permit_acquire)
root.order.add_edge(permit_acquire, structural_ret)
root.order.add_edge(structural_ret, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(lighting_setup, sensor_deploy)
root.order.add_edge(seed_sourcing, compliance_loop)
root.order.add_edge(nutrient_prep, compliance_loop)
root.order.add_edge(staff_training, compliance_loop)
root.order.add_edge(compliance_loop, community_meet)
root.order.add_edge(community_meet, market_launch)
root.order.add_edge(market_launch, logistics_plan)