from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

root = StrictPartialOrder(
    nodes=[
        Transition(label='Milk Sourcing'),
        Transition(label='Quality Testing'),
        Transition(label='Milk Pasteurize'),
        Transition(label='Culture Inoculate'),
        Transition(label='Coagulation'),
        Transition(label='Curd Cutting'),
        Transition(label='Whey Drain'),
        Transition(label='Pressing'),
        Transition(label='Salting'),
        Transition(label='Aging Control'),
        Transition(label='Sensory Audit'),
        Transition(label='Packaging Design'),
        Transition(label='Label Approval'),
        Transition(label='Order Customization'),
        Transition(label='Logistics Plan'),
        Transition(label='Market Delivery'),
        Transition(label='Customer Feedback'),
        Transition(label='Regulatory Check')
    ],
    order=[
        ('Milk Sourcing', 'Quality Testing'),
        ('Quality Testing', 'Milk Pasteurize'),
        ('Milk Pasteurize', 'Culture Inoculate'),
        ('Culture Inoculate', 'Coagulation'),
        ('Coagulation', 'Curd Cutting'),
        ('Curd Cutting', 'Whey Drain'),
        ('Whey Drain', 'Pressing'),
        ('Pressing', 'Salting'),
        ('Salting', 'Aging Control'),
        ('Aging Control', 'Sensory Audit'),
        ('Sensory Audit', 'Packaging Design'),
        ('Packaging Design', 'Label Approval'),
        ('Label Approval', 'Order Customization'),
        ('Order Customization', 'Logistics Plan'),
        ('Logistics Plan', 'Market Delivery'),
        ('Market Delivery', 'Customer Feedback'),
        ('Customer Feedback', 'Regulatory Check')
    ]
)