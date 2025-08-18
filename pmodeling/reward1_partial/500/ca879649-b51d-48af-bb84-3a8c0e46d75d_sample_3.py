import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the control-flow operators
xor_aging_control = OperatorPOWL(operator=Operator.XOR, children=[aging_control, climate_packing])
xor_customs_filing = OperatorPOWL(operator=Operator.XOR, children=[customs_filing, cold_storage])
xor_freight_booking = OperatorPOWL(operator=Operator.XOR, children=[freight_booking, transport_tracking])
xor_transport_tracking = OperatorPOWL(operator=Operator.XOR, children=[transport_tracking, retail_delivery])

loop_aging_control = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, climate_packing])
loop_customs_filing = OperatorPOWL(operator=Operator.LOOP, children=[customs_filing, cold_storage])
loop_freight_booking = OperatorPOWL(operator=Operator.LOOP, children=[freight_booking, transport_tracking])
loop_transport_tracking = OperatorPOWL(operator=Operator.LOOP, children=[transport_tracking, retail_delivery])

root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, batch_selection, curd_preparation, pressing_cheese, xor_aging_control, xor_customs_filing, xor_freight_booking, xor_transport_tracking, loop_aging_control, loop_customs_filing, loop_freight_booking, loop_transport_tracking, feedback_collection])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, batch_selection)
root.order.add_edge(batch_selection, curd_preparation)
root.order.add_edge(curd_preparation, pressing_cheese)
root.order.add_edge(pressing_cheese, xor_aging_control)
root.order.add_edge(xor_aging_control, xor_customs_filing)
root.order.add_edge(xor_customs_filing, xor_freight_booking)
root.order.add_edge(xor_freight_booking, xor_transport_tracking)
root.order.add_edge(xor_transport_tracking, loop_aging_control)
root.order.add_edge(loop_aging_control, loop_customs_filing)
root.order.add_edge(loop_customs_filing, loop_freight_booking)
root.order.add_edge(loop_freight_booking, loop_transport_tracking)
root.order.add_edge(loop_transport_tracking, feedback_collection)