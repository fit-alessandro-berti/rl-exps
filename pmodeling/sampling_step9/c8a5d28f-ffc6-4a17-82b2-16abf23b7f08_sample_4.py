import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
culture_addition = Transition(label='Culture Addition')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
cheese_molding = Transition(label='Cheese Molding')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
health_certify = Transition(label='Health Certify')
custom_labeling = Transition(label='Custom Labeling')
cold_packaging = Transition(label='Cold Packaging')
logistics_setup = Transition(label='Logistics Setup')
export_docs = Transition(label='Export Docs')
customs_clearance = Transition(label='Customs Clearance')
shipment_track = Transition(label='Shipment Track')
client_feedback = Transition(label='Client Feedback')

# Define silent activities
skip = SilentTransition()

# Define the loop for controlled aging and sensory check
loop_aging_check = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging, sensory_check])
loop_aging_check.order.add_edge(controlled_aging, sensory_check)

# Define the exclusive choice for health certification and custom labeling
xor_health_certify_labeling = OperatorPOWL(operator=Operator.XOR, children=[health_certify, custom_labeling])
xor_health_certify_labeling.order.add_edge(health_certify, custom_labeling)

# Define the loop for logistics setup and export documentation
loop_logistics_docs = OperatorPOWL(operator=Operator.LOOP, children=[logistics_setup, export_docs])
loop_logistics_docs.order.add_edge(logistics_setup, export_docs)

# Define the loop for customs clearance and shipment tracking
loop_customs_clearance_track = OperatorPOWL(operator=Operator.LOOP, children=[customs_clearance, shipment_track])
loop_customs_clearance_track.order.add_edge(customs_clearance, shipment_track)

# Define the exclusive choice for client feedback and logistics setup
xor_client_feedback_logistics = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, logistics_setup])
xor_client_feedback_logistics.order.add_edge(client_feedback, logistics_setup)

# Define the final POWL model
root = StrictPartialOrder(nodes=[loop_aging_check, xor_health_certify_labeling, loop_logistics_docs, loop_customs_clearance_track, xor_client_feedback_logistics])
root.order.add_edge(loop_aging_check, xor_health_certify_labeling)
root.order.add_edge(xor_health_certify_labeling, loop_logistics_docs)
root.order.add_edge(loop_logistics_docs, loop_customs_clearance_track)
root.order.add_edge(loop_customs_clearance_track, xor_client_feedback_logistics)