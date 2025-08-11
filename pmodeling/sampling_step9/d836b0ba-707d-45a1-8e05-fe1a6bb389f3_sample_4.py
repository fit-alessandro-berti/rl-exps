import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSelect = Transition(label='Site Select')
DesignLayout = Transition(label='Design Layout')
SensorIntegrate = Transition(label='Sensor Integrate')
CropChoose = Transition(label='Crop Choose')
SoilPrepare = Transition(label='Soil Prepare')
IrrigationSetup = Transition(label='Irrigation Setup')
PestControl = Transition(label='Pest Control')
LightingInstall = Transition(label='Lighting Install')
StaffTrain = Transition(label='Staff Train')
ComplianceCheck = Transition(label='Compliance Check')
MarketAnalyze = Transition(label='Market Analyze')
PackageDesign = Transition(label='Package Design')
LogisticsPlan = Transition(label='Logistics Plan')
DataAnalyze = Transition(label='Data Analyze')
FeedbackLoop = Transition(label='Feedback Loop')

skip = SilentTransition()

siteSelectLoop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSelect, DesignLayout])
layoutDesignLoop = OperatorPOWL(operator=Operator.LOOP, children=[SensorIntegrate, CropChoose, SoilPrepare, IrrigationSetup, PestControl, LightingInstall])
staffTrainLoop = OperatorPOWL(operator=Operator.LOOP, children=[StaffTrain, ComplianceCheck, MarketAnalyze, PackageDesign, LogisticsPlan, DataAnalyze])
feedbackLoop = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop])

root = StrictPartialOrder(nodes=[siteSelectLoop, layoutDesignLoop, staffTrainLoop, feedbackLoop])
root.order.add_edge(siteSelectLoop, layoutDesignLoop)
root.order.add_edge(layoutDesignLoop, staffTrainLoop)
root.order.add_edge(staffTrainLoop, feedbackLoop)