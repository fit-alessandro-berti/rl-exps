import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Batch_Selection = Transition(label='Batch Selection')
Curd_Preparation = Transition(label='Curd Preparation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Aging_Control = Transition(label='Aging Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Prep = Transition(label='Packaging Prep')
Climate_Packing = Transition(label='Climate Packing')
Export_Licensing = Transition(label='Export Licensing')
Customs_Filing = Transition(label='Customs Filing')
Freight_Booking = Transition(label='Freight Booking')
Cold_Storage = Transition(label='Cold Storage')
Transport_Tracking = Transition(label='Transport Tracking')
Retail_Delivery = Transition(label='Retail Delivery')
Feedback_Collection = Transition(label='Feedback Collection')

root = StrictPartialOrder(nodes=[
    Milk_Sourcing, Quality_Testing, Batch_Selection, Curd_Preparation, Pressing_Cheese,
    Aging_Control, Flavor_Profiling, Packaging_Prep, Climate_Packing, Export_Licensing,
    Customs_Filing, Freight_Booking, Cold_Storage, Transport_Tracking, Retail_Delivery,
    Feedback_Collection
])
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Batch_Selection)
root.order.add_edge(Batch_Selection, Curd_Preparation)
root.order.add_edge(Curd_Preparation, Pressing_Cheese)
root.order.add_edge(Pressing_Cheese, Aging_Control)
root.order.add_edge(Aging_Control, Flavor_Profiling)
root.order.add_edge(Flavor_Profiling, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Climate_Packing)
root.order.add_edge(Climate_Packing, Export_Licensing)
root.order.add_edge(Export_Licensing, Customs_Filing)
root.order.add_edge(Customs_Filing, Freight_Booking)
root.order.add_edge(Freight_Booking, Cold_Storage)
root.order.add_edge(Cold_Storage, Transport_Tracking)
root.order.add_edge(Transport_Tracking, Retail_Delivery)
root.order.add_edge(Retail_Delivery, Feedback_Collection)