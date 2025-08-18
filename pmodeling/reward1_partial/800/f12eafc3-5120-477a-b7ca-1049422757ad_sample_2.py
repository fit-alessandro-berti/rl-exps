import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities with their labels
activities = {
    'Milk Selection': Transition(label='Milk Selection'),
    'Quality Testing': Transition(label='Quality Testing'),
    'Milk Pasteurize': Transition(label='Milk Pasteurize'),
    'Cheese Crafting': Transition(label='Cheese Crafting'),
    'Controlled Aging': Transition(label='Controlled Aging'),
    'Sensory Review': Transition(label='Sensory Review'),
    'Custom Packaging': Transition(label='Custom Packaging'),
    'Label Printing': Transition(label='Label Printing'),
    'Export Licensing': Transition(label='Export Licensing'),
    'Documentation Prep': Transition(label='Documentation Prep'),
    'Customs Clearance': Transition(label='Customs Clearance'),
    'Cold Shipping': Transition(label='Cold Shipping'),
    'Delivery Tracking': Transition(label='Delivery Tracking'),
    'Feedback Review': Transition(label='Feedback Review'),
    'Market Analysis': Transition(label='Market Analysis')
}

# Define the partial order structure
root = StrictPartialOrder(nodes=list(activities.values()))

# Define dependencies between activities
root.order.add_edge(activities['Milk Selection'], activities['Quality Testing'])
root.order.add_edge(activities['Quality Testing'], activities['Milk Pasteurize'])
root.order.add_edge(activities['Milk Pasteurize'], activities['Cheese Crafting'])
root.order.add_edge(activities['Cheese Crafting'], activities['Controlled Aging'])
root.order.add_edge(activities['Controlled Aging'], activities['Sensory Review'])
root.order.add_edge(activities['Sensory Review'], activities['Custom Packaging'])
root.order.add_edge(activities['Custom Packaging'], activities['Label Printing'])
root.order.add_edge(activities['Label Printing'], activities['Export Licensing'])
root.order.add_edge(activities['Export Licensing'], activities['Documentation Prep'])
root.order.add_edge(activities['Documentation Prep'], activities['Customs Clearance'])
root.order.add_edge(activities['Customs Clearance'], activities['Cold Shipping'])
root.order.add_edge(activities['Cold Shipping'], activities['Delivery Tracking'])
root.order.add_edge(activities['Delivery Tracking'], activities['Feedback Review'])
root.order.add_edge(activities['Feedback Review'], activities['Market Analysis'])

# Print the root model
print(root)