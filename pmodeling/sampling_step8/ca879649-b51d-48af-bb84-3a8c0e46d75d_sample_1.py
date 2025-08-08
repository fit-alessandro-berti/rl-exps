from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define each activity as a Transition object
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

# Define the partial order model
root = StrictPartialOrder()

# Add activities to the root
root.add_node(milk_sourcing)
root.add_node(quality_testing)
root.add_node(batch_selection)
root.add_node(curd_preparation)
root.add_node(pressing_cheese)
root.add_node(aging_control)
root.add_node(flavor_profiling)
root.add_node(packaging_prep)
root.add_node(climate_packing)
root.add_node(export_licensing)
root.add_node(customs_filing)
root.add_node(freight_booking)
root.add_node(cold_storage)
root.add_node(transport_tracking)
root.add_node(retail_delivery)
root.add_node(feedback_collection)

# Define the dependencies between activities
root.add_edge(milk_sourcing, quality_testing)
root.add_edge(quality_testing, batch_selection)
root.add_edge(batch_selection, curd_preparation)
root.add_edge(curd_preparation, pressing_cheese)
root.add_edge(pressing_cheese, aging_control)
root.add_edge(aging_control, flavor_profiling)
root.add_edge(flavor_profiling, packaging_prep)
root.add_edge(packaging_prep, climate_packing)
root.add_edge(climate_packing, export_licensing)
root.add_edge(export_licensing, customs_filing)
root.add_edge(customs_filing, freight_booking)
root.add_edge(freight_booking, cold_storage)
root.add_edge(cold_storage, transport_tracking)
root.add_edge(transport_tracking, retail_delivery)
root.add_edge(retail_delivery, feedback_collection)

# The final result is stored in the 'root' variable