import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
AuditArtifacts = Transition(label='Audit Artifacts')
InterviewStaff = Transition(label='Interview Staff')
AssessRisks = Transition(label='Assess Risks')
PlanRetrieval = Transition(label='Plan Retrieval')
LegalReview = Transition(label='Legal Review')
SecurityCheck = Transition(label='Security Check')
ExecuteRecovery = Transition(label='Execute Recovery')
ValidateItems = Transition(label='Validate Items')
RestoreFunction = Transition(label='Restore Function')
UpdateSystems = Transition(label='Update Systems')
TrainUsers = Transition(label='Train Users')
DocumentFindings = Transition(label='Document Findings')
ArchiveRecords = Transition(label='Archive Records')
ReviewLessons = Transition(label='Review Lessons')
CloseProcess = Transition(label='Close Process')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    AuditArtifacts, InterviewStaff, AssessRisks, PlanRetrieval,
    LegalReview, SecurityCheck, ExecuteRecovery, ValidateItems,
    RestoreFunction, UpdateSystems, TrainUsers, DocumentFindings,
    ArchiveRecords, ReviewLessons, CloseProcess
])

# Define the partial order dependencies
root.order.add_edge(AuditArtifacts, InterviewStaff)
root.order.add_edge(InterviewStaff, AssessRisks)
root.order.add_edge(AssessRisks, PlanRetrieval)
root.order.add_edge(PlanRetrieval, LegalReview)
root.order.add_edge(LegalReview, SecurityCheck)
root.order.add_edge(SecurityCheck, ExecuteRecovery)
root.order.add_edge(ExecuteRecovery, ValidateItems)
root.order.add_edge(ValidateItems, RestoreFunction)
root.order.add_edge(RestoreFunction, UpdateSystems)
root.order.add_edge(UpdateSystems, TrainUsers)
root.order.add_edge(TrainUsers, DocumentFindings)
root.order.add_edge(DocumentFindings, ArchiveRecords)
root.order.add_edge(ArchiveRecords, ReviewLessons)
root.order.add_edge(ReviewLessons, CloseProcess)

# Print the final POWL model
print(root)