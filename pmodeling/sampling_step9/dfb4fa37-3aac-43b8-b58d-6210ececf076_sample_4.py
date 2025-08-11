import pm4py
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

# Define silent activities
skip = SilentTransition()

# Define the loop node for pilot cultivation
loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot_cultivation, skip])

# Define the XOR node for decision-making between pilot cultivation and process refinement
xor = OperatorPOWL(operator=Operator.XOR, children=[process_refinement, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])

# Define the order of execution
root.order.add_edge(loop, xor)

# Print the root
print(root)