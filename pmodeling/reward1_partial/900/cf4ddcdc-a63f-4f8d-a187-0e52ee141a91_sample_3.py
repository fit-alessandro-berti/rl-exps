import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Return Request'),
        Transition(label='Authorization Check'),
        Transition(label='Pickup Schedule'),
        Transition(label='Transport Dispatch'),
        Transition(label='Receiving Goods'),
        Transition(label='Quality Inspect'),
        Transition(label='Sort Items'),
        Transition(label='Refurbish Prep'),
        Transition(label='Recycle Process'),
        Transition(label='Inventory Update'),
        Transition(label='Customer Notify'),
        Transition(label='Disposal Arrange'),
        Transition(label='Compliance Audit'),
        Transition(label='Cost Analysis'),
        Transition(label='Report Generate')
    ],
    order={
        # Define the dependencies between activities
        ('Return Request', 'Authorization Check'): None,
        ('Authorization Check', 'Pickup Schedule'): None,
        ('Pickup Schedule', 'Transport Dispatch'): None,
        ('Transport Dispatch', 'Receiving Goods'): None,
        ('Receiving Goods', 'Quality Inspect'): None,
        ('Quality Inspect', 'Sort Items'): None,
        ('Sort Items', 'Refurbish Prep'): None,
        ('Refurbish Prep', 'Recycle Process'): None,
        ('Recycle Process', 'Inventory Update'): None,
        ('Inventory Update', 'Customer Notify'): None,
        ('Customer Notify', 'Disposal Arrange'): None,
        ('Disposal Arrange', 'Compliance Audit'): None,
        ('Compliance Audit', 'Cost Analysis'): None,
        ('Cost Analysis', 'Report Generate'): None
    }
)

# Add the dependencies between activities
root.order.add_edge('Return Request', 'Authorization Check')
root.order.add_edge('Authorization Check', 'Pickup Schedule')
root.order.add_edge('Pickup Schedule', 'Transport Dispatch')
root.order.add_edge('Transport Dispatch', 'Receiving Goods')
root.order.add_edge('Receiving Goods', 'Quality Inspect')
root.order.add_edge('Quality Inspect', 'Sort Items')
root.order.add_edge('Sort Items', 'Refurbish Prep')
root.order.add_edge('Refurbish Prep', 'Recycle Process')
root.order.add_edge('Recycle Process', 'Inventory Update')
root.order.add_edge('Inventory Update', 'Customer Notify')
root.order.add_edge('Customer Notify', 'Disposal Arrange')
root.order.add_edge('Disposal Arrange', 'Compliance Audit')
root.order.add_edge('Compliance Audit', 'Cost Analysis')
root.order.add_edge('Cost Analysis', 'Report Generate')

# Print the POWL model
print(root)