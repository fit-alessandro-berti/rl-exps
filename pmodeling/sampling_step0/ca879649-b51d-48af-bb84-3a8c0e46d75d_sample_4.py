import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
batch_selection = Transition(label='Batch Selection')
curd_preparation = Transition(label='Curd Preparation')
pressing_cheese = Transition(label='Pressing Cheese')
aging_control = Transition(label='Aging Control')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_prep = Transition(label='Packaging Prep')
climate_packing = Transition(label='Climate Packing')
export_licensing = Transition(label='Export Licensing')
customs_filing = Transition(label='Customs Filing')
freight_booking = Transition(label='Freight Booking')
cold_storage = Transition(label='Cold Storage')
transport_tracking = Transition(label='Transport Tracking')
retail_delivery = Transition(label='Retail Delivery')
feedback_collection = Transition(label='Feedback Collection')

# Define silent transitions
skip = SilentTransition()

# Define the workflow model
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
xor_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[batch_selection, skip])
loop_curd_preparation = OperatorPOWL(operator=Operator.LOOP, children=[curd_preparation, aging_control])
xor_aging_control = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, skip])
loop_packaging_prep = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, climate_packing])
xor_climate_packing = OperatorPOWL(operator=Operator.XOR, children=[export_licensing, skip])
loop_freight_booking = OperatorPOWL(operator=Operator.LOOP, children=[customs_filing, freight_booking])
xor_customs_filing = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, skip])
loop_transport_tracking = OperatorPOWL(operator=Operator.LOOP, children=[transport_tracking, retail_delivery])
xor_transport_tracking = OperatorPOWL(operator=Operator.XOR, children=[feedback_collection, skip])

root = StrictPartialOrder(nodes=[
    loop_milk_sourcing, xor_quality_testing, loop_curd_preparation, xor_aging_control,
    loop_packaging_prep, xor_climate_packing, loop_freight_booking, xor_customs_filing,
    loop_transport_tracking, xor_transport_tracking
])

root.order.add_edge(loop_milk_sourcing, xor_quality_testing)
root.order.add_edge(xor_quality_testing, loop_curd_preparation)
root.order.add_edge(loop_curd_preparation, xor_aging_control)
root.order.add_edge(xor_aging_control, loop_packaging_prep)
root.order.add_edge(loop_packaging_prep, xor_climate_packing)
root.order.add_edge(xor_climate_packing, loop_freight_booking)
root.order.add_edge(loop_freight_booking, xor_customs_filing)
root.order.add_edge(xor_customs_filing, loop_transport_tracking)
root.order.add_edge(loop_transport_tracking, xor_transport_tracking)

print(root)