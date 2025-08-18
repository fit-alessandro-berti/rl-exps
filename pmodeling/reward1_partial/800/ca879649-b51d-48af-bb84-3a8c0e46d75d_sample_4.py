import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (milk_sourcing, quality_testing),
        (quality_testing, batch_selection),
        (batch_selection, curd_preparation),
        (curd_preparation, pressing_cheese),
        (pressing_cheese, aging_control),
        (aging_control, flavor_profiling),
        (flavor_profiling, packaging_prep),
        (packaging_prep, climate_packing),
        (climate_packing, export_licensing),
        (export_licensing, customs_filing),
        (customs_filing, freight_booking),
        (freight_booking, cold_storage),
        (cold_storage, transport_tracking),
        (transport_tracking, retail_delivery),
        (retail_delivery, feedback_collection)
    ]
)

# Print the root POWL model
print(root)