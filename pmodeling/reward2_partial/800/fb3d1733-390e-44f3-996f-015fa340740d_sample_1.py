import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = {
    'Initial Assess': Transition(label='Initial Assess'),
    'Disassemble Parts': Transition(label='Disassemble Parts'),
    'Ultrasonic Clean': Transition(label='Ultrasonic Clean'),
    'Inspect Components': Transition(label='Inspect Components'),
    'Fabricate Gears': Transition(label='Fabricate Gears'),
    'Dial Restoration': Transition(label='Dial Restoration'),
    'Repaint Markers': Transition(label='Repaint Markers'),
    'Reassemble Movement': Transition(label='Reassemble Movement'),
    'Lubricate Bearings': Transition(label='Lubricate Bearings'),
    'Calibrate Timing': Transition(label='Calibrate Timing'),
    'Polish Case': Transition(label='Polish Case'),
    'Re-case Watch': Transition(label='Re-case Watch'),
    'Quality Testing': Transition(label='Quality Testing'),
    'Document Process': Transition(label='Document Process'),
    'Package Product': Transition(label='Package Product')
}

# Define the partial order graph
root = StrictPartialOrder(nodes=[
    activities['Initial Assess'],
    activities['Disassemble Parts'],
    activities['Ultrasonic Clean'],
    activities['Inspect Components'],
    activities['Fabricate Gears'],
    activities['Dial Restoration'],
    activities['Repaint Markers'],
    activities['Reassemble Movement'],
    activities['Lubricate Bearings'],
    activities['Calibrate Timing'],
    activities['Polish Case'],
    activities['Re-case Watch'],
    activities['Quality Testing'],
    activities['Document Process'],
    activities['Package Product']
])

# Define the partial order dependencies
root.order.add_edge(activities['Initial Assess'], activities['Disassemble Parts'])
root.order.add_edge(activities['Disassemble Parts'], activities['Ultrasonic Clean'])
root.order.add_edge(activities['Ultrasonic Clean'], activities['Inspect Components'])
root.order.add_edge(activities['Inspect Components'], activities['Fabricate Gears'])
root.order.add_edge(activities['Fabricate Gears'], activities['Dial Restoration'])
root.order.add_edge(activities['Dial Restoration'], activities['Repaint Markers'])
root.order.add_edge(activities['Repaint Markers'], activities['Reassemble Movement'])
root.order.add_edge(activities['Reassemble Movement'], activities['Lubricate Bearings'])
root.order.add_edge(activities['Lubricate Bearings'], activities['Calibrate Timing'])
root.order.add_edge(activities['Calibrate Timing'], activities['Polish Case'])
root.order.add_edge(activities['Polish Case'], activities['Re-case Watch'])
root.order.add_edge(activities['Re-case Watch'], activities['Quality Testing'])
root.order.add_edge(activities['Quality Testing'], activities['Document Process'])
root.order.add_edge(activities['Document Process'], activities['Package Product'])

print(root)