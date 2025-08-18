import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
farm_selection = Transition(label='Farm Selection')
milk_testing = Transition(label='Milk Testing')
batch_pasteurize = Transition(label='Batch Pasteurize')
culture_add = Transition(label='Culture Add')
curd_cut = Transition(label='Curd Cut')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_form = Transition(label='Press Form')
salt_rub = Transition(label='Salt Rub')
aging_monitor = Transition(label='Aging Monitor')
flavor_adjust = Transition(label='Flavor Adjust')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_processing = Transition(label='Order Processing')
cold_storage = Transition(label='Cold Storage')
delivery_schedule = Transition(label='Delivery Schedule')
retail_setup = Transition(label='Retail Setup')
feedback_collect = Transition(label='Feedback Collect')

# Define silent transitions
skip = SilentTransition()

# Define POWL model
loop_farm = OperatorPOWL(operator=Operator.LOOP, children=[farm_selection])
loop_milk = OperatorPOWL(operator=Operator.LOOP, children=[milk_testing, batch_pasteurize, culture_add, curd_cut, whey_drain, mold_inoculate, press_form, salt_rub])
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_monitor, flavor_adjust])
loop_packaging = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, label_approval])
loop_order = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, cold_storage, delivery_schedule, retail_setup, feedback_collect])

# Create root POWL model
root = StrictPartialOrder(nodes=[loop_farm, loop_milk, loop_aging, loop_packaging, loop_order])
root.order.add_edge(loop_farm, loop_milk)
root.order.add_edge(loop_milk, loop_aging)
root.order.add_edge(loop_aging, loop_packaging)
root.order.add_edge(loop_packaging, loop_order)

print(root)