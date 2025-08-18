from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition('Colony Sourcing'),
    Transition('Hive Design'),
    Transition('Site Survey'),
    Transition('Installation Prep'),
    Transition('Hive Setup'),
    Transition('Sensor Install'),
    Transition('Health Monitor'),
    Transition('Pest Control'),
    Transition('Honey Harvest'),
    Transition('Wax Processing'),
    Transition('Product Packaging'),
    Transition('Order Dispatch'),
    Transition('Workshop Setup'),
    Transition('Community Outreach'),
    Transition('Regulation Check'),
    Transition('Data Analysis'),
    Transition('Maintenance Plan')
])

# Define the dependencies between the activities
root.order.add_edge('Colony Sourcing', 'Hive Design')
root.order.add_edge('Hive Design', 'Site Survey')
root.order.add_edge('Site Survey', 'Installation Prep')
root.order.add_edge('Installation Prep', 'Hive Setup')
root.order.add_edge('Hive Setup', 'Sensor Install')
root.order.add_edge('Sensor Install', 'Health Monitor')
root.order.add_edge('Health Monitor', 'Pest Control')
root.order.add_edge('Pest Control', 'Honey Harvest')
root.order.add_edge('Honey Harvest', 'Wax Processing')
root.order.add_edge('Wax Processing', 'Product Packaging')
root.order.add_edge('Product Packaging', 'Order Dispatch')
root.order.add_edge('Order Dispatch', 'Workshop Setup')
root.order.add_edge('Workshop Setup', 'Community Outreach')
root.order.add_edge('Community Outreach', 'Regulation Check')
root.order.add_edge('Regulation Check', 'Data Analysis')
root.order.add_edge('Data Analysis', 'Maintenance Plan')

print(root)