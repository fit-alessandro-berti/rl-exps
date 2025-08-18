from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
root = StrictPartialOrder(
    nodes=[
        Transition(label='Assess Structure'),
        Transition(label='Analyze Environment'),
        Transition(label='Design Modules'),
        Transition(label='Procure Materials'),
        Transition(label='Install Irrigation'),
        Transition(label='Set Sensors'),
        Transition(label='Select Seeds'),
        Transition(label='Schedule Planting'),
        Transition(label='Monitor Growth'),
        Transition(label='Collect Data'),
        Transition(label='Manage Pests'),
        Transition(label='Harvest Crops'),
        Transition(label='Coordinate Sales'),
        Transition(label='Compost Waste'),
        Transition(label='Review Feedback')
    ],
    order={
        ('Assess Structure', 'Analyze Environment'),
        ('Analyze Environment', 'Design Modules'),
        ('Design Modules', 'Procure Materials'),
        ('Procure Materials', 'Install Irrigation'),
        ('Install Irrigation', 'Set Sensors'),
        ('Set Sensors', 'Select Seeds'),
        ('Select Seeds', 'Schedule Planting'),
        ('Schedule Planting', 'Monitor Growth'),
        ('Monitor Growth', 'Collect Data'),
        ('Collect Data', 'Manage Pests'),
        ('Manage Pests', 'Harvest Crops'),
        ('Harvest Crops', 'Coordinate Sales'),
        ('Coordinate Sales', 'Compost Waste'),
        ('Compost Waste', 'Review Feedback')
    }
)

# Print the final POWL model
print(root)