from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Permit Filing'),
        Transition(label='Structure Prep'),
        Transition(label='System Install'),
        Transition(label='Nutrient Mix'),
        Transition(label='Sensor Setup'),
        Transition(label='AI Calibration'),
        Transition(label='Seed Sourcing'),
        Transition(label='Staff Training'),
        Transition(label='Energy Connect'),
        Transition(label='Water Cycle'),
        Transition(label='Growth Monitor'),
        Transition(label='Waste Audit'),
        Transition(label='Community Meet'),
        Transition(label='Data Review'),
        Transition(label='Yield Forecast')
    ],
    order={
        ('Site Survey', 'Permit Filing'): None,
        ('Permit Filing', 'Structure Prep'): None,
        ('Structure Prep', 'System Install'): None,
        ('System Install', 'Nutrient Mix'): None,
        ('Nutrient Mix', 'Sensor Setup'): None,
        ('Sensor Setup', 'AI Calibration'): None,
        ('AI Calibration', 'Seed Sourcing'): None,
        ('Seed Sourcing', 'Staff Training'): None,
        ('Staff Training', 'Energy Connect'): None,
        ('Energy Connect', 'Water Cycle'): None,
        ('Water Cycle', 'Growth Monitor'): None,
        ('Growth Monitor', 'Waste Audit'): None,
        ('Waste Audit', 'Community Meet'): None,
        ('Community Meet', 'Data Review'): None,
        ('Data Review', 'Yield Forecast'): None
    }
)

# Add dependencies between nodes
root.order.add_edge('Site Survey', 'Permit Filing')
root.order.add_edge('Permit Filing', 'Structure Prep')
root.order.add_edge('Structure Prep', 'System Install')
root.order.add_edge('System Install', 'Nutrient Mix')
root.order.add_edge('Nutrient Mix', 'Sensor Setup')
root.order.add_edge('Sensor Setup', 'AI Calibration')
root.order.add_edge('AI Calibration', 'Seed Sourcing')
root.order.add_edge('Seed Sourcing', 'Staff Training')
root.order.add_edge('Staff Training', 'Energy Connect')
root.order.add_edge('Energy Connect', 'Water Cycle')
root.order.add_edge('Water Cycle', 'Growth Monitor')
root.order.add_edge('Growth Monitor', 'Waste Audit')
root.order.add_edge('Waste Audit', 'Community Meet')
root.order.add_edge('Community Meet', 'Data Review')
root.order.add_edge('Data Review', 'Yield Forecast')

print(root)