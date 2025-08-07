import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities using their exact names
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

# Define the partial order workflow
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    batch_selection,
    curd_preparation,
    pressing_cheese,
    aging_control,
    flavor_profiling,
    packaging_prep,
    climate_packing,
    export_licensing,
    customs_filing,
    freight_booking,
    cold_storage,
    transport_tracking,
    retail_delivery,
    feedback_collection
])

# Define the dependencies (order) between the activities
# Note: This is a simplified representation and assumes a linear workflow for demonstration purposes.
# In a real scenario, you would define the dependencies based on the actual workflow logic.
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(milk_sourcing, batch_selection)
root.order.add_edge(quality_testing, curd_preparation)
root.order.add_edge(quality_testing, pressing_cheese)
root.order.add_edge(batch_selection, aging_control)
root.order.add_edge(batch_selection, flavor_profiling)
root.order.add_edge(aging_control, packaging_prep)
root.order.add_edge(aging_control, climate_packing)
root.order.add_edge(climate_packing, export_licensing)
root.order.add_edge(climate_packing, customs_filing)
root.order.add_edge(climate_packing, freight_booking)
root.order.add_edge(climate_packing, cold_storage)
root.order.add_edge(cold_storage, transport_tracking)
root.order.add_edge(transport_tracking, retail_delivery)
root.order.add_edge(transport_tracking, feedback_collection)

# Print the root of the POWL model
print(root)