from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Seed Selection'),
        Transition(label='Nutrient Mix'),
        Transition(label='Planting Setup'),
        Transition(label='Climate Control'),
        Transition(label='Water Cycling'),
        Transition(label='Growth Monitoring'),
        Transition(label='Pest Detection'),
        Transition(label='Light Adjustment'),
        Transition(label='Data Analysis'),
        Transition(label='Harvest Planning'),
        Transition(label='Crop Harvest'),
        Transition(label='Yield Sorting'),
        Transition(label='Packaging Prep'),
        Transition(label='Distribution Plan'),
        Transition(label='Regulation Check'),
        Transition(label='Waste Recycling'),
        Transition(label='System Maintenance')
    ],
    order={
        'Seed Selection': {'Nutrient Mix'},
        'Nutrient Mix': {'Planting Setup'},
        'Planting Setup': {'Climate Control'},
        'Climate Control': {'Water Cycling'},
        'Water Cycling': {'Growth Monitoring'},
        'Growth Monitoring': {'Pest Detection'},
        'Pest Detection': {'Light Adjustment'},
        'Light Adjustment': {'Data Analysis'},
        'Data Analysis': {'Harvest Planning'},
        'Harvest Planning': {'Crop Harvest'},
        'Crop Harvest': {'Yield Sorting'},
        'Yield Sorting': {'Packaging Prep'},
        'Packaging Prep': {'Distribution Plan'},
        'Distribution Plan': {'Regulation Check'},
        'Regulation Check': {'Waste Recycling'},
        'Waste Recycling': {'System Maintenance'}
    }
)

print(root)