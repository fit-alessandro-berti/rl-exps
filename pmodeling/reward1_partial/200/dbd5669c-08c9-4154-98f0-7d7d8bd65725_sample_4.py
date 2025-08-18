import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the urban vertical farm process
root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Layout'),
        Transition(label='Material Sourcing'),
        Transition(label='Unit Assembly'),
        Transition(label='System Wiring'),
        Transition(label='Sensor Install'),
        Transition(label='Water Testing'),
        Transition(label='Nutrient Mix'),
        Transition(label='Seed Selection'),
        Transition(label='Planting Setup'),
        Transition(label='Climate Control'),
        Transition(label='Pest Management'),
        Transition(label='Data Calibration'),
        Transition(label='Yield Analysis'),
        Transition(label='Community Meet'),
        Transition(label='Compliance Check'),
        Transition(label='Expansion Plan')
    ],
    order={
        ('Site Survey', 'Design Layout'): True,
        ('Design Layout', 'Material Sourcing'): True,
        ('Material Sourcing', 'Unit Assembly'): True,
        ('Unit Assembly', 'System Wiring'): True,
        ('System Wiring', 'Sensor Install'): True,
        ('Sensor Install', 'Water Testing'): True,
        ('Water Testing', 'Nutrient Mix'): True,
        ('Nutrient Mix', 'Seed Selection'): True,
        ('Seed Selection', 'Planting Setup'): True,
        ('Planting Setup', 'Climate Control'): True,
        ('Climate Control', 'Pest Management'): True,
        ('Pest Management', 'Data Calibration'): True,
        ('Data Calibration', 'Yield Analysis'): True,
        ('Yield Analysis', 'Community Meet'): True,
        ('Community Meet', 'Compliance Check'): True,
        ('Compliance Check', 'Expansion Plan'): True
    }
)

print(root)