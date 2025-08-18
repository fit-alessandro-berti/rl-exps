import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[farm_select, milk_test, milk_pasteurize, curd_form, whey_drain, cheese_press, salt_rub, aging_set, flavor_check, texture_scan, quality_approve, custom_pack])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[cold_ship, retail_train])
xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_log, batch_adjust])

root = StrictPartialOrder(nodes=[loop1, loop2, xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)

print(root)