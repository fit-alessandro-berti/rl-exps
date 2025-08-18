from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = ['Site Survey', 'Design Draft', 'Permit Review', 'Structure Build', 'Enviro Setup', 'Nutrient Mix', 'Seed Selection', 'Plant Robots', 'Sensor Install', 'Data Sync', 'Growth Monitor', 'Pest Control', 'Harvest Plan', 'Quality Check', 'Market Launch', 'Feedback Loop']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Create a loop node for the Feedback Loop
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[transitions[-1]])

# Create a partial order model
root = StrictPartialOrder(nodes=transitions[:-1] + [feedback_loop])
root.order.add_edge(transitions[-2], feedback_loop)

print(root)