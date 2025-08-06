import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
root = StrictPartialOrder(
    nodes=[
        Transition(label='Trend Scan'),
        Transition(label='Idea Sprint'),
        Transition(label='Feasibility Check'),
        Transition(label='Risk Review'),
        Transition(label='Tech Prototype'),
        Transition(label='Market Simulate'),
        Transition(label='Stakeholder Align'),
        Transition(label='Budget Adjust'),
        Transition(label='Talent Source'),
        Transition(label='Pilot Launch'),
        Transition(label='Data Refine'),
        Transition(label='Scale Analysis'),
        Transition(label='Integration Plan'),
        Transition(label='Change Manage'),
        Transition(label='Knowledge Transfer'),
    ],
    order=[
        # Define the dependencies between activities
        ('Trend Scan', 'Idea Sprint'),
        ('Idea Sprint', 'Feasibility Check'),
        ('Feasibility Check', 'Risk Review'),
        ('Risk Review', 'Tech Prototype'),
        ('Tech Prototype', 'Market Simulate'),
        ('Market Simulate', 'Stakeholder Align'),
        ('Stakeholder Align', 'Budget Adjust'),
        ('Budget Adjust', 'Talent Source'),
        ('Talent Source', 'Pilot Launch'),
        ('Pilot Launch', 'Data Refine'),
        ('Data Refine', 'Scale Analysis'),
        ('Scale Analysis', 'Integration Plan'),
        ('Integration Plan', 'Change Manage'),
        ('Change Manage', 'Knowledge Transfer'),
    ]
)

# Print the resulting POWL model
print(root)