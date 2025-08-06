import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.process_tree.obj import ProcessTree

# Define activities
activities = {
    'Source Materials': Transition(label='Source Materials'),
    'Vet Suppliers': Transition(label='Vet Suppliers'),
    'Design Modules': Transition(label='Design Modules'),
    'Prototype Build': Transition(label='Prototype Build'),
    'Test Durability': Transition(label='Test Durability'),
    'Secure Permits': Transition(label='Secure Permits'),
    'Map Habitats': Transition(label='Map Habitats'),
    'Micro Warehouse': Transition(label='Micro Warehouse'),
    'Inventory Sync': Transition(label='Inventory Sync'),
    'Pack Sustainably': Transition(label='Pack Sustainably'),
    'Route Optimize': Transition(label='Route Optimize'),
    'Engage Community': Transition(label='Engage Community'),
    'Collect Feedback': Transition(label='Collect Feedback'),
    'Adjust Production': Transition(label='Adjust Production'),
    'Partner NGOs': Transition(label='Partner NGOs'),
    'Launch Campaign': Transition(label='Launch Campaign'),
    'Monitor Sensors': Transition(label='Monitor Sensors'),
    'Report Impact': Transition(label='Report Impact')
}

# Define transitions
transitions = {
    'Source Materials': OperatorPOWL(operator=Operator.LOOP, children=[activities['Source Materials']]),
    'Vet Suppliers': OperatorPOWL(operator=Operator.LOOP, children=[activities['Vet Suppliers']]),
    'Design Modules': OperatorPOWL(operator=Operator.LOOP, children=[activities['Design Modules']]),
    'Prototype Build': OperatorPOWL(operator=Operator.LOOP, children=[activities['Prototype Build']]),
    'Test Durability': OperatorPOWL(operator=Operator.LOOP, children=[activities['Test Durability']]),
    'Secure Permits': OperatorPOWL(operator=Operator.LOOP, children=[activities['Secure Permits']]),
    'Map Habitats': OperatorPOWL(operator=Operator.LOOP, children=[activities['Map Habitats']]),
    'Micro Warehouse': OperatorPOWL(operator=Operator.LOOP, children=[activities['Micro Warehouse']]),
    'Inventory Sync': OperatorPOWL(operator=Operator.LOOP, children=[activities['Inventory Sync']]),
    'Pack Sustainably': OperatorPOWL(operator=Operator.LOOP, children=[activities['Pack Sustainably']]),
    'Route Optimize': OperatorPOWL(operator=Operator.LOOP, children=[activities['Route Optimize']]),
    'Engage Community': OperatorPOWL(operator=Operator.LOOP, children=[activities['Engage Community']]),
    'Collect Feedback': OperatorPOWL(operator=Operator.LOOP, children=[activities['Collect Feedback']]),
    'Adjust Production': OperatorPOWL(operator=Operator.LOOP, children=[activities['Adjust Production']]),
    'Partner NGOs': OperatorPOWL(operator=Operator.LOOP, children=[activities['Partner NGOs']]),
    'Launch Campaign': OperatorPOWL(operator=Operator.LOOP, children=[activities['Launch Campaign']]),
    'Monitor Sensors': OperatorPOWL(operator=Operator.LOOP, children=[activities['Monitor Sensors']]),
    'Report Impact': OperatorPOWL(operator=Operator.LOOP, children=[activities['Report Impact']])
}

# Define root POWL
root = StrictPartialOrder(nodes=list(transitions.values()))

# Define order
root.order.add_edge(transitions['Source Materials'], transitions['Vet Suppliers'])
root.order.add_edge(transitions['Vet Suppliers'], transitions['Design Modules'])
root.order.add_edge(transitions['Design Modules'], transitions['Prototype Build'])
root.order.add_edge(transitions['Prototype Build'], transitions['Test Durability'])
root.order.add_edge(transitions['Test Durability'], transitions['Secure Permits'])
root.order.add_edge(transitions['Secure Permits'], transitions['Map Habitats'])
root.order.add_edge(transitions['Map Habitats'], transitions['Micro Warehouse'])
root.order.add_edge(transitions['Micro Warehouse'], transitions['Inventory Sync'])
root.order.add_edge(transitions['Inventory Sync'], transitions['Pack Sustainably'])
root.order.add_edge(transitions['Pack Sustainably'], transitions['Route Optimize'])
root.order.add_edge(transitions['Route Optimize'], transitions['Engage Community'])
root.order.add_edge(transitions['Engage Community'], transitions['Collect Feedback'])
root.order.add_edge(transitions['Collect Feedback'], transitions['Adjust Production'])
root.order.add_edge(transitions['Adjust Production'], transitions['Partner NGOs'])
root.order.add_edge(transitions['Partner NGOs'], transitions['Launch Campaign'])
root.order.add_edge(transitions['Launch Campaign'], transitions['Monitor Sensors'])
root.order.add_edge(transitions['Monitor Sensors'], transitions['Report Impact'])

# Print root
print(root)