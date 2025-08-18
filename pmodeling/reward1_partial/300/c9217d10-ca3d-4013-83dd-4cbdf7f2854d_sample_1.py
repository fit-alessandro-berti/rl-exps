from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Climate Study': Transition(label='Climate Study'),
    'Design Layout': Transition(label='Design Layout'),
    'System Install': Transition(label='System Install'),
    'Crop Select': Transition(label='Crop Select'),
    'Nutrient Plan': Transition(label='Nutrient Plan'),
    'Sensor Setup': Transition(label='Sensor Setup'),
    'Automation Test': Transition(label='Automation Test'),
    'Staff Train': Transition(label='Staff Train'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Marketing Sync': Transition(label='Marketing Sync'),
    'Data Monitor': Transition(label='Data Monitor'),
    'Yield Analyze': Transition(label='Yield Analyze'),
    'Supply Chain': Transition(label='Supply Chain'),
    'Customer Engage': Transition(label='Customer Engage')
}

# Define the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))
root.order.add_edge(activities['Site Survey'], activities['Climate Study'])
root.order.add_edge(activities['Climate Study'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['System Install'])
root.order.add_edge(activities['System Install'], activities['Crop Select'])
root.order.add_edge(activities['Crop Select'], activities['Nutrient Plan'])
root.order.add_edge(activities['Nutrient Plan'], activities['Sensor Setup'])
root.order.add_edge(activities['Sensor Setup'], activities['Automation Test'])
root.order.add_edge(activities['Automation Test'], activities['Staff Train'])
root.order.add_edge(activities['Staff Train'], activities['Compliance Check'])
root.order.add_edge(activities['Compliance Check'], activities['Marketing Sync'])
root.order.add_edge(activities['Marketing Sync'], activities['Data Monitor'])
root.order.add_edge(activities['Data Monitor'], activities['Yield Analyze'])
root.order.add_edge(activities['Yield Analyze'], activities['Supply Chain'])
root.order.add_edge(activities['Supply Chain'], activities['Customer Engage'])