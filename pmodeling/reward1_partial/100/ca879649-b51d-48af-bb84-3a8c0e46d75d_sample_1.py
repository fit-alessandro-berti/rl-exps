import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define each activity as a transition
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

# Define loops and choices using OperatorPOWL
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, flavor_profiling])
climate_packing_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_packing])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, climate_packing])
export_licensing_choice = OperatorPOWL(operator=Operator.XOR, children=[export_licensing, SilentTransition()])
customs_filing_choice = OperatorPOWL(operator=Operator.XOR, children=[customs_filing, SilentTransition()])
freight_booking_choice = OperatorPOWL(operator=Operator.XOR, children=[freight_booking, SilentTransition()])
transport_tracking_loop = OperatorPOWL(operator=Operator.LOOP, children=[transport_tracking])

# Create the root node as a StrictPartialOrder
root = StrictPartialOrder(nodes=[
    milk_sourcing, 
    quality_testing, 
    batch_selection, 
    curd_preparation, 
    pressing_cheese, 
    aging_loop, 
    packaging_loop, 
    export_licensing_choice, 
    customs_filing_choice, 
    freight_booking_choice, 
    cold_storage, 
    transport_tracking_loop, 
    retail_delivery, 
    feedback_collection
])

# Add dependencies between nodes
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(milk_sourcing, batch_selection)
root.order.add_edge(quality_testing, curd_preparation)
root.order.add_edge(batch_selection, pressing_cheese)
root.order.add_edge(pressing_cheese, aging_loop)
root.order.add_edge(aging_loop, packaging_loop)
root.order.add_edge(packaging_loop, export_licensing_choice)
root.order.add_edge(packaging_loop, customs_filing_choice)
root.order.add_edge(packaging_loop, freight_booking_choice)
root.order.add_edge(export_licensing_choice, cold_storage)
root.order.add_edge(customs_filing_choice, cold_storage)
root.order.add_edge(freight_booking_choice, cold_storage)
root.order.add_edge(cold_storage, transport_tracking_loop)
root.order.add_edge(transport_tracking_loop, retail_delivery)
root.order.add_edge(retail_delivery, feedback_collection)

# Print the root node
print(root)