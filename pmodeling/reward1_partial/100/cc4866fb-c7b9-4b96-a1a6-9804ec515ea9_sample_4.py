import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Planning': Transition(label='Design Planning'),
    'Permit Filing': Transition(label='Permit Filing'),
    'Structural Reinforce': Transition(label='Structural Reinforce'),
    'Hydroponic Setup': Transition(label='Hydroponic Setup'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Crop Selection': Transition(label='Crop Selection'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Waste Process': Transition(label='Waste Process'),
    'Climate Control': Transition(label='Climate Control'),
    'Staff Training': Transition(label='Staff Training'),
    'Market Study': Transition(label='Market Study'),
    'Community Meet': Transition(label='Community Meet'),
    'Launch Trial': Transition(label='Launch Trial'),
    'Data Monitor': Transition(label='Data Monitor')
}

# Define the POWL model
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Design Planning'],
    activities['Permit Filing'],
    activities['Structural Reinforce'],
    activities['Hydroponic Setup'],
    activities['Sensor Install'],
    activities['Energy Audit'],
    activities['Crop Selection'],
    activities['Nutrient Mix'],
    activities['Waste Process'],
    activities['Climate Control'],
    activities['Staff Training'],
    activities['Market Study'],
    activities['Community Meet'],
    activities['Launch Trial'],
    activities['Data Monitor']
])

# Define the order of execution
root.order.add_edge(activities['Site Survey'], activities['Design Planning'])
root.order.add_edge(activities['Design Planning'], activities['Permit Filing'])
root.order.add_edge(activities['Permit Filing'], activities['Structural Reinforce'])
root.order.add_edge(activities['Structural Reinforce'], activities['Hydroponic Setup'])
root.order.add_edge(activities['Hydroponic Setup'], activities['Sensor Install'])
root.order.add_edge(activities['Sensor Install'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Crop Selection'])
root.order.add_edge(activities['Crop Selection'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Waste Process'])
root.order.add_edge(activities['Waste Process'], activities['Climate Control'])
root.order.add_edge(activities['Climate Control'], activities['Staff Training'])
root.order.add_edge(activities['Staff Training'], activities['Market Study'])
root.order.add_edge(activities['Market Study'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Launch Trial'])
root.order.add_edge(activities['Launch Trial'], activities['Data Monitor'])

# Print the root
print(root)