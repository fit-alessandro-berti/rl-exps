from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

farm_select = Transition(label='Farm Select')
milk_test = Transition(label='Milk Test')
milk_past = Transition(label='Milk Pasteurize')
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

skip = SilentTransition()

farm_select_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_select, milk_test, milk_past, curd_form, whey_drain, cheese_press, salt_rub, aging_set, flavor_check, texture_scan, quality_approve, custom_pack, cold_ship, retail_train, feedback_log, batch_adjust])
farm_select_choice = OperatorPOWL(operator=Operator.XOR, children=[farm_select_loop, skip])

root = StrictPartialOrder(nodes=[farm_select_choice])
root.order.add_edge(farm_select_choice, farm_select_loop)