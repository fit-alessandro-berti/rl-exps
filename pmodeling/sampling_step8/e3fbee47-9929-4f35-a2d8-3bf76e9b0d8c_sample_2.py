from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Farm Selection'),
        Transition(label='Milk Testing'),
        Transition(label='Batch Pasteurize'),
        Transition(label='Culture Add'),
        Transition(label='Curd Cut'),
        Transition(label='Whey Drain'),
        Transition(label='Mold Inoculate'),
        Transition(label='Press Form'),
        Transition(label='Salt Rub'),
        Transition(label='Aging Monitor'),
        Transition(label='Flavor Adjust'),
        Transition(label='Packaging Design'),
        Transition(label='Label Approval'),
        Transition(label='Order Processing'),
        Transition(label='Cold Storage'),
        Transition(label='Delivery Schedule'),
        Transition(label='Retail Setup'),
        Transition(label='Feedback Collect')
    ],
    order=[
        ('Farm Selection', 'Milk Testing'),
        ('Milk Testing', 'Batch Pasteurize'),
        ('Batch Pasteurize', 'Culture Add'),
        ('Culture Add', 'Curd Cut'),
        ('Curd Cut', 'Whey Drain'),
        ('Whey Drain', 'Mold Inoculate'),
        ('Mold Inoculate', 'Press Form'),
        ('Press Form', 'Salt Rub'),
        ('Salt Rub', 'Aging Monitor'),
        ('Aging Monitor', 'Flavor Adjust'),
        ('Flavor Adjust', 'Packaging Design'),
        ('Packaging Design', 'Label Approval'),
        ('Label Approval', 'Order Processing'),
        ('Order Processing', 'Cold Storage'),
        ('Cold Storage', 'Delivery Schedule'),
        ('Delivery Schedule', 'Retail Setup'),
        ('Retail Setup', 'Feedback Collect')
    ]
)