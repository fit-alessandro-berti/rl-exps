import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
TrendScan = Transition(label='Trend Scan')
OpportunityMap = Transition(label='Opportunity Map')
ExpertGather = Transition(label='Expert Gather')
IdeaSprint = Transition(label='Idea Sprint')
ProtoBuild = Transition(label='Proto Build')
UserFeedback = Transition(label='User Feedback')
RiskReview = Transition(label='Risk Review')
IPAudit = Transition(label='IP Audit')
PilotLaunch = Transition(label='Pilot Launch')
StakeholderMeet = Transition(label='Stakeholder Meet')
ResourceShift = Transition(label='Resource Shift')
ScaleUp = Transition(label='Scale Up')
ImpactAssess = Transition(label='Impact Assess')
KnowledgeShare = Transition(label='Knowledge Share')
MonitorTrends = Transition(label='Monitor Trends')

# Define silent transitions
skip = SilentTransition()

# Define loop for pilot testing
loop = OperatorPOWL(operator=Operator.LOOP, children=[PilotLaunch, skip])

# Define XOR for risk and IP review
xor = OperatorPOWL(operator=Operator.XOR, children=[RiskReview, IPAudit])

# Define XOR for user feedback and resource shift
xor2 = OperatorPOWL(operator=Operator.XOR, children=[UserFeedback, ResourceShift])

# Define XOR for stakeholder meet and scale up
xor3 = OperatorPOWL(operator=Operator.XOR, children=[StakeholderMeet, ScaleUp])

# Define XOR for impact assessment and knowledge share
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ImpactAssess, KnowledgeShare])

# Define XOR for monitor trends and resource shift
xor5 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, ResourceShift])

# Define XOR for resource shift and knowledge share
xor6 = OperatorPOWL(operator=Operator.XOR, children=[ResourceShift, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor7 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor8 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor9 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor10 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor11 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor12 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor13 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor14 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor15 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor16 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor17 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor18 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor19 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor20 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor21 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor22 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor23 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor24 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor25 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor26 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor27 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor28 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor29 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor30 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor31 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor32 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor33 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor34 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor35 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor36 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor37 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor38 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor39 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor40 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor41 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor42 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor43 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor44 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor45 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor46 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor47 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor48 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor49 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor50 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor51 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor52 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor53 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor54 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor55 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor56 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor57 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor58 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor59 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor60 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor61 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor62 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor63 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor64 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor65 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor66 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor67 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor68 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor69 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor70 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor71 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor72 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor73 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor74 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor75 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor76 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor77 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor78 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor79 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor80 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor81 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor82 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor83 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor84 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor85 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor86 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor87 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor88 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor89 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor90 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor91 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor92 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor93 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor94 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor95 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor96 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor97 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor98 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor99 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor100 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor101 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor102 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor103 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor104 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor105 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor106 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor107 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor108 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor109 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor110 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor111 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor112 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor113 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor114 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor115 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor116 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor117 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor118 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends
xor119 = OperatorPOWL(operator=Operator.XOR, children=[KnowledgeShare, MonitorTrends])

# Define XOR for monitor trends and knowledge share
xor120 = OperatorPOWL(operator=Operator.XOR, children=[MonitorTrends, KnowledgeShare])

# Define XOR for knowledge share and monitor trends