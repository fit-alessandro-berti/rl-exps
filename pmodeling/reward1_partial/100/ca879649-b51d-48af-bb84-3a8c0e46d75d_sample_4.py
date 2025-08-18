import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define sub-processes (loops or choices)
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, flavor_profiling, packaging_prep, climate_packing])
export_process = OperatorPOWL(operator=Operator.XOR, children=[export_licensing, customs_filing, freight_booking])
storage_process = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, transport_tracking])
delivery_process = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, feedback_collection])

# Define the root process
root = StrictPartialOrder(nodes=[aging_loop, export_process, storage_process, delivery_process])
root.order.add_edge(aging_loop, export_process)
root.order.add_edge(aging_loop, storage_process)
root.order.add_edge(export_process, storage_process)
root.order.add_edge(export_process, delivery_process)
root.order.add_edge(storage_process, delivery_process)

# Print the root process (for demonstration purposes)
print(root)