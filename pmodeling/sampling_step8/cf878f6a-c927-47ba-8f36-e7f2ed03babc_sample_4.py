from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Assess': Transition(label='Site Assess'),
    'Zoning Check': Transition(label='Zoning Check'),
    'Design Farm': Transition(label='Design Farm'),
    'Procure Gear': Transition(label='Procure Gear'),
    'Install Systems': Transition(label='Install Systems'),
    'Setup Sensors': Transition(label='Setup Sensors'),
    'Select Crops': Transition(label='Select Crops'),
    'Prepare Seeds': Transition(label='Prepare Seeds'),
    'Mix Nutrients': Transition(label='Mix Nutrients'),
    'Monitor Growth': Transition(label='Monitor Growth'),
    'Adjust Climate': Transition(label='Adjust Climate'),
    'Robotic Harvest': Transition(label='Robotic Harvest'),
    'Grade Quality': Transition(label='Grade Quality'),
    'Pack Produce': Transition(label='Pack Produce'),
    'Manage Logistics': Transition(label='Manage Logistics'),
    'Market Products': Transition(label='Market Products'),
    'Recycle Waste': Transition(label='Recycle Waste'),
    'Audit Systems': Transition(label='Audit Systems')
}

# Define the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies (partial order)
root.order.add_edge(activities['Site Assess'], activities['Zoning Check'])
root.order.add_edge(activities['Zoning Check'], activities['Design Farm'])
root.order.add_edge(activities['Design Farm'], activities['Procure Gear'])
root.order.add_edge(activities['Procure Gear'], activities['Install Systems'])
root.order.add_edge(activities['Install Systems'], activities['Setup Sensors'])
root.order.add_edge(activities['Setup Sensors'], activities['Select Crops'])
root.order.add_edge(activities['Select Crops'], activities['Prepare Seeds'])
root.order.add_edge(activities['Prepare Seeds'], activities['Mix Nutrients'])
root.order.add_edge(activities['Mix Nutrients'], activities['Monitor Growth'])
root.order.add_edge(activities['Monitor Growth'], activities['Adjust Climate'])
root.order.add_edge(activities['Adjust Climate'], activities['Robotic Harvest'])
root.order.add_edge(activities['Robotic Harvest'], activities['Grade Quality'])
root.order.add_edge(activities['Grade Quality'], activities['Pack Produce'])
root.order.add_edge(activities['Pack Produce'], activities['Manage Logistics'])
root.order.add_edge(activities['Manage Logistics'], activities['Market Products'])
root.order.add_edge(activities['Market Products'], activities['Recycle Waste'])
root.order.add_edge(activities['Recycle Waste'], activities['Audit Systems'])

print(root)