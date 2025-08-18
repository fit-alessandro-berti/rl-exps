from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[])

# Add activities as transitions
site_analysis = Transition(label='Site Analysis')
permit_secuting = Transition(label='Permit Securing')
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

# Add activities to the root model
root.nodes.append(site_analysis)
root.nodes.append(permit_secuting)
root.nodes.append(unit_designing)
root.nodes.append(led_sourcing)
root.nodes.append(hydroponic_setup)
root.nodes.append(staff_hiring)
root.nodes.append(pilot_cultivation)
root.nodes.append(data_integration)
root.nodes.append(waste_recycling)
root.nodes.append(local_distribution)
root.nodes.append(subscription_setup)
root.nodes.append(iot_deployment)
root.nodes.append(sustainability_audit)
root.nodes.append(market_testing)
root.nodes.append(process_refinement)

# Define dependencies between activities
root.order.add_edge(site_analysis, permit_secuting)
root.order.add_edge(permit_secuting, unit_designing)
root.order.add_edge(unit_designing, led_sourcing)
root.order.add_edge(led_sourcing, hydroponic_setup)
root.order.add_edge(hydroponic_setup, staff_hiring)
root.order.add_edge(staff_hiring, pilot_cultivation)
root.order.add_edge(pilot_cultivation, data_integration)
root.order.add_edge(data_integration, waste_recycling)
root.order.add_edge(waste_recycling, local_distribution)
root.order.add_edge(local_distribution, subscription_setup)
root.order.add_edge(subscription_setup, iot_deployment)
root.order.add_edge(iot_deployment, sustainability_audit)
root.order.add_edge(sustainability_audit, market_testing)
root.order.add_edge(market_testing, process_refinement)

# The final POWL model is now defined in the 'root' variable