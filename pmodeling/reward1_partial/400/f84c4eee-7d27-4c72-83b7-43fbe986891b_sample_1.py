import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Component Sourcing': Transition(label='Component Sourcing'),
    'Frame Assembly': Transition(label='Frame Assembly'),
    'Sensor Mounting': Transition(label='Sensor Mounting'),
    'Wiring Harness': Transition(label='Wiring Harness'),
    'Circuit Testing': Transition(label='Circuit Testing'),
    'Firmware Loading': Transition(label='Firmware Loading'),
    'Initial Calibration': Transition(label='Initial Calibration'),
    'Software Integration': Transition(label='Software Integration'),
    'Flight Testing': Transition(label='Flight Testing'),
    'Data Logging': Transition(label='Data Logging'),
    'Performance Tuning': Transition(label='Performance Tuning'),
    'Packaging Prep': Transition(label='Packaging Prep'),
    'Custom Labeling': Transition(label='Custom Labeling'),
    'Documentation Print': Transition(label='Documentation Print'),
    'Quality Review': Transition(label='Quality Review'),
    'Client Training': Transition(label='Client Training'),
    'Remote Monitoring': Transition(label='Remote Monitoring'),
    'Firmware Update': Transition(label='Firmware Update')
}

# Define the partial order
root = StrictPartialOrder(nodes=[
    activities['Component Sourcing'],
    activities['Frame Assembly'],
    activities['Sensor Mounting'],
    activities['Wiring Harness'],
    activities['Circuit Testing'],
    activities['Firmware Loading'],
    activities['Initial Calibration'],
    activities['Software Integration'],
    activities['Flight Testing'],
    activities['Data Logging'],
    activities['Performance Tuning'],
    activities['Packaging Prep'],
    activities['Custom Labeling'],
    activities['Documentation Print'],
    activities['Quality Review'],
    activities['Client Training'],
    activities['Remote Monitoring'],
    activities['Firmware Update']
])

# Define the dependencies
root.order.add_edge(activities['Component Sourcing'], activities['Frame Assembly'])
root.order.add_edge(activities['Frame Assembly'], activities['Sensor Mounting'])
root.order.add_edge(activities['Sensor Mounting'], activities['Wiring Harness'])
root.order.add_edge(activities['Wiring Harness'], activities['Circuit Testing'])
root.order.add_edge(activities['Circuit Testing'], activities['Firmware Loading'])
root.order.add_edge(activities['Firmware Loading'], activities['Initial Calibration'])
root.order.add_edge(activities['Initial Calibration'], activities['Software Integration'])
root.order.add_edge(activities['Software Integration'], activities['Flight Testing'])
root.order.add_edge(activities['Flight Testing'], activities['Data Logging'])
root.order.add_edge(activities['Data Logging'], activities['Performance Tuning'])
root.order.add_edge(activities['Performance Tuning'], activities['Packaging Prep'])
root.order.add_edge(activities['Packaging Prep'], activities['Custom Labeling'])
root.order.add_edge(activities['Custom Labeling'], activities['Documentation Print'])
root.order.add_edge(activities['Documentation Print'], activities['Quality Review'])
root.order.add_edge(activities['Quality Review'], activities['Client Training'])
root.order.add_edge(activities['Client Training'], activities['Remote Monitoring'])
root.order.add_edge(activities['Remote Monitoring'], activities['Firmware Update'])

print(root)