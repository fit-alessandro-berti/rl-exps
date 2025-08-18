from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Permit Filing': Transition(label='Permit Filing'),
    'Structure Prep': Transition(label='Structure Prep'),
    'System Install': Transition(label='System Install'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Sensor Setup': Transition(label='Sensor Setup'),
    'AI Calibration': Transition(label='AI Calibration'),
    'Seed Sourcing': Transition(label='Seed Sourcing'),
    'Staff Training': Transition(label='Staff Training'),
    'Energy Connect': Transition(label='Energy Connect'),
    'Water Cycle': Transition(label='Water Cycle'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Waste Audit': Transition(label='Waste Audit'),
    'Community Meet': Transition(label='Community Meet'),
    'Data Review': Transition(label='Data Review'),
    'Yield Forecast': Transition(label='Yield Forecast')
}

# Define the partial order
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Permit Filing'],
    activities['Structure Prep'],
    activities['System Install'],
    activities['Nutrient Mix'],
    activities['Sensor Setup'],
    activities['AI Calibration'],
    activities['Seed Sourcing'],
    activities['Staff Training'],
    activities['Energy Connect'],
    activities['Water Cycle'],
    activities['Growth Monitor'],
    activities['Waste Audit'],
    activities['Community Meet'],
    activities['Data Review'],
    activities['Yield Forecast']
])

# Define the dependencies
root.order.add_edge(activities['Site Survey'], activities['Permit Filing'])
root.order.add_edge(activities['Permit Filing'], activities['Structure Prep'])
root.order.add_edge(activities['Structure Prep'], activities['System Install'])
root.order.add_edge(activities['System Install'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Sensor Setup'])
root.order.add_edge(activities['Sensor Setup'], activities['AI Calibration'])
root.order.add_edge(activities['AI Calibration'], activities['Seed Sourcing'])
root.order.add_edge(activities['Seed Sourcing'], activities['Staff Training'])
root.order.add_edge(activities['Staff Training'], activities['Energy Connect'])
root.order.add_edge(activities['Energy Connect'], activities['Water Cycle'])
root.order.add_edge(activities['Water Cycle'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Waste Audit'])
root.order.add_edge(activities['Waste Audit'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Data Review'])
root.order.add_edge(activities['Data Review'], activities['Yield Forecast'])

print(root)