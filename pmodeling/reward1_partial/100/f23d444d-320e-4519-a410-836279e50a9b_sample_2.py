import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with exact names
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'System Design': Transition(label='System Design'),
    'Module Build': Transition(label='Module Build'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Planting Plan': Transition(label='Planting Plan'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Climate Control': Transition(label='Climate Control'),
    'Lighting Adjust': Transition(label='Lighting Adjust'),
    'Pest Monitor': Transition(label='Pest Monitor'),
    'Waste Cycle': Transition(label='Waste Cycle'),
    'Data Capture': Transition(label='Data Capture'),
    'Yield Forecast': Transition(label='Yield Forecast'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Community Meet': Transition(label='Community Meet'),
    'Harvest Prep': Transition(label='Harvest Prep'),
    'Market Link': Transition(label='Market Link')
}

# Define the partial order structure
root = StrictPartialOrder(nodes=[])
root.order.add_edge(activities['Site Survey'], activities['System Design'])
root.order.add_edge(activities['System Design'], activities['Module Build'])
root.order.add_edge(activities['Module Build'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Seed Selection'])
root.order.add_edge(activities['Seed Selection'], activities['Planting Plan'])
root.order.add_edge(activities['Planting Plan'], activities['Irrigation Setup'])
root.order.add_edge(activities['Irrigation Setup'], activities['Climate Control'])
root.order.add_edge(activities['Climate Control'], activities['Lighting Adjust'])
root.order.add_edge(activities['Lighting Adjust'], activities['Pest Monitor'])
root.order.add_edge(activities['Pest Monitor'], activities['Waste Cycle'])
root.order.add_edge(activities['Waste Cycle'], activities['Data Capture'])
root.order.add_edge(activities['Data Capture'], activities['Yield Forecast'])
root.order.add_edge(activities['Yield Forecast'], activities['Regulation Check'])
root.order.add_edge(activities['Regulation Check'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Harvest Prep'])
root.order.add_edge(activities['Harvest Prep'], activities['Market Link'])