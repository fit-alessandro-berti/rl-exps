import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing      = Transition(label='Milk Sourcing')
quality_testing    = Transition(label='Quality Testing')
milk_pasteurize    = Transition(label='Milk Pasteurize')
culture_addition   = Transition(label='Culture Addition')
curd_cutting       = Transition(label='Curd Cutting')
whey_drain         = Transition(label='Whey Drain')
cheese_molding     = Transition(label='Cheese Molding')
controlled_aging   = Transition(label='Controlled Aging')
sensory_check      = Transition(label='Sensory Check')
health_certify     = Transition(label='Health Certify')
custom_labeling    = Transition(label='Custom Labeling')
cold_packaging     = Transition(label='Cold Packaging')
logistics_setup    = Transition(label='Logistics Setup')
export_docs        = Transition(label='Export Docs')
customs_clearance  = Transition(label='Customs Clearance')
shipment_track     = Transition(label='Shipment Track')
client_feedback    = Transition(label='Client Feedback')

# Build the production sub‐workflow: milk → testing → pasteurize → culture → curd → drain → mold → age → check
production = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    milk_pasteurize,
    culture_addition,
    curd_cutting,
    whey_drain,
    cheese_molding,
    controlled_aging,
    sensory_check
])
production.order.add_edge(milk_sourcing, quality_testing)
production.order.add_edge(quality_testing, milk_pasteurize)
production.order.add_edge(milk_pasteurize, culture_addition)
production.order.add_edge(culture_addition, curd_cutting)
production.order.add_edge(curd_cutting, whey_drain)
production.order.add_edge(whey_drain, cheese_molding)
production.order.add_edge(cheese_molding, controlled_aging)
production.order.add_edge(controlled_aging, sensory_check)

# Build the export sub‐workflow: certify → label → pack → setup → docs → clearance → track → feedback
export = StrictPartialOrder(nodes=[
    health_certify,
    custom_labeling,
    cold_packaging,
    logistics_setup,
    export_docs,
    customs_clearance,
    shipment_track,
    client_feedback
])
export.order.add_edge(health_certify, custom_labeling)
export.order.add_edge(custom_labeling, cold_packaging)
export.order.add_edge(cold_packaging, logistics_setup)
export.order.add_edge(logistics_setup, export_docs)
export.order.add_edge(export_docs, customs_clearance)
export.order.add_edge(customs_clearance, shipment_track)
export.order.add_edge(shipment_track, client_feedback)

# Final partial order: production then export
root = StrictPartialOrder(nodes=[production, export])
root.order.add_edge(production, export)