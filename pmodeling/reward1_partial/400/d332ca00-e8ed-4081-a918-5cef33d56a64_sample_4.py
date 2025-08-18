import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
root = StrictPartialOrder(
    nodes=[
        Transition(label='Intake Document'),
        Transition(label='Visual Inspect'),
        Transition(label='Imaging Scan'),
        Transition(label='Material Test'),
        Transition(label='Database Cross'),
        Transition(label='Provenance Check'),
        Transition(label='Expert Consult'),
        Transition(label='Carbon Dating'),
        Transition(label='Forensic Analyze'),
        Transition(label='Anomaly Review'),
        Transition(label='Risk Assess'),
        Transition(label='Report Draft'),
        Transition(label='Insurance Quote'),
        Transition(label='Storage Plan'),
        Transition(label='Final Approval')
    ],
    order=[
        ('Intake Document', 'Visual Inspect'),
        ('Visual Inspect', 'Imaging Scan'),
        ('Imaging Scan', 'Material Test'),
        ('Material Test', 'Database Cross'),
        ('Database Cross', 'Provenance Check'),
        ('Provenance Check', 'Expert Consult'),
        ('Expert Consult', 'Carbon Dating'),
        ('Carbon Dating', 'Forensic Analyze'),
        ('Forensic Analyze', 'Anomaly Review'),
        ('Anomaly Review', 'Risk Assess'),
        ('Risk Assess', 'Report Draft'),
        ('Report Draft', 'Insurance Quote'),
        ('Insurance Quote', 'Storage Plan'),
        ('Storage Plan', 'Final Approval')
    ]
)

print(root)