from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Impact Study': Transition(label='Impact Study'),
    'Structure Check': Transition(label='Structure Check'),
    'Soil Testing': Transition(label='Soil Testing'),
    'System Design': Transition(label='System Design'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Lighting Install': Transition(label='Lighting Install'),
    'Pest Control': Transition(label='Pest Control'),
    'Community Meet': Transition(label='Community Meet'),
    'Regulation Review': Transition(label='Regulation Review'),
    'Waste Plan': Transition(label='Waste Plan'),
    'Crop Monitor': Transition(label='Crop Monitor'),
    'Harvest Prep': Transition(label='Harvest Prep'),
    'Market Launch': Transition(label='Market Launch')
}

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        activities['Site Survey'],
        activities['Impact Study'],
        activities['Structure Check'],
        activities['Soil Testing'],
        activities['System Design'],
        activities['Seed Selection'],
        activities['Irrigation Setup'],
        activities['Lighting Install'],
        activities['Pest Control'],
        activities['Community Meet'],
        activities['Regulation Review'],
        activities['Waste Plan'],
        activities['Crop Monitor'],
        activities['Harvest Prep'],
        activities['Market Launch']
    ]
)

# Define the dependencies between the activities
root.order.add_edge(activities['Site Survey'], activities['Impact Study'])
root.order.add_edge(activities['Site Survey'], activities['Structure Check'])
root.order.add_edge(activities['Site Survey'], activities['Soil Testing'])
root.order.add_edge(activities['Site Survey'], activities['System Design'])
root.order.add_edge(activities['Impact Study'], activities['System Design'])
root.order.add_edge(activities['Impact Study'], activities['Seed Selection'])
root.order.add_edge(activities['Impact Study'], activities['Irrigation Setup'])
root.order.add_edge(activities['Impact Study'], activities['Lighting Install'])
root.order.add_edge(activities['Impact Study'], activities['Pest Control'])
root.order.add_edge(activities['Impact Study'], activities['Community Meet'])
root.order.add_edge(activities['Impact Study'], activities['Regulation Review'])
root.order.add_edge(activities['Impact Study'], activities['Waste Plan'])
root.order.add_edge(activities['Impact Study'], activities['Crop Monitor'])
root.order.add_edge(activities['Impact Study'], activities['Harvest Prep'])
root.order.add_edge(activities['Impact Study'], activities['Market Launch'])
root.order.add_edge(activities['Structure Check'], activities['System Design'])
root.order.add_edge(activities['Structure Check'], activities['Seed Selection'])
root.order.add_edge(activities['Structure Check'], activities['Irrigation Setup'])
root.order.add_edge(activities['Structure Check'], activities['Lighting Install'])
root.order.add_edge(activities['Structure Check'], activities['Pest Control'])
root.order.add_edge(activities['Structure Check'], activities['Community Meet'])
root.order.add_edge(activities['Structure Check'], activities['Regulation Review'])
root.order.add_edge(activities['Structure Check'], activities['Waste Plan'])
root.order.add_edge(activities['Structure Check'], activities['Crop Monitor'])
root.order.add_edge(activities['Structure Check'], activities['Harvest Prep'])
root.order.add_edge(activities['Structure Check'], activities['Market Launch'])
root.order.add_edge(activities['Soil Testing'], activities['System Design'])
root.order.add_edge(activities['Soil Testing'], activities['Seed Selection'])
root.order.add_edge(activities['Soil Testing'], activities['Irrigation Setup'])
root.order.add_edge(activities['Soil Testing'], activities['Lighting Install'])
root.order.add_edge(activities['Soil Testing'], activities['Pest Control'])
root.order.add_edge(activities['Soil Testing'], activities['Community Meet'])
root.order.add_edge(activities['Soil Testing'], activities['Regulation Review'])
root.order.add_edge(activities['Soil Testing'], activities['Waste Plan'])
root.order.add_edge(activities['Soil Testing'], activities['Crop Monitor'])
root.order.add_edge(activities['Soil Testing'], activities['Harvest Prep'])
root.order.add_edge(activities['Soil Testing'], activities['Market Launch'])
root.order.add_edge(activities['System Design'], activities['Seed Selection'])
root.order.add_edge(activities['System Design'], activities['Irrigation Setup'])
root.order.add_edge(activities['System Design'], activities['Lighting Install'])
root.order.add_edge(activities['System Design'], activities['Pest Control'])
root.order.add_edge(activities['System Design'], activities['Community Meet'])
root.order.add_edge(activities['System Design'], activities['Regulation Review'])
root.order.add_edge(activities['System Design'], activities['Waste Plan'])
root.order.add_edge(activities['System Design'], activities['Crop Monitor'])
root.order.add_edge(activities['System Design'], activities['Harvest Prep'])
root.order.add_edge(activities['System Design'], activities['Market Launch'])
root.order.add_edge(activities['Seed Selection'], activities['Irrigation Setup'])
root.order.add_edge(activities['Seed Selection'], activities['Lighting Install'])
root.order.add_edge(activities['Seed Selection'], activities['Pest Control'])
root.order.add_edge(activities['Seed Selection'], activities['Community Meet'])
root.order.add_edge(activities['Seed Selection'], activities['Regulation Review'])
root.order.add_edge(activities['Seed Selection'], activities['Waste Plan'])
root.order.add_edge(activities['Seed Selection'], activities['Crop Monitor'])
root.order.add_edge(activities['Seed Selection'], activities['Harvest Prep'])
root.order.add_edge(activities['Seed Selection'], activities['Market Launch'])
root.order.add_edge(activities['Irrigation Setup'], activities['Lighting Install'])
root.order.add_edge(activities['Irrigation Setup'], activities['Pest Control'])
root.order.add_edge(activities['Irrigation Setup'], activities['Community Meet'])
root.order.add_edge(activities['Irrigation Setup'], activities['Regulation Review'])
root.order.add_edge(activities['Irrigation Setup'], activities['Waste Plan'])
root.order.add_edge(activities['Irrigation Setup'], activities['Crop Monitor'])
root.order.add_edge(activities['Irrigation Setup'], activities['Harvest Prep'])
root.order.add_edge(activities['Irrigation Setup'], activities['Market Launch'])
root.order.add_edge(activities['Lighting Install'], activities['Pest Control'])
root.order.add_edge(activities['Lighting Install'], activities['Community Meet'])
root.order.add_edge(activities['Lighting Install'], activities['Regulation Review'])
root.order.add_edge(activities['Lighting Install'], activities['Waste Plan'])
root.order.add_edge(activities['Lighting Install'], activities['Crop Monitor'])
root.order.add_edge(activities['Lighting Install'], activities['Harvest Prep'])
root.order.add_edge(activities['Lighting Install'], activities['Market Launch'])
root.order.add_edge(activities['Pest Control'], activities['Community Meet'])
root.order.add_edge(activities['Pest Control'], activities['Regulation Review'])
root.order.add_edge(activities['Pest Control'], activities['Waste Plan'])
root.order.add_edge(activities['Pest Control'], activities['Crop Monitor'])
root.order.add_edge(activities['Pest Control'], activities['Harvest Prep'])
root.order.add_edge(activities['Pest Control'], activities['Market Launch'])
root.order.add_edge(activities['Community Meet'], activities['Regulation Review'])
root.order.add_edge(activities['Community Meet'], activities['Waste Plan'])
root.order.add_edge(activities['Community Meet'], activities['Crop Monitor'])
root.order.add_edge(activities['Community Meet'], activities['Harvest Prep'])
root.order.add_edge(activities['Community Meet'], activities['Market Launch'])
root.order.add_edge(activities['Regulation Review'], activities['Waste Plan'])
root.order.add_edge(activities['Regulation Review'], activities['Crop Monitor'])
root.order.add_edge(activities['Regulation Review'], activities['Harvest Prep'])
root.order.add_edge(activities['Regulation Review'], activities['Market Launch'])
root.order.add_edge(activities['Waste Plan'], activities['Crop Monitor'])
root.order.add_edge(activities['Waste Plan'], activities['Harvest Prep'])
root.order.add_edge(activities['Waste Plan'], activities['Market Launch'])
root.order.add_edge(activities['Crop Monitor'], activities['Harvest Prep'])
root.order.add_edge(activities['Crop Monitor'], activities['Market Launch'])
root.order.add_edge(activities['Harvest Prep'], activities['Market Launch'])

# Print the root POWL model
print(root)