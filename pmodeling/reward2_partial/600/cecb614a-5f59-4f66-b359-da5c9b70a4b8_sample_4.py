import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Load Testing': Transition(label='Load Testing'),
    'Crop Selection': Transition(label='Crop Selection'),
    'Soil Prep': Transition(label='Soil Prep'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Permits Acquire': Transition(label='Permits Acquire'),
    'Supplier Outreach': Transition(label='Supplier Outreach'),
    'Planting Seedlings': Transition(label='Planting Seedlings'),
    'Pest Monitoring': Transition(label='Pest Monitoring'),
    'Nutrient Testing': Transition(label='Nutrient Testing'),
    'Waste Sorting': Transition(label='Waste Sorting'),
    'Staff Training': Transition(label='Staff Training'),
    'Community Meet': Transition(label='Community Meet'),
    'Harvest Planning': Transition(label='Harvest Planning'),
    'Market Launch': Transition(label='Market Launch'),
    'Yield Tracking': Transition(label='Yield Tracking')
}

# Define the partial order graph
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Load Testing'],
    activities['Crop Selection'],
    activities['Soil Prep'],
    activities['Irrigation Setup'],
    activities['Permits Acquire'],
    activities['Supplier Outreach'],
    activities['Planting Seedlings'],
    activities['Pest Monitoring'],
    activities['Nutrient Testing'],
    activities['Waste Sorting'],
    activities['Staff Training'],
    activities['Community Meet'],
    activities['Harvest Planning'],
    activities['Market Launch'],
    activities['Yield Tracking']
])

# Define the dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Load Testing'])
root.order.add_edge(activities['Load Testing'], activities['Crop Selection'])
root.order.add_edge(activities['Crop Selection'], activities['Soil Prep'])
root.order.add_edge(activities['Soil Prep'], activities['Irrigation Setup'])
root.order.add_edge(activities['Irrigation Setup'], activities['Permits Acquire'])
root.order.add_edge(activities['Permits Acquire'], activities['Supplier Outreach'])
root.order.add_edge(activities['Supplier Outreach'], activities['Planting Seedlings'])
root.order.add_edge(activities['Planting Seedlings'], activities['Pest Monitoring'])
root.order.add_edge(activities['Pest Monitoring'], activities['Nutrient Testing'])
root.order.add_edge(activities['Nutrient Testing'], activities['Waste Sorting'])
root.order.add_edge(activities['Waste Sorting'], activities['Staff Training'])
root.order.add_edge(activities['Staff Training'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Harvest Planning'])
root.order.add_edge(activities['Harvest Planning'], activities['Market Launch'])
root.order.add_edge(activities['Market Launch'], activities['Yield Tracking'])

# Print the final result
print(root)