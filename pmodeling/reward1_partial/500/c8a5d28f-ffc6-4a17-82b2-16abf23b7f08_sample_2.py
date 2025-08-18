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

# Define the process steps
# Milk Sourcing
root = StrictPartialOrder(nodes=[milk_sourcing])

# Quality Testing
root.order.add_edge(milk_sourcing, quality_testing)

# Milk Pasteurize
root.order.add_edge(quality_testing, milk_pasteurize)

# Culture Addition
root.order.add_edge(milk_pasteurize, culture_addition)

# Curd Cutting
root.order.add_edge(culture_addition, curd_cutting)

# Whey Drain
root.order.add_edge(curd_cutting, whey_drain)

# Cheese Molding
root.order.add_edge(whey_drain, cheese_molding)

# Controlled Aging
root.order.add_edge(cheese_molding, controlled_aging)

# Sensory Check
root.order.add_edge(controlled_aging, sensory_check)

# Health Certify
root.order.add_edge(sensory_check, health_certify)

# Custom Labeling
root.order.add_edge(health_certify, custom_labeling)

# Cold Packaging
root.order.add_edge(custom_labeling, cold_packaging)

# Logistics Setup
root.order.add_edge(cold_packaging, logistics_setup)

# Export Docs
root.order.add_edge(logistics_setup, export_docs)

# Customs Clearance
root.order.add_edge(export_docs, customs_clearance)

# Shipment Track
root.order.add_edge(customs_clearance, shipment_track)

# Client Feedback
root.order.add_edge(shipment_track, client_feedback)