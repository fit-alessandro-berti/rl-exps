import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_pasturize = Transition(label='Milk Pasturize')
milk_inoculate = Transition(label='Milk Inoculate')
curd_formation = Transition(label='Curd Formation')
curd_cut = Transition(label='Curd Cut')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
temperature_monitor = Transition(label='Temperature Monitor')
quality_test = Transition(label='Quality Test')
packaging = Transition(label='Packaging')
order_fulfill = Transition(label='Order Fulfill')
retail_deliver = Transition(label='Retail Deliver')
feedback_collect = Transition(label='Feedback Collect')

# Define the partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    milk_sourcing,
    culture_prep,
    milk_pasturize,
    milk_inoculate,
    curd_formation,
    curd_cut,
    whey_drain,
    mold_inoculate,
    press_cheese,
    aging_setup,
    humidity_control,
    temperature_monitor,
    quality_test,
    packaging,
    order_fulfill,
    retail_deliver,
    feedback_collect
])

xor = OperatorPOWL(operator=Operator.XOR, children=[
    feedback_collect,
    SilentTransition()
])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root model
print(root)