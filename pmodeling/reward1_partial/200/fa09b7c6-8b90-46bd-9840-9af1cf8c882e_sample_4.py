root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Install Lighting'),
    Transition(label='Setup Hydroponics'),
    Transition(label='Calibrate Sensors'),
    Transition(label='Select Crops'),
    Transition(label='Mix Nutrients'),
    Transition(label='Deploy IoT'),
    Transition(label='Energy Audit'),
    Transition(label='Train Staff'),
    Transition(label='Pest Control'),
    Transition(label='Legal Review'),
    Transition(label='Market Analysis'),
    Transition(label='Plan Logistics'),
    Transition(label='Yield Review')
])

# Define the dependencies between activities
root.order.add_edge('Site Survey', 'Design Layout')
root.order.add_edge('Design Layout', 'Install Lighting')
root.order.add_edge('Install Lighting', 'Setup Hydroponics')
root.order.add_edge('Setup Hydroponics', 'Calibrate Sensors')
root.order.add_edge('Calibrate Sensors', 'Select Crops')
root.order.add_edge('Select Crops', 'Mix Nutrients')
root.order.add_edge('Mix Nutrients', 'Deploy IoT')
root.order.add_edge('Deploy IoT', 'Energy Audit')
root.order.add_edge('Energy Audit', 'Train Staff')
root.order.add_edge('Train Staff', 'Pest Control')
root.order.add_edge('Pest Control', 'Legal Review')
root.order.add_edge('Legal Review', 'Market Analysis')
root.order.add_edge('Market Analysis', 'Plan Logistics')
root.order.add_edge('Plan Logistics', 'Yield Review')