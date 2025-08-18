from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
Assess_Artifact = Transition(label='Assess Artifact')
Verify_Provenance = Transition(label='Verify Provenance')
Analyze_Condition = Transition(label='Analyze Condition')
Plan_Conservation = Transition(label='Plan Conservation')
Clean_Surface = Transition(label='Clean Surface')
Stabilize_Structure = Transition(label='Stabilize Structure')
Source_Materials = Transition(label='Source Materials')
Fabricate_Parts = Transition(label='Fabricate Parts')
Perform_Repairs = Transition(label='Perform Repairs')
Apply_Patina = Transition(label='Apply Patina')
Match_Colors = Transition(label='Match Colors')
Document_Process = Transition(label='Document Process')
Review_Quality = Transition(label='Review Quality')
Obtain_Approval = Transition(label='Obtain Approval')
Package_Securely = Transition(label='Package Securely')
Arrange_Transport = Transition(label='Arrange Transport')

# Create the POWL model
root = StrictPartialOrder(
    nodes=[
        Assess_Artifact, 
        Verify_Provenance, 
        Analyze_Condition, 
        Plan_Conservation, 
        Clean_Surface, 
        Stabilize_Structure, 
        Source_Materials, 
        Fabricate_Parts, 
        Perform_Repairs, 
        Apply_Patina, 
        Match_Colors, 
        Document_Process, 
        Review_Quality, 
        Obtain_Approval, 
        Package_Securely, 
        Arrange_Transport
    ],
    order={
        Assess_Artifact: [Verify_Provenance],
        Verify_Provenance: [Analyze_Condition],
        Analyze_Condition: [Plan_Conservation],
        Plan_Conservation: [Clean_Surface, Stabilize_Structure],
        Clean_Surface: [Stabilize_Structure],
        Stabilize_Structure: [Source_Materials],
        Source_Materials: [Fabricate_Parts],
        Fabricate_Parts: [Perform_Repairs],
        Perform_Repairs: [Apply_Patina],
        Apply_Patina: [Match_Colors],
        Match_Colors: [Document_Process],
        Document_Process: [Review_Quality],
        Review_Quality: [Obtain_Approval],
        Obtain_Approval: [Package_Securely],
        Package_Securely: [Arrange_Transport]
    }
)