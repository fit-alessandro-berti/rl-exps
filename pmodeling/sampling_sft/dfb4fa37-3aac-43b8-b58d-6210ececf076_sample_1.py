import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_analysis    = Transition(label='Site Analysis')
permit_securing  = Transition(label='Permit Securing')
unit_designing   = Transition(label='Unit Designing')
led_sourcing     = Transition(label='LED Sourcing')
hydroponic_setup = Transition(label='Hydroponic Setup')
staff_hiring     = Transition(label='Staff Hiring')
pilot_cultivation= Transition(label='Pilot Cultivation')
data_integration = Transition(label='Data Integration')
waste_recycling  = Transition(label='Waste Recycling')
local_distribution = Transition(label='Local Distribution')
subscription_setup = Transition(label='Subscription Setup')
iot_deployment   = Transition(label='IoT Deployment')
sustainability_audit = Transition(label='Sustainability Audit')
market_testing   = Transition(label='Market Testing')
process_refinement = Transition(label='Process Refinement')

# Define the loop for continuous improvement: Market Testing then optionally Process Refinement and Market Testing again
loop_improvement = OperatorPOWL(
    operator=Operator.LOOP,
    children=[market_testing, process_refinement]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_analysis, permit_securing, unit_designing, led_sourcing, hydroponic_setup,
    staff_hiring, pilot_cultivation, data_integration, waste_recycling,
    local_distribution, subscription_setup, iot_deployment, sustainability_audit,
    loop_improvement
])

# Add the sequential dependencies
root.order.add_edge(site_analysis,    permit_securing)
root.order.add_edge(permit_securing,  unit_designing)
root.order.add_edge(unit_designing,   led_sourcing)
root.order.add_edge(unit_designing,   hydroponic_setup)
root.order.add_edge(led_sourcing,     staff_hiring)
root.order.add_edge(hydroponic_setup, staff_hiring)
root.order.add_edge(staff_hiring,     pilot_cultivation)
root.order.add_edge(pilot_cultivation, data_integration)
root.order.add_edge(data_integration, waste_recycling)
root.order.add_edge(waste_recycling,  local_distribution)
root.order.add_edge(local_distribution, subscription_setup)
root.order.add_edge(subscription_setup, iot_deployment)
root.order.add_edge(iot_deployment,   sustainability_audit)
root.order.add_edge(sustainability_audit, loop_improvement)