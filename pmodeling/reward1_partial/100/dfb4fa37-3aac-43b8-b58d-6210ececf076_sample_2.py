from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_analysis = Transition(label='Site Analysis')
permit_securing = Transition(label='Permit Securing')
unit_designing = Transition(label='Unit Designing')
led_sourcing = Transition(label='LED Sourcing')
hydroponic_setup = Transition(label='Hydroponic Setup')
staff_hiring = Transition(label='Staff Hiring')
pilot_cultivation = Transition(label='Pilot Cultivation')
data_integration = Transition(label='Data Integration')
waste_recycling = Transition(label='Waste Recycling')
local_distribution = Transition(label='Local Distribution')
subscription_setup = Transition(label='Subscription Setup')
iot_deployment = Transition(label='IoT Deployment')
sustainability_audit = Transition(label='Sustainability Audit')
market_testing = Transition(label='Market Testing')
process_refinement = Transition(label='Process Refinement')

# Define the loop for process refinement
refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, permit_securing, unit_designing, led_sourcing, hydroponic_setup, staff_hiring, pilot_cultivation, data_integration, waste_recycling, local_distribution, subscription_setup, iot_deployment, sustainability_audit, market_testing, process_refinement])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[refinement_loop])
root.order.add_edge(refinement_loop, site_analysis)
root.order.add_edge(refinement_loop, permit_securing)
root.order.add_edge(refinement_loop, unit_designing)
root.order.add_edge(refinement_loop, led_sourcing)
root.order.add_edge(refinement_loop, hydroponic_setup)
root.order.add_edge(refinement_loop, staff_hiring)
root.order.add_edge(refinement_loop, pilot_cultivation)
root.order.add_edge(refinement_loop, data_integration)
root.order.add_edge(refinement_loop, waste_recycling)
root.order.add_edge(refinement_loop, local_distribution)
root.order.add_edge(refinement_loop, subscription_setup)
root.order.add_edge(refinement_loop, iot_deployment)
root.order.add_edge(refinement_loop, sustainability_audit)
root.order.add_edge(refinement_loop, market_testing)
root.order.add_edge(refinement_loop, process_refinement)

# Print the root
print(root)