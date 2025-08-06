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

# Define the POWL model
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, feedback_collection])
xor_export = OperatorPOWL(operator=Operator.XOR, children=[export_licensing, customs_filing])
xor_filing = OperatorPOWL(operator=Operator.XOR, children=[freight_booking, cold_storage])
xor_shipping = OperatorPOWL(operator=Operator.XOR, children=[transport_tracking, retail_delivery])

root = StrictPartialOrder(nodes=[loop_aging, xor_export, xor_filing, xor_shipping])
root.order.add_edge(loop_aging, xor_export)
root.order.add_edge(loop_aging, xor_filing)
root.order.add_edge(loop_aging, xor_shipping)
root.order.add_edge(xor_export, xor_filing)
root.order.add_edge(xor_filing, xor_shipping)

# Print the POWL model
print(root)