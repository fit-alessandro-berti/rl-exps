import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing     = Transition(label='Milk Sourcing')
quality_testing   = Transition(label='Quality Testing')
milk_pasturize    = Transition(label='Milk Pasteurize')
culture_addition  = Transition(label='Culture Addition')
curd_cutting      = Transition(label='Curd Cutting')
whey_drain        = Transition(label='Whey Drain')
cheese_molding    = Transition(label='Cheese Molding')
controlled_aging  = Transition(label='Controlled Aging')
sensory_check     = Transition(label='Sensory Check')
health_certify    = Transition(label='Health Certify')
custom_labeling   = Transition(label='Custom Labeling')
cold_packaging    = Transition(label='Cold Packaging')
logistics_setup   = Transition(label='Logistics Setup')
export_docs       = Transition(label='Export Docs')
customs_clearance = Transition(label='Customs Clearance')
shipment_track    = Transition(label='Shipment Track')
client_feedback   = Transition(label='Client Feedback')

# Silent transition for loop repetition exit
skip = SilentTransition()

# Loop: perform aging, then optionally check sensory and certify health, then repeat
loop_body = StrictPartialOrder(nodes=[controlled_aging, sensory_check, health_certify])
loop_body.order.add_edge(controlled_aging, sensory_check)
loop_body.order.add_edge(sensory_check, health_certify)

loop = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, milk_pasturize, culture_addition, curd_cutting,
    whey_drain, cheese_molding, loop,
    custom_labeling, cold_packaging, logistics_setup, export_docs, customs_clearance, shipment_track,
    client_feedback
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasturize)
root.order.add_edge(milk_pasturize, culture_addition)
root.order.add_edge(culture_addition, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, cheese_molding)
root.order.add_edge(cheese_molding, loop)
root.order.add_edge(loop, custom_labeling)
root.order.add_edge(custom_labeling, cold_packaging)
root.order.add_edge(cold_packaging, logistics_setup)
root.order.add_edge(logistics_setup, export_docs)
root.order.add_edge(export_docs, customs_clearance)
root.order.add_edge(customs_clearance, shipment_track)
root.order.add_edge(shipment_track, client_feedback)