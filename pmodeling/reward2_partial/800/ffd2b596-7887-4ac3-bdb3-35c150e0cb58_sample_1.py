import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = {
    'Component Sourcing': Transition(label='Component Sourcing'),
    'Sensor Calibrate': Transition(label='Sensor Calibrate'),
    'Motor Assembly': Transition(label='Motor Assembly'),
    'Frame Build': Transition(label='Frame Build'),
    'Software Install': Transition(label='Software Install'),
    'Algorithm Tune': Transition(label='Algorithm Tune'),
    'Battery Integrate': Transition(label='Battery Integrate'),
    'Signal Test': Transition(label='Signal Test'),
    'Durability Check': Transition(label='Durability Check'),
    'Flight Simulate': Transition(label='Flight Simulate'),
    'Quality Inspect': Transition(label='Quality Inspect'),
    'Compliance Review': Transition(label='Compliance Review'),
    'Packaging Prep': Transition(label='Packaging Prep'),
    'Logistics Plan': Transition(label='Logistics Plan'),
    'Client Feedback': Transition(label='Client Feedback')
}

# Create the Partial Order
root = StrictPartialOrder(nodes=[activities['Component Sourcing'], 
                                 activities['Sensor Calibrate'], 
                                 activities['Motor Assembly'], 
                                 activities['Frame Build'], 
                                 activities['Software Install'], 
                                 activities['Algorithm Tune'], 
                                 activities['Battery Integrate'], 
                                 activities['Signal Test'], 
                                 activities['Durability Check'], 
                                 activities['Flight Simulate'], 
                                 activities['Quality Inspect'], 
                                 activities['Compliance Review'], 
                                 activities['Packaging Prep'], 
                                 activities['Logistics Plan'], 
                                 activities['Client Feedback']])

# Add edges to represent the dependencies between activities
root.order.add_edge(activities['Component Sourcing'], activities['Sensor Calibrate'])
root.order.add_edge(activities['Sensor Calibrate'], activities['Motor Assembly'])
root.order.add_edge(activities['Motor Assembly'], activities['Frame Build'])
root.order.add_edge(activities['Frame Build'], activities['Software Install'])
root.order.add_edge(activities['Software Install'], activities['Algorithm Tune'])
root.order.add_edge(activities['Algorithm Tune'], activities['Battery Integrate'])
root.order.add_edge(activities['Battery Integrate'], activities['Signal Test'])
root.order.add_edge(activities['Signal Test'], activities['Durability Check'])
root.order.add_edge(activities['Durability Check'], activities['Flight Simulate'])
root.order.add_edge(activities['Flight Simulate'], activities['Quality Inspect'])
root.order.add_edge(activities['Quality Inspect'], activities['Compliance Review'])
root.order.add_edge(activities['Compliance Review'], activities['Packaging Prep'])
root.order.add_edge(activities['Packaging Prep'], activities['Logistics Plan'])
root.order.add_edge(activities['Logistics Plan'], activities['Client Feedback'])

print(root)