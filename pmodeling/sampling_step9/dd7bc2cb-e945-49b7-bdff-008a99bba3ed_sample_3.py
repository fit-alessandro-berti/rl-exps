import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
farm_select = Transition(label='Farm Select')
milk_test = Transition(label='Milk Test')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define loops and choices
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_set, flavor_check, texture_scan, quality_approve])
aging_choice = OperatorPOWL(operator=Operator.XOR, children=[aging_loop, skip])

packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[custom_pack, cold_ship])
packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_loop, skip])

distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[retail_train, feedback_log, batch_adjust])
distribution_choice = OperatorPOWL(operator=Operator.XOR, children=[distribution_loop, skip])

root = StrictPartialOrder(nodes=[farm_select, milk_test, milk_pasturize, curd_form, whey_drain, cheese_press, salt_rub, aging_choice, packaging_choice, distribution_choice])
root.order.add_edge(farm_select, milk_test)
root.order.add_edge(milk_test, milk_pasturize)
root.order.add_edge(milk_pasturize, curd_form)
root.order.add_edge(curd_form, whey_drain)
root.order.add_edge(whey_drain, cheese_press)
root.order.add_edge(cheese_press, salt_rub)
root.order.add_edge(salt_rub, aging_choice)
root.order.add_edge(aging_choice, packaging_choice)
root.order.add_edge(packaging_choice, distribution_choice)
root.order.add_edge(distribution_choice, distribution_choice)