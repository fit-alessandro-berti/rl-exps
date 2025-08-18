root = StrictPartialOrder(nodes=[
    Transition(label='Site Assess'),
    Transition(label='Zoning Check'),
    Transition(label='Design Farm'),
    Transition(label='Procure Gear'),
    Transition(label='Install Systems'),
    Transition(label='Setup Sensors'),
    Transition(label='Select Crops'),
    Transition(label='Prepare Seeds'),
    Transition(label='Mix Nutrients'),
    Transition(label='Monitor Growth'),
    Transition(label='Adjust Climate'),
    Transition(label='Robotic Harvest'),
    Transition(label='Grade Quality'),
    Transition(label='Pack Produce'),
    Transition(label='Manage Logistics'),
    Transition(label='Market Products'),
    Transition(label='Recycle Waste'),
    Transition(label='Audit Systems')
])

# Define the relationships between activities
root.order.add_edge('Site Assess', 'Zoning Check')
root.order.add_edge('Zoning Check', 'Design Farm')
root.order.add_edge('Design Farm', 'Procure Gear')
root.order.add_edge('Procure Gear', 'Install Systems')
root.order.add_edge('Install Systems', 'Setup Sensors')
root.order.add_edge('Setup Sensors', 'Select Crops')
root.order.add_edge('Select Crops', 'Prepare Seeds')
root.order.add_edge('Prepare Seeds', 'Mix Nutrients')
root.order.add_edge('Mix Nutrients', 'Monitor Growth')
root.order.add_edge('Monitor Growth', 'Adjust Climate')
root.order.add_edge('Adjust Climate', 'Robotic Harvest')
root.order.add_edge('Robotic Harvest', 'Grade Quality')
root.order.add_edge('Grade Quality', 'Pack Produce')
root.order.add_edge('Pack Produce', 'Manage Logistics')
root.order.add_edge('Manage Logistics', 'Market Products')
root.order.add_edge('Market Products', 'Recycle Waste')
root.order.add_edge('Recycle Waste', 'Audit Systems')