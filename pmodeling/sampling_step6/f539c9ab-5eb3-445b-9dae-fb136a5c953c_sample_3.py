import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structural Audit': Transition(label='Structural Audit'),
    'Modular Design': Transition(label='Modular Design'),
    'Hydroponic Setup': Transition(label='Hydroponic Setup'),
    'Climate Config': Transition(label='Climate Config'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Pest Detect': Transition(label='Pest Detect'),
    'Lighting Setup': Transition(label='Lighting Setup'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Automation Install': Transition(label='Automation Install'),
    'Staff Training': Transition(label='Staff Training'),
    'Market Analysis': Transition(label='Market Analysis'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Yield Monitor': Transition(label='Yield Monitor'),
    'Waste Manage': Transition(label='Waste Manage'),
    'Data Analytics': Transition(label='Data Analytics')
}

# Create the partial order workflow model
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Structural Audit'],
    activities['Modular Design'],
    activities['Hydroponic Setup'],
    activities['Climate Config'],
    activities['Nutrient Mix'],
    activities['Pest Detect'],
    activities['Lighting Setup'],
    activities['Energy Audit'],
    activities['Automation Install'],
    activities['Staff Training'],
    activities['Market Analysis'],
    activities['Regulation Check'],
    activities['Yield Monitor'],
    activities['Waste Manage'],
    activities['Data Analytics']
])

# Add dependencies if needed (this example assumes no dependencies)
# root.order.add_edge(loop, xor)

print(root)