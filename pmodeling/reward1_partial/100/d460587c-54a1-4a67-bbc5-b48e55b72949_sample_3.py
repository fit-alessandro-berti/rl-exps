root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Permit Filing'),
    Transition(label='Load Testing'),
    Transition(label='Soil Sampling'),
    Transition(label='Water Testing'),
    Transition(label='System Design'),
    Transition(label='Solar Setup'),
    Transition(label='Crop Planning'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Material Order'),
    Transition(label='System Install'),
    Transition(label='Environmental Audit'),
    Transition(label='Growth Monitoring'),
    Transition(label='Pest Control'),
    Transition(label='Market Launch')
])

# Define the order of the activities
root.order.add_edge('Site Survey', 'Permit Filing')
root.order.add_edge('Permit Filing', 'Load Testing')
root.order.add_edge('Load Testing', 'Soil Sampling')
root.order.add_edge('Soil Sampling', 'Water Testing')
root.order.add_edge('Water Testing', 'System Design')
root.order.add_edge('System Design', 'Solar Setup')
root.order.add_edge('Solar Setup', 'Crop Planning')
root.order.add_edge('Crop Planning', 'Stakeholder Meet')
root.order.add_edge('Stakeholder Meet', 'Material Order')
root.order.add_edge('Material Order', 'System Install')
root.order.add_edge('System Install', 'Environmental Audit')
root.order.add_edge('Environmental Audit', 'Growth Monitoring')
root.order.add_edge('Growth Monitoring', 'Pest Control')
root.order.add_edge('Pest Control', 'Market Launch')