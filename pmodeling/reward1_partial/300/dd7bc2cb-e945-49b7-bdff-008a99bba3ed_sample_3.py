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

skip = SilentTransition()

# Define the process flow
farm_select_to_milk_test = OperatorPOWL(operator=Operator.XOR, children=[milk_test, skip])
milk_test_to_milk_pasteurize = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, skip])
milk_pasteurize_to_curd_form = OperatorPOWL(operator=Operator.XOR, children=[curd_form, skip])
curd_form_to_whey_drain = OperatorPOWL(operator=Operator.XOR, children=[whey_drain, skip])
whey_drain_to_cheese_press = OperatorPOWL(operator=Operator.XOR, children=[cheese_press, skip])
cheese_press_to_salt_rub = OperatorPOWL(operator=Operator.XOR, children=[salt_rub, skip])
salt_rub_to_aging_set = OperatorPOWL(operator=Operator.XOR, children=[aging_set, skip])
aging_set_to_flavor_check = OperatorPOWL(operator=Operator.XOR, children=[flavor_check, skip])
flavor_check_to_texture_scan = OperatorPOWL(operator=Operator.XOR, children=[texture_scan, skip])
texture_scan_to_quality_approve = OperatorPOWL(operator=Operator.XOR, children=[quality_approve, skip])
quality_approve_to_custom_pack = OperatorPOWL(operator=Operator.XOR, children=[custom_pack, skip])
custom_pack_to_cold_ship = OperatorPOWL(operator=Operator.XOR, children=[cold_ship, skip])
cold_ship_to_retail_train = OperatorPOWL(operator=Operator.XOR, children=[retail_train, skip])
retail_train_to_feedback_log = OperatorPOWL(operator=Operator.XOR, children=[feedback_log, skip])
feedback_log_to_batch_adjust = OperatorPOWL(operator=Operator.XOR, children=[batch_adjust, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[
    farm_select, 
    milk_test, 
    milk_pasteurize, 
    curd_form, 
    whey_drain, 
    cheese_press, 
    salt_rub, 
    aging_set, 
    flavor_check, 
    texture_scan, 
    quality_approve, 
    custom_pack, 
    cold_ship, 
    retail_train, 
    feedback_log, 
    batch_adjust
])

# Define the dependencies
root.order.add_edge(farm_select, milk_test)
root.order.add_edge(milk_test, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_form)
root.order.add_edge(curd_form, whey_drain)
root.order.add_edge(whey_drain, cheese_press)
root.order.add_edge(cheese_press, salt_rub)
root.order.add_edge(salt_rub, aging_set)
root.order.add_edge(aging_set, flavor_check)
root.order.add_edge(flavor_check, texture_scan)
root.order.add_edge(texture_scan, quality_approve)
root.order.add_edge(quality_approve, custom_pack)
root.order.add_edge(custom_pack, cold_ship)
root.order.add_edge(cold_ship, retail_train)
root.order.add_edge(retail_train, feedback_log)
root.order.add_edge(feedback_log, batch_adjust)

# Print the root node
print(root)