from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Milk Sourcing'),
        Transition(label='Quality Testing'),
        Transition(label='Batch Curdling'),
        Transition(label='Whey Removal'),
        Transition(label='Mold Inoculation'),
        Transition(label='Humidity Control'),
        Transition(label='Temperature Aging'),
        Transition(label='Rind Brushing'),
        Transition(label='Flavor Sampling'),
        Transition(label='Label Printing'),
        Transition(label='Packaging Prep'),
        Transition(label='Cold Storage'),
        Transition(label='Order Consolidation'),
        Transition(label='Logistics Scheduling'),
        Transition(label='Customer Feedback'),
        Transition(label='Certification Audit'),
        Transition(label='Recipe Adjustment')
    ],
    order=[
        ('Milk Sourcing', 'Quality Testing'),
        ('Quality Testing', 'Batch Curdling'),
        ('Batch Curdling', 'Whey Removal'),
        ('Whey Removal', 'Mold Inoculation'),
        ('Mold Inoculation', 'Humidity Control'),
        ('Humidity Control', 'Temperature Aging'),
        ('Temperature Aging', 'Rind Brushing'),
        ('Rind Brushing', 'Flavor Sampling'),
        ('Flavor Sampling', 'Label Printing'),
        ('Label Printing', 'Packaging Prep'),
        ('Packaging Prep', 'Cold Storage'),
        ('Cold Storage', 'Order Consolidation'),
        ('Order Consolidation', 'Logistics Scheduling'),
        ('Logistics Scheduling', 'Customer Feedback'),
        ('Customer Feedback', 'Certification Audit'),
        ('Certification Audit', 'Recipe Adjustment'),
        ('Recipe Adjustment', 'Batch Curdling')
    ]
)

# Print the root
print(root)