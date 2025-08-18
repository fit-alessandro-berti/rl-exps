from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define exclusive choice nodes
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, permit_securing])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[unit_designing, led_sourcing])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, staff_hiring])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[pilot_cultivation, data_integration])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, local_distribution])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[subscription_setup, iot_deployment])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, market_testing])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[process_refinement, exclusive_choice_1])

# Define the partial order
root = StrictPartialOrder(nodes=[exclusive_choice_1, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4, exclusive_choice_5, exclusive_choice_6, exclusive_choice_7, exclusive_choice_8])
root.order.add_edge(exclusive_choice_1, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)