import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
skip = SilentTransition()

# Define loop for controlled aging
controlled_aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging, sensory_check])

# Define XOR for health certification and custom labeling
health_certify_labeling_xor = OperatorPOWL(operator=Operator.XOR, children=[health_certify, custom_labeling])

# Define loop for logistics setup and shipment tracking
logistics_setup_track_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_setup, shipment_track])

# Define XOR for export documentation and customs clearance
export_docs_clearance_xor = OperatorPOWL(operator=Operator.XOR, children=[export_docs, customs_clearance])

# Define XOR for client feedback and skipping
client_feedback_skip_xor = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, milk_pasteurize, culture_addition, curd_cutting, whey_drain, cheese_molding, controlled_aging_loop, health_certify_labeling_xor, logistics_setup_track_loop, export_docs_clearance_xor, client_feedback_skip_xor])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_addition)
root.order.add_edge(culture_addition, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, cheese_molding)
root.order.add_edge(cheese_molding, controlled_aging_loop)
root.order.add_edge(controlled_aging_loop, health_certify_labeling_xor)
root.order.add_edge(health_certify_labeling_xor, logistics_setup_track_loop)
root.order.add_edge(logistics_setup_track_loop, export_docs_clearance_xor)
root.order.add_edge(export_docs_clearance_xor, client_feedback_skip_xor)
root.order.add_edge(client_feedback_skip_xor, client_feedback)

# Print the root POWL model
print(root)