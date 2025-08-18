from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Flora Mapping': Transition(label='Flora Mapping'),
    'Hive Setup': Transition(label='Hive Setup'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Health Check': Transition(label='Health Check'),
    'Pest Control': Transition(label='Pest Control'),
    'Data Logging': Transition(label='Data Logging'),
    'Community Meet': Transition(label='Community Meet'),
    'Workshop Plan': Transition(label='Workshop Plan'),
    'Honey Extract': Transition(label='Honey Extract'),
    'Quality Test': Transition(label='Quality Test'),
    'Packaging': Transition(label='Packaging'),
    'Market Setup': Transition(label='Market Setup'),
    'Sales Report': Transition(label='Sales Report'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Waste Manage': Transition(label='Waste Manage'),
    'Seasonal Review': Transition(label='Seasonal Review')
}

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        activities['Site Survey'],
        activities['Flora Mapping'],
        activities['Hive Setup'],
        activities['Sensor Install'],
        activities['Health Check'],
        activities['Pest Control'],
        activities['Data Logging'],
        activities['Community Meet'],
        activities['Workshop Plan'],
        activities['Honey Extract'],
        activities['Quality Test'],
        activities['Packaging'],
        activities['Market Setup'],
        activities['Sales Report'],
        activities['Regulation Check'],
        activities['Waste Manage'],
        activities['Seasonal Review']
    ],
    order=[
        (activities['Site Survey'], activities['Flora Mapping']),
        (activities['Flora Mapping'], activities['Hive Setup']),
        (activities['Hive Setup'], activities['Sensor Install']),
        (activities['Sensor Install'], activities['Health Check']),
        (activities['Health Check'], activities['Pest Control']),
        (activities['Pest Control'], activities['Data Logging']),
        (activities['Data Logging'], activities['Community Meet']),
        (activities['Community Meet'], activities['Workshop Plan']),
        (activities['Workshop Plan'], activities['Honey Extract']),
        (activities['Honey Extract'], activities['Quality Test']),
        (activities['Quality Test'], activities['Packaging']),
        (activities['Packaging'], activities['Market Setup']),
        (activities['Market Setup'], activities['Sales Report']),
        (activities['Sales Report'], activities['Regulation Check']),
        (activities['Regulation Check'], activities['Waste Manage']),
        (activities['Waste Manage'], activities['Seasonal Review'])
    ]
)

# Print the final result
print(root)