from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Testing, Batch_Selection])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Curd_Preparation, Pressing_Cheese])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Control, Flavor_Profiling])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Packaging_Prep, Climate_Packing])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Export_Licensing, Customs_Filing])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Freight_Booking, Cold_Storage])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Transport_Tracking, Retail_Delivery])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Collection, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop1)