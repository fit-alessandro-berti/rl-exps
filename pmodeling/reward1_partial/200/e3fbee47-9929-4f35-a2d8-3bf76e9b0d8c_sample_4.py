import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_testing, batch_pasteurize, culture_add, curd_cut, whey_drain, mold_inoculate, press_form, salt_rub, aging_monitor])
xor = OperatorPOWL(operator=Operator.XOR, children=[flavor_adjust, packaging_design, label_approval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[order_processing, cold_storage, delivery_schedule])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[retail_setup, feedback_collect])
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)