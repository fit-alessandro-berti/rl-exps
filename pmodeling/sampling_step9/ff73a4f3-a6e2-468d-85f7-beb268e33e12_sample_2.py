import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transition
skip = SilentTransition()

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[AuditArtifacts, InterviewStaff, AssessRisks, PlanRetrieval, LegalReview, SecurityCheck, ExecuteRecovery, ValidateItems, RestoreFunction])

# Define the XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[UpdateSystems, TrainUsers, DocumentFindings, ArchiveRecords, ReviewLessons, CloseProcess])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)