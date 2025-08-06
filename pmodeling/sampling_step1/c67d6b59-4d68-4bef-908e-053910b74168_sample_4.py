from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Client Meet'),
        Transition(label='Design Draft'),
        Transition(label='Vendor Select'),
        Transition(label='Component Order'),
        Transition(label='Parts Inspect'),
        Transition(label='Frame Build'),
        Transition(label='Wiring Setup'),
        Transition(label='Software Load'),
        Transition(label='Flight Sim'),
        Transition(label='Quality Test'),
        Transition(label='Feedback Review'),
        Transition(label='Adjust Design'),
        Transition(label='Compliance Check'),
        Transition(label='Packaging Prep'),
        Transition(label='Final Demo'),
        Transition(label='Ship Drone')
    ],
    order=[
        # Define the order of activities
        ('Client Meet', 'Design Draft'),
        ('Design Draft', 'Vendor Select'),
        ('Vendor Select', 'Component Order'),
        ('Component Order', 'Parts Inspect'),
        ('Parts Inspect', 'Frame Build'),
        ('Frame Build', 'Wiring Setup'),
        ('Wiring Setup', 'Software Load'),
        ('Software Load', 'Flight Sim'),
        ('Flight Sim', 'Quality Test'),
        ('Quality Test', 'Feedback Review'),
        ('Feedback Review', 'Adjust Design'),
        ('Adjust Design', 'Compliance Check'),
        ('Compliance Check', 'Packaging Prep'),
        ('Packaging Prep', 'Final Demo'),
        ('Final Demo', 'Ship Drone')
    ]
)

print(root)