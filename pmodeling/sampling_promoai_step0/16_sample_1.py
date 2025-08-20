from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SendNotification = Transition(label='Send notification')
GatherDocuments = Transition(label='Gather necessary documents')
PrepareStatements = Transition(label='Prepare financial statements')
CheckRegUpdates = Transition(label='Check regulatory updates')
ReviewSubmission = Transition(label='Review submission')
RequestClarifications = Transition(label='Request clarifications of discrepancies')
ReceiveClarifications = Transition(label='Receive clarifications')
CompleteRiskAssessment = Transition(label='Complete risk assessment/mitigation')
EvaluateComplianceRisks = Transition(label='Evaluate compliance risks')
EvaluateFinancialRisks = Transition(label='Evaluate financial risks')
EvaluateOperationalRisks = Transition(label='Evaluate operational risks')
ConductDataAnalysis = Transition(label='Conduct data analysis')
ConductInterviews = Transition(label='Conduct interviews')
PerformSiteVisits = Transition(label='Perform site visits')
LaunchDetailedInvestigation = Transition(label='Launch detailed investigation')
CompileAuditReport = Transition(label='Compile audit report')
ReviewReport = Transition(label='Review report by audit director')
ApproveReport = Transition(label='Approve report')
SendReportForRevision = Transition(label='Send report for revision')
UpdateAndResubmitReport = Transition(label='Update and resubmit report')
SubmitDocuments = Transition(label='Submit documents')
ArchiveReport = Transition(label='Archive report')
CloseAuditProcess = Transition(label='Close audit process')

# Define silent transitions
SkipCheckRegUpdates = SilentTransition()
SkipReviewSubmission = SilentTransition()
SkipRequestClarifications = SilentTransition()
SkipReceiveClarifications = SilentTransition()
SkipCompleteRiskAssessment = SilentTransition()
SkipEvaluateComplianceRisks = SilentTransition()
SkipEvaluateFinancialRisks = SilentTransition()
SkipEvaluateOperationalRisks = SilentTransition()
SkipConductDataAnalysis = SilentTransition()
SkipConductInterviews = SilentTransition()
SkipPerformSiteVisits = SilentTransition()
SkipLaunchDetailedInvestigation = SilentTransition()
SkipCompileAuditReport = SilentTransition()
SkipReviewReport = SilentTransition()
SkipApproveReport = SilentTransition()
SkipSendReportForRevision = SilentTransition()
SkipUpdateAndResubmitReport = SilentTransition()
SkipSubmitDocuments = SilentTransition()
SkipArchiveReport = SilentTransition()
SkipCloseAuditProcess = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(nodes=[
    SendNotification,
    GatherDocuments,
    PrepareStatements,
    CheckRegUpdates,
    ReviewSubmission,
    RequestClarifications,
    ReceiveClarifications,
    CompleteRiskAssessment,
    EvaluateComplianceRisks,
    EvaluateFinancialRisks,
    EvaluateOperationalRisks,
    ConductDataAnalysis,
    ConductInterviews,
    PerformSiteVisits,
    LaunchDetailedInvestigation,
    CompileAuditReport,
    ReviewReport,
    ApproveReport,
    SendReportForRevision,
    UpdateAndResubmitReport,
    SubmitDocuments,
    ArchiveReport,
    CloseAuditProcess,
    SkipCheckRegUpdates,
    SkipReviewSubmission,
    SkipRequestClarifications,
    SkipReceiveClarifications,
    SkipCompleteRiskAssessment,
    SkipEvaluateComplianceRisks,
    SkipEvaluateFinancialRisks,
    SkipEvaluateOperationalRisks,
    SkipConductDataAnalysis,
    SkipConductInterviews,
    SkipPerformSiteVisits,
    SkipLaunchDetailedInvestigation,
    SkipCompileAuditReport,
    SkipReviewReport,
    SkipApproveReport,
    SkipSendReportForRevision,
    SkipUpdateAndResubmitReport,
    SkipSubmitDocuments,
    SkipArchiveReport,
    SkipCloseAuditProcess
])

# Define the partial order relationships
root.order.add_edge(SendNotification, GatherDocuments)
root.order.add_edge(SendNotification, PrepareStatements)
root.order.add_edge(GatherDocuments, ReviewSubmission)
root.order.add_edge(PrepareStatements, ReviewSubmission)
root.order.add_edge(ReviewSubmission, RequestClarifications)
root.order.add_edge(RequestClarifications, ReceiveClarifications)
root.order.add_edge(ReceiveClarifications, CompleteRiskAssessment)
root.order.add_edge(CompleteRiskAssessment, EvaluateComplianceRisks)
root.order.add_edge(CompleteRiskAssessment, EvaluateFinancialRisks)
root.order.add_edge(CompleteRiskAssessment, EvaluateOperationalRisks)
root.order.add_edge(EvaluateComplianceRisks, ConductDataAnalysis)
root.order.add_edge(EvaluateFinancialRisks, ConductDataAnalysis)
root.order.add_edge(EvaluateOperationalRisks, ConductDataAnalysis)
root.order.add_edge(ConductDataAnalysis, ConductInterviews)
root.order.add_edge(ConductInterviews, PerformSiteVisits)
root.order.add_edge(PerformSiteVisits, LaunchDetailedInvestigation)
root.order.add_edge(LaunchDetailedInvestigation, CompileAuditReport)
root.order.add_edge(CompileAuditReport, ReviewReport)
root.order.add_edge(ReviewReport, ApproveReport)
root.order.add_edge(ApproveReport, SendReportForRevision)
root.order.add_edge(SendReportForRevision, UpdateAndResubmitReport)
root.order.add_edge(UpdateAndResubmitReport, SubmitDocuments)
root.order.add_edge(SubmitDocuments, ArchiveReport)
root.order.add_edge(ArchiveReport, CloseAuditProcess)
root.order.add_edge(CheckRegUpdates, ReviewSubmission)
root.order.add_edge(ReviewSubmission, ReviewSubmission)
root.order.add_edge(RequestClarifications, RequestClarifications)
root.order.add_edge(ReceiveClarifications, ReceiveClarifications)
root.order.add_edge(CompleteRiskAssessment, CompleteRiskAssessment)
root.order.add_edge(EvaluateComplianceRisks, EvaluateComplianceRisks)
root.order.add_edge(EvaluateFinancialRisks, EvaluateFinancialRisks)
root.order.add_edge(EvaluateOperationalRisks, EvaluateOperationalRisks)
root.order.add_edge(ConductDataAnalysis, ConductDataAnalysis)
root.order.add_edge(ConductInterviews, ConductInterviews)
root.order.add_edge(PerformSiteVisits, PerformSiteVisits)
root.order.add_edge(LaunchDetailedInvestigation, LaunchDetailedInvestigation)
root.order.add_edge(CompileAuditReport, CompileAuditReport)
root.order.add_edge(ReviewReport, ReviewReport)
root.order.add_edge(ApproveReport, ApproveReport)
root.order.add_edge(SendReportForRevision, SendReportForRevision)
root.order.add_edge(UpdateAndResubmitReport, UpdateAndResubmitReport)
root.order.add_edge(SubmitDocuments, SubmitDocuments)
root.order.add_edge(ArchiveReport, ArchiveReport)
root.order.add_edge(CloseAuditProcess, CloseAuditProcess)

# Print the final root POWL model
print(root)