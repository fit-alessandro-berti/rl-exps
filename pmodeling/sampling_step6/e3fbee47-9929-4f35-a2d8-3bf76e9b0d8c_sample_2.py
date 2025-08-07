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

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    farm_selection,
    milk_testing,
    batch_pasteurize,
    culture_add,
    curd_cut,
    whey_drain,
    mold_inoculate,
    press_form,
    salt_rub,
    aging_monitor,
    flavor_adjust,
    packaging_design,
    label_approval,
    order_processing,
    cold_storage,
    delivery_schedule,
    retail_setup,
    feedback_collect
])

# Optionally, add dependencies between activities if needed
# For example, to add a dependency from 'Milk Testing' to 'Batch Pasteurize':
# root.order.add_edge(milk_testing, batch_pasteurize)

# Now, 'root' contains the POWL model for the specified process