import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define loops and choices
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Control, Flavor_Profiling])
loop_transport = OperatorPOWL(operator=Operator.LOOP, children=[Transport_Tracking, Retail_Delivery])
loop_customs = OperatorPOWL(operator=Operator.LOOP, children=[Customs_Filing, Feedback_Collection])

xor_quality = OperatorPOWL(operator=Operator.XOR, children=[Quality_Testing, skip])
xor_packing = OperatorPOWL(operator=Operator.XOR, children=[Packaging_Prep, Climate_Packing])
xor_freight = OperatorPOWL(operator=Operator.XOR, children=[Freight_Booking, Cold_Storage])

root = StrictPartialOrder(nodes=[loop_aging, loop_transport, loop_customs, xor_quality, xor_packing, xor_freight])
root.order.add_edge(loop_aging, xor_quality)
root.order.add_edge(loop_aging, xor_packing)
root.order.add_edge(loop_aging, xor_freight)
root.order.add_edge(loop_transport, xor_freight)
root.order.add_edge(loop_customs, xor_freight)

print(root)