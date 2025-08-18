import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Acquisition', 'Impact Assess', 'Modular Setup', 'Crop Planting', 'Nutrient Control', 'Pest Control', 'Growth Monitor', 'Community Engage', 'Yield Forecast', 'Supply Coordinate', 'Compliance Check', 'Waste Recycle', 'Energy Optimize', 'Market Strategy', 'Performance Review']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Create the process tree structure
root = StrictPartialOrder(nodes=[
    transitions['Site Acquisition'],
    OperatorPOWL(operator=Operator.XOR, children=[
        OperatorPOWL(operator=Operator.XOR, children=[
            transitions['Impact Assess'],
            transitions['Modular Setup']
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            transitions['Crop Planting'],
            OperatorPOWL(operator=Operator.LOOP, children=[
                OperatorPOWL(operator=Operator.XOR, children=[
                    transitions['Nutrient Control'],
                    transitions['Pest Control']
                ])
            ])
        ])
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        OperatorPOWL(operator=Operator.XOR, children=[
            transitions['Growth Monitor'],
            transitions['Community Engage']
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            transitions['Yield Forecast'],
            transitions['Supply Coordinate']
        ])
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        transitions['Compliance Check'],
        OperatorPOWL(operator=Operator.LOOP, children=[
            OperatorPOWL(operator=Operator.XOR, children=[
                transitions['Waste Recycle'],
                transitions['Energy Optimize']
            ])
        ])
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        transitions['Market Strategy'],
        transitions['Performance Review']
    ])
])

# Add edges to the partial order
root.order.add_edge(transitions['Site Acquisition'], transitions['Impact Assess'])
root.order.add_edge(transitions['Site Acquisition'], transitions['Modular Setup'])
root.order.add_edge(transitions['Impact Assess'], transitions['Crop Planting'])
root.order.add_edge(transitions['Modular Setup'], transitions['Crop Planting'])
root.order.add_edge(transitions['Crop Planting'], transitions['Nutrient Control'])
root.order.add_edge(transitions['Crop Planting'], transitions['Pest Control'])
root.order.add_edge(transitions['Nutrient Control'], transitions['Growth Monitor'])
root.order.add_edge(transitions['Pest Control'], transitions['Growth Monitor'])
root.order.add_edge(transitions['Growth Monitor'], transitions['Community Engage'])
root.order.add_edge(transitions['Growth Monitor'], transitions['Yield Forecast'])
root.order.add_edge(transitions['Community Engage'], transitions['Yield Forecast'])
root.order.add_edge(transitions['Yield Forecast'], transitions['Supply Coordinate'])
root.order.add_edge(transitions['Yield Forecast'], transitions['Compliance Check'])
root.order.add_edge(transitions['Supply Coordinate'], transitions['Compliance Check'])
root.order.add_edge(transitions['Compliance Check'], transitions['Waste Recycle'])
root.order.add_edge(transitions['Compliance Check'], transitions['Energy Optimize'])
root.order.add_edge(transitions['Waste Recycle'], transitions['Market Strategy'])
root.order.add_edge(transitions['Energy Optimize'], transitions['Market Strategy'])
root.order.add_edge(transitions['Market Strategy'], transitions['Performance Review'])
root.order.add_edge(transitions['Performance Review'], transitions['Performance Review'])

# The final result is saved in the variable 'root'