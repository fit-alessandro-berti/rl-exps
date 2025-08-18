from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Load Test'),
        Transition(label='Soil Sample'),
        Transition(label='Climate Check'),
        Transition(label='Crop Select'),
        Transition(label='Irrigation Plan'),
        Transition(label='Energy Setup'),
        Transition(label='Pest Control'),
        Transition(label='Permit Obtain'),
        Transition(label='Stakeholder Meet'),
        Transition(label='Bed Construction'),
        Transition(label='Seed Planting'),
        Transition(label='Water Schedule'),
        Transition(label='Growth Monitor'),
        Transition(label='Harvest Plan'),
        Transition(label='Waste Recycle'),
        Transition(label='Yield Report')
    ],
    order={
        ('Site Survey', 'Load Test'): 1,
        ('Load Test', 'Soil Sample'): 1,
        ('Soil Sample', 'Climate Check'): 1,
        ('Climate Check', 'Crop Select'): 1,
        ('Crop Select', 'Irrigation Plan'): 1,
        ('Irrigation Plan', 'Energy Setup'): 1,
        ('Energy Setup', 'Pest Control'): 1,
        ('Pest Control', 'Permit Obtain'): 1,
        ('Permit Obtain', 'Stakeholder Meet'): 1,
        ('Stakeholder Meet', 'Bed Construction'): 1,
        ('Bed Construction', 'Seed Planting'): 1,
        ('Seed Planting', 'Water Schedule'): 1,
        ('Water Schedule', 'Growth Monitor'): 1,
        ('Growth Monitor', 'Harvest Plan'): 1,
        ('Harvest Plan', 'Waste Recycle'): 1,
        ('Waste Recycle', 'Yield Report'): 1
    }
)