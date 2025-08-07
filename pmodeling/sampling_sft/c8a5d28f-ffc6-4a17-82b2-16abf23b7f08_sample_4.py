import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing    = Transition(label='Milk Sourcing')
quality_testing  = Transition(label='Quality Testing')
milk_pasteurize  = Transition(label='Milk Pasteurize')
culture_addition = Transition(label='Culture Addition')
curd_cutting     = Transition(label='Curd Cutting')
whey_drain       = Transition(label='Whey Drain')
cheese_molding   = Transition(label='Cheese Molding')
controlled_aging = Transition(label='Controlled Aging')
sensory_check    = Transition(label='Sensory Check')
health_certify   = Transition(label='Health Certify')
custom_labeling  = Transition(label='Custom Labeling')
cold_packaging   = Transition(label='Cold Packaging')
logistics_setup  = Transition(label='Logistics Setup')
export_docs      = Transition(label='Export Docs')
customs_clearance= Transition(label='Customs Clearance')
shipment_track   = Transition(label='Shipment Track')
client_feedback  = Transition(label='Client Feedback')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for controlled aging and sensory check
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[controlled_aging, sensory_check]
)

# Export process: Export Docs -> Customs Clearance -> Logistics Setup -> Shipment Track
export_seq = StrictPartialOrder(nodes=[export_docs, customs_clearance, logistics_setup, shipment_track])
export_seq.order.add_edge(export_docs, customs_clearance)
export_seq.order.add_edge(customs_clearance, logistics_setup)
export_seq.order.add_edge(logistics_setup, shipment_track)

# Final feedback loop: Client Feedback (optional)
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[client_feedback, skip]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, milk_pasteurize,
    culture_addition, curd_cutting, whey_drain,
    cheese_molding, aging_loop,
    health_certify, custom_labeling, cold_packaging,
    export_seq,
    feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_addition)
root.order.add_edge(culture_addition, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, cheese_molding)
root.order.add_edge(cheese_molding, aging_loop)
root.order.add_edge(aging_loop, health_certify)
root.order.add_edge(health_certify, custom_labeling)
root.order.add_edge(custom_labeling, cold_packaging)
root.order.add_edge(cold_packaging, export_seq)
root.order.add_edge(export_seq, feedback_loop)