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

# Define silent transitions
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, skip])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[curd_form, whey_drain])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[cheese_press, salt_rub])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[aging_set, flavor_check, texture_scan, quality_approve])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[custom_pack, cold_ship])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[retail_train, feedback_log])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[batch_adjust])

# Define root
root = StrictPartialOrder(nodes=[farm_select, xor, loop1, loop2, loop3, loop4, loop5, loop6])
root.order.add_edge(farm_select, xor)
root.order.add_edge(xor, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, farm_select)