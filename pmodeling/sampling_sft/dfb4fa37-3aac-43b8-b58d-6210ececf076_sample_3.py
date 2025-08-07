import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_analysis     = Transition(label='Site Analysis')
permit_securing   = Transition(label='Permit Securing')
unit_designing    = Transition(label='Unit Designing')
led_sourcing      = Transition(label='LED Sourcing')
hydroponic_setup  = Transition(label='Hydroponic Setup')
staff_hiring      = Transition(label='Staff Hiring')
pilot_cultivation = Transition(label='Pilot Cultivation')
data_integration  = Transition(label='Data Integration')
waste_recycling   = Transition(label='Waste Recycling')
local_distribution= Transition(label='Local Distribution')
subscription_setup= Transition(label='Subscription Setup')
iot_deployment    = Transition(label='IoT Deployment')
sustainability_audit= Transition(label='Sustainability Audit')
market_testing    = Transition(label='Market Testing')
process_refinement= Transition(label='Process Refinement')

# Define the loop body: Data Integration -> Waste Recycling -> Local Distribution -> Subscription Setup
body = StrictPartialOrder(nodes=[data_integration, waste_recycling, local_distribution, subscription_setup])
body.order.add_edge(data_integration, waste_recycling)
body.order.add_edge(waste_recycling, local_distribution)
body.order.add_edge(local_distribution, subscription_setup)

# Define the loop: IoT Deployment, then either exit or repeat the body and then IoT Deployment again
loop = OperatorPOWL(operator=Operator.LOOP, children=[iot_deployment, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_analysis, permit_securing, unit_designing, led_sourcing, hydroponic_setup,
    staff_hiring, pilot_cultivation, loop,
    sustainability_audit, market_testing, process_refinement
])

# Add the control-flow edges
root.order.add_edge(site_analysis, permit_securing)
root.order.add_edge(permit_securing, unit_designing)
root.order.add_edge(unit_designing, led_sourcing)
root.order.add_edge(led_sourcing, hydroponic_setup)
root.order.add_edge(hydroponic_setup, staff_hiring)
root.order.add_edge(staff_hiring, pilot_cultivation)
root.order.add_edge(pilot_cultivation, loop)
root.order.add_edge(loop, sustainability_audit)
root.order.add_edge(sustainability_audit, market_testing)
root.order.add_edge(market_testing, process_refinement)