import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their corresponding labels
activities = {
    'Design Consult': Transition(label='Design Consult'),
    'Component Sourcing': Transition(label='Component Sourcing'),
    'Sensor Calibrate': Transition(label='Sensor Calibrate'),
    'Firmware Integrate': Transition(label='Firmware Integrate'),
    'Payload Configure': Transition(label='Payload Configure'),
    'Assembly Setup': Transition(label='Assembly Setup'),
    'Wiring Connect': Transition(label='Wiring Connect'),
    'Chassis Build': Transition(label='Chassis Build'),
    'Software Load': Transition(label='Software Load'),
    'Flight Testing': Transition(label='Flight Testing'),
    'Data Analyze': Transition(label='Data Analyze'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Quality Inspect': Transition(label='Quality Inspect'),
    'Packaging Prep': Transition(label='Packaging Prep'),
    'Logistics Plan': Transition(label='Logistics Plan'),
    'Client Review': Transition(label='Client Review')
}

# Define the partial order
root = StrictPartialOrder(nodes=activities.values())

# Define the order relationships
root.order.add_edge(activities['Design Consult'], activities['Component Sourcing'])
root.order.add_edge(activities['Component Sourcing'], activities['Sensor Calibrate'])
root.order.add_edge(activities['Sensor Calibrate'], activities['Firmware Integrate'])
root.order.add_edge(activities['Firmware Integrate'], activities['Payload Configure'])
root.order.add_edge(activities['Payload Configure'], activities['Assembly Setup'])
root.order.add_edge(activities['Assembly Setup'], activities['Wiring Connect'])
root.order.add_edge(activities['Wiring Connect'], activities['Chassis Build'])
root.order.add_edge(activities['Chassis Build'], activities['Software Load'])
root.order.add_edge(activities['Software Load'], activities['Flight Testing'])
root.order.add_edge(activities['Flight Testing'], activities['Data Analyze'])
root.order.add_edge(activities['Data Analyze'], activities['Regulation Check'])
root.order.add_edge(activities['Regulation Check'], activities['Quality Inspect'])
root.order.add_edge(activities['Quality Inspect'], activities['Packaging Prep'])
root.order.add_edge(activities['Packaging Prep'], activities['Logistics Plan'])
root.order.add_edge(activities['Logistics Plan'], activities['Client Review'])

# Print the root of the POWL model
print(root)