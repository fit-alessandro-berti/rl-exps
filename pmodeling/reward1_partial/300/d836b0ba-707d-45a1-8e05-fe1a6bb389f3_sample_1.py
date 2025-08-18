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

xor = OperatorPOWL(operator=Operator.XOR, children=[
    SiteSelect,
    DesignLayout,
    SensorIntegrate,
    CropChoose,
    SoilPrepare,
    IrrigationSetup,
    PestControl,
    LightingInstall,
    StaffTrain,
    ComplianceCheck,
    MarketAnalyze,
    PackageDesign,
    LogisticsPlan,
    DataAnalyze,
    FeedbackLoop
])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, xor)