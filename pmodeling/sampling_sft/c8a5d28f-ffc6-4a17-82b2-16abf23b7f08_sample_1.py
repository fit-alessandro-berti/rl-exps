import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Silent transition for loop exit
skip = SilentTransition()

# Loop: sensory check then optional feedback
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_check, client_feedback])

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    milk_pasteurize,
    culture_addition,
    curd_cutting,
    whey_drain,
    cheese_molding,
    controlled_aging,
    health_certify,
    custom_labeling,
    cold_packaging,
    logistics_setup,
    export_docs,
    customs_clearance,
    shipment_track,
    sensory_loop
])

# Sequence: milk sourcing -> quality testing -> milk pasteurize -> culture addition -> curd cutting -> whey drain -> cheese molding -> controlled aging
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_addition)
root.order.add_edge(culture_addition, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, cheese_molding)
root.order.add_edge(cheese_molding, controlled_aging)

# After aging, do health certify and custom labeling in parallel
root.order.add_edge(controlled_aging, health_certify)
root.order.add_edge(controlled_aging, custom_labeling)

# Both certifications must finish before packaging
root.order.add_edge(health_certify, cold_packaging)
root.order.add_edge(custom_labeling, cold_packaging)

# Packaging must finish before logistics setup
root.order.add_edge(cold_packaging, logistics_setup)

# Logistics setup must finish before export docs
root.order.add_edge(logistics_setup, export_docs)

# Export docs must finish before customs clearance
root.order.add_edge(export_docs, customs_clearance)

# Customs clearance must finish before shipment tracking
root.order.add_edge(customs_clearance, shipment_track)

# Shipment tracking must finish before sensory check
root.order.add_edge(shipment_track, sensory_loop)

# Sensory check loop must finish before feedback
root.order.add_edge(sensory_loop, client_feedback)