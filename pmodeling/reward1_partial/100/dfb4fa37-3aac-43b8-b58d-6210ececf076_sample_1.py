import pm4py
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

# Define silent transitions
skip = SilentTransition()

# Define partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot_cultivation, data_integration, waste_recycling])
xor = OperatorPOWL(operator=Operator.XOR, children=[unit_designing, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[led_sourcing, hydroponic_setup])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[staff_hiring, pilot_cultivation])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[local_distribution, subscription_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[iot_deployment, sustainability_audit])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[market_testing, process_refinement])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[permit_securing, skip])

# Create the root partial order
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, loop)