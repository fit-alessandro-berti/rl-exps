from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Seed Select': Transition(label='Seed Select'),
    'Germinate Seeds': Transition(label='Germinate Seeds'),
    'Transplant Seedlings': Transition(label='Transplant Seedlings'),
    'Mix Nutrients': Transition(label='Mix Nutrients'),
    'Adjust pH': Transition(label='Adjust pH'),
    'Monitor Climate': Transition(label='Monitor Climate'),
    'Control Humidity': Transition(label='Control Humidity'),
    'CO2 Regulation': Transition(label='CO2 Regulation'),
    'Detect Pests': Transition(label='Detect Pests'),
    'Deploy Biocontrols': Transition(label='Deploy Biocontrols'),
    'Schedule Harvest': Transition(label='Schedule Harvest'),
    'Automate Picking': Transition(label='Automate Picking'),
    'Package Produce': Transition(label='Package Produce'),
    'Compost Waste': Transition(label='Compost Waste'),
    'Recycle Water': Transition(label='Recycle Water'),
    'Data Logging': Transition(label='Data Logging'),
    'System Maintenance': Transition(label='System Maintenance')
}

# Define the partial order model
root = StrictPartialOrder(nodes=[
    activities['Seed Select'],
    activities['Germinate Seeds'],
    activities['Transplant Seedlings'],
    activities['Mix Nutrients'],
    activities['Adjust pH'],
    activities['Monitor Climate'],
    activities['Control Humidity'],
    activities['CO2 Regulation'],
    activities['Detect Pests'],
    activities['Deploy Biocontrols'],
    activities['Schedule Harvest'],
    activities['Automate Picking'],
    activities['Package Produce'],
    activities['Compost Waste'],
    activities['Recycle Water'],
    activities['Data Logging'],
    activities['System Maintenance']
])

# Define the dependencies between activities
root.order.add_edge(activities['Seed Select'], activities['Germinate Seeds'])
root.order.add_edge(activities['Germinate Seeds'], activities['Transplant Seedlings'])
root.order.add_edge(activities['Transplant Seedlings'], activities['Mix Nutrients'])
root.order.add_edge(activities['Mix Nutrients'], activities['Adjust pH'])
root.order.add_edge(activities['Adjust pH'], activities['Monitor Climate'])
root.order.add_edge(activities['Monitor Climate'], activities['Control Humidity'])
root.order.add_edge(activities['Control Humidity'], activities['CO2 Regulation'])
root.order.add_edge(activities['CO2 Regulation'], activities['Detect Pests'])
root.order.add_edge(activities['Detect Pests'], activities['Deploy Biocontrols'])
root.order.add_edge(activities['Deploy Biocontrols'], activities['Schedule Harvest'])
root.order.add_edge(activities['Schedule Harvest'], activities['Automate Picking'])
root.order.add_edge(activities['Automate Picking'], activities['Package Produce'])
root.order.add_edge(activities['Package Produce'], activities['Compost Waste'])
root.order.add_edge(activities['Compost Waste'], activities['Recycle Water'])
root.order.add_edge(activities['Recycle Water'], activities['Data Logging'])
root.order.add_edge(activities['Data Logging'], activities['System Maintenance'])

print(root)