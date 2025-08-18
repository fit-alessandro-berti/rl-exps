from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the process model
root = StrictPartialOrder(
    nodes=[farm_select, milk_test, milk_pasteurize, curd_form, whey_drain, cheese_press, salt_rub, aging_set,
           flavor_check, texture_scan, quality_approve, custom_pack, cold_ship, retail_train, feedback_log,
           batch_adjust],
    order={
        (farm_select, milk_test): OperatorPOWL(operator=Operator.XOR),
        (milk_test, milk_pasteurize): OperatorPOWL(operator=Operator.XOR),
        (milk_pasteurize, curd_form): OperatorPOWL(operator=Operator.XOR),
        (curd_form, whey_drain): OperatorPOWL(operator=Operator.XOR),
        (whey_drain, cheese_press): OperatorPOWL(operator=Operator.XOR),
        (cheese_press, salt_rub): OperatorPOWL(operator=Operator.XOR),
        (salt_rub, aging_set): OperatorPOWL(operator=Operator.XOR),
        (aging_set, flavor_check): OperatorPOWL(operator=Operator.XOR),
        (flavor_check, texture_scan): OperatorPOWL(operator=Operator.XOR),
        (texture_scan, quality_approve): OperatorPOWL(operator=Operator.XOR),
        (quality_approve, custom_pack): OperatorPOWL(operator=Operator.XOR),
        (custom_pack, cold_ship): OperatorPOWL(operator=Operator.XOR),
        (cold_ship, retail_train): OperatorPOWL(operator=Operator.XOR),
        (retail_train, feedback_log): OperatorPOWL(operator=Operator.XOR),
        (feedback_log, batch_adjust): OperatorPOWL(operator=Operator.XOR)
    }
)