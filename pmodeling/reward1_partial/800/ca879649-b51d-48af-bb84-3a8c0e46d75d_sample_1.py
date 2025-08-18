from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, milk_sourcing])
loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_selection, curd_preparation])
xor_aging = OperatorPOWL(operator=Operator.XOR, children=[aging_control, packaging_prep])
xor_climate = OperatorPOWL(operator=Operator.XOR, children=[climate_packing, export_licensing])
xor_customs = OperatorPOWL(operator=Operator.XOR, children=[customs_filing, freight_booking])
xor_cold = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, transport_tracking])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_collection, retail_delivery])

# Create root model
root = StrictPartialOrder(nodes=[xor, loop, xor_aging, xor_climate, xor_customs, xor_cold, xor_feedback])
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor_aging)
root.order.add_edge(xor_aging, xor_climate)
root.order.add_edge(xor_climate, xor_customs)
root.order.add_edge(xor_customs, xor_cold)
root.order.add_edge(xor_cold, xor_feedback)