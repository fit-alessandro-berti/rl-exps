import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
ApproveReport = Transition(label='Approve report')
ArchiveReport = Transition(label='Archive report')
CheckRegulatoryUpdates = Transition(label='Check regulatory updates')
CloseAuditProcess = Transition(label='Close audit process')
CompileAuditReport = Transition(label='Compile audit report')
CompleteRiskAssessmentMitigation = Transition(label='Complete risk assessment/mitigation')
ConductDataAnalysis = Transition(label='Conduct data analysis')
ConductInterviews = Transition(label='Conduct interviews')
DistributeFinalReport = Transition(label='Distribute final report')
EvaluateComplianceRisks = Transition(label='Evaluate compliance risks')
EvaluateFinancialRisks = Transition(label='Evaluate financial risks')
EvaluateOperationalRisks = Transition(label='Evaluate operational risks')
GatherNecessaryDocuments = Transition(label='Gather necessary documents')
LaunchDetailedInvestigation = Transition(label='Launch detailed investigation')
PerformSiteVisits = Transition(label='Perform site visits')
PrepareFinancialStatements = Transition(label='Prepare financial statements')
ReceiveClarifications = Transition(label='Receive clarifications')
RequestClarificationsOfDiscrepancies = Transition(label='Request clarifications of discrepancies')
ReviewReportByAuditDirector = Transition(label='Review report by audit director')
ReviewSubmission = Transition(label='Review submission')
SendNotification = Transition(label='Send notification')
SendReportForRevision = Transition(label='Send report for revision')
SubmitDocuments = Transition(label='Submit documents')
UpdateAndResubmitReport = Transition(label='Update and resubmit report')

# Define the partial order
root = StrictPartialOrder(nodes=[
    ApproveReport, ArchiveReport, CheckRegulatoryUpdates, CloseAuditProcess, 
    CompileAuditReport, CompleteRiskAssessmentMitigation, ConductDataAnalysis, 
    ConductInterviews, DistributeFinalReport, EvaluateComplianceRisks, 
    EvaluateFinancialRisks, EvaluateOperationalRisks, GatherNecessaryDocuments, 
    LaunchDetailedInvestigation, PerformSiteVisits, PrepareFinancialStatements, 
    ReceiveClarifications, RequestClarificationsOfDiscrepancies, ReviewReportByAuditDirector, 
    ReviewSubmission, SendNotification, SendReportForRevision, SubmitDocuments, 
    UpdateAndResubmitReport])

# Define the dependencies between the nodes
root.order.add_edge(SendNotification, GatherNecessaryDocuments)
root.order.add_edge(GatherNecessaryDocuments, PrepareFinancialStatements)
root.order.add_edge(PrepareFinancialStatements, CheckRegulatoryUpdates)
root.order.add_edge(CheckRegulatoryUpdates, SubmitDocuments)
root.order.add_edge(SubmitDocuments, ReviewSubmission)
root.order.add_edge(ReviewSubmission, LaunchDetailedInvestigation)
root.order.add_edge(LaunchDetailedInvestigation, ConductDataAnalysis)
root.order.add_edge(ConductDataAnalysis, ConductInterviews)
root.order.add_edge(ConductInterviews, CompleteRiskAssessmentMitigation)
root.order.add_edge(CompleteRiskAssessmentMitigation, EvaluateFinancialRisks)
root.order.add_edge(EvaluateFinancialRisks, EvaluateOperationalRisks)
root.order.add_edge(EvaluateOperationalRisks, EvaluateComplianceRisks)
root.order.add_edge(EvaluateComplianceRisks, CompleteRiskAssessmentMitigation)
root.order.add_edge(CompleteRiskAssessmentMitigation, RequestClarificationsOfDiscrepancies)
root.order.add_edge(RequestClarificationsOfDiscrepancies, ReceiveClarifications)
root.order.add_edge(ReceiveClarifications, LaunchDetailedInvestigation)
root.order.add_edge(LaunchDetailedInvestigation, PerformSiteVisits)
root.order.add_edge(PerformSiteVisits, CompleteRiskAssessmentMitigation)
root.order.add_edge(CompleteRiskAssessmentMitigation, CompileAuditReport)
root.order.add_edge(CompileAuditReport, ReviewReportByAuditDirector)
root.order.add_edge(ReviewReportByAuditDirector, ApproveReport)
root.order.add_edge(ApproveReport, DistributeFinalReport)
root.order.add_edge(DistributeFinalReport, ArchiveReport)
root.order.add_edge(UpdateAndResubmitReport, SendReportForRevision)
root.order.add_edge(SendReportForRevision, ReviewSubmission)
root.order.add_edge(ReviewSubmission, SubmitDocuments)
root.order.add_edge(SubmitDocuments, ReviewReportByAuditDirector)
root.order.add_edge(ReviewReportByAuditDirector, ApproveReport)
root.order.add_edge(ApproveReport, DistributeFinalReport)
root.order.add_edge(DistributeFinalReport, ArchiveReport)
root.order.add_edge(CloseAuditProcess, ArchiveReport)

# Print the root POWL model
print(root)