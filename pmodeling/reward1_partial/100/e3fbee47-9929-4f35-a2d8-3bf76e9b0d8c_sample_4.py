import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define exclusive choices for each stage
stage1 = OperatorPOWL(operator=Operator.XOR, children=[farm_selection, milk_testing])
stage2 = OperatorPOWL(operator=Operator.XOR, children=[batch_pasteurize, culture_add])
stage3 = OperatorPOWL(operator=Operator.XOR, children=[curd_cut, whey_drain])
stage4 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, press_form])
stage5 = OperatorPOWL(operator=Operator.XOR, children=[salt_rub, aging_monitor])
stage6 = OperatorPOWL(operator=Operator.XOR, children=[flavor_adjust, packaging_design])
stage7 = OperatorPOWL(operator=Operator.XOR, children=[label_approval, order_processing])
stage8 = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, delivery_schedule])
stage9 = OperatorPOWL(operator=Operator.XOR, children=[retail_setup, feedback_collect])

# Define the root POWL model with sequential execution
root = StrictPartialOrder(nodes=[stage1, stage2, stage3, stage4, stage5, stage6, stage7, stage8, stage9])
root.order.add_edge(stage1, stage2)
root.order.add_edge(stage2, stage3)
root.order.add_edge(stage3, stage4)
root.order.add_edge(stage4, stage5)
root.order.add_edge(stage5, stage6)
root.order.add_edge(stage6, stage7)
root.order.add_edge(stage7, stage8)
root.order.add_edge(stage8, stage9)

print(root)