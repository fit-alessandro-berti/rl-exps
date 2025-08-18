import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
farm_select = Transition(label='Farm Select')
milk_test = Transition(label='Milk Test')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_form = Transition(label='Curd Form')
whey_drain = Transition(label='Whey Drain')
cheese_press = Transition(label='Cheese Press')
salt_rub = Transition(label='Salt Rub')
aging_set = Transition(label='Aging Set')
flavor_check = Transition(label='Flavor Check')
texture_scan = Transition(label='Texture Scan')
quality_approve = Transition(label='Quality Approve')
custom_pack = Transition(label='Custom Pack')
cold_ship = Transition(label='Cold Ship')
retail_train = Transition(label='Retail Train')
feedback_log = Transition(label='Feedback Log')
batch_adjust = Transition(label='Batch Adjust')

# Define the control flow
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_set, flavor_check, texture_scan, quality_approve])
xor_distribution = OperatorPOWL(operator=Operator.XOR, children=[custom_pack, cold_ship])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[retail_train, feedback_log])
xor_batch_adjust = OperatorPOWL(operator=Operator.XOR, children=[batch_adjust, farm_select])

# Define the root
root = StrictPartialOrder(nodes=[farm_select, milk_test, milk_pasteurize, curd_form, whey_drain, cheese_press, salt_rub, loop_aging, xor_distribution, xor_feedback, xor_batch_adjust])
root.order.add_edge(farm_select, milk_test)
root.order.add_edge(milk_test, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_form)
root.order.add_edge(curd_form, whey_drain)
root.order.add_edge(whey_drain, cheese_press)
root.order.add_edge(cheese_press, salt_rub)
root.order.add_edge(salt_rub, loop_aging)
root.order.add_edge(loop_aging, xor_distribution)
root.order.add_edge(xor_distribution, xor_feedback)
root.order.add_edge(xor_feedback, xor_batch_adjust)
root.order.add_edge(xor_batch_adjust, farm_select)

# Print the root
print(root)