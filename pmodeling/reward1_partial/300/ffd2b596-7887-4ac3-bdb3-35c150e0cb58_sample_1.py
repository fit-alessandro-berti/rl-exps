import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
ComponentSourcing = Transition(label='Component Sourcing')
SensorCalibrate = Transition(label='Sensor Calibrate')
MotorAssembly = Transition(label='Motor Assembly')
FrameBuild = Transition(label='Frame Build')
SoftwareInstall = Transition(label='Software Install')
AlgorithmTune = Transition(label='Algorithm Tune')
BatteryIntegrate = Transition(label='Battery Integrate')
SignalTest = Transition(label='Signal Test')
DurabilityCheck = Transition(label='Durability Check')
FlightSimulate = Transition(label='Flight Simulate')
QualityInspect = Transition(label='Quality Inspect')
ComplianceReview = Transition(label='Compliance Review')
PackagingPrep = Transition(label='Packaging Prep')
LogisticsPlan = Transition(label='Logistics Plan')
ClientFeedback = Transition(label='Client Feedback')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        ComponentSourcing,
        SensorCalibrate,
        MotorAssembly,
        FrameBuild,
        SoftwareInstall,
        AlgorithmTune,
        BatteryIntegrate,
        SignalTest,
        DurabilityCheck,
        FlightSimulate,
        QualityInspect,
        ComplianceReview,
        PackagingPrep,
        LogisticsPlan,
        ClientFeedback
    ]
)

# Add dependencies based on the process description
root.order.add_edge(ComponentSourcing, SensorCalibrate)
root.order.add_edge(ComponentSourcing, MotorAssembly)
root.order.add_edge(ComponentSourcing, FrameBuild)
root.order.add_edge(SensorCalibrate, SoftwareInstall)
root.order.add_edge(SensorCalibrate, AlgorithmTune)
root.order.add_edge(SensorCalibrate, BatteryIntegrate)
root.order.add_edge(MotorAssembly, SignalTest)
root.order.add_edge(FrameBuild, DurabilityCheck)
root.order.add_edge(SoftwareInstall, FlightSimulate)
root.order.add_edge(AlgorithmTune, FlightSimulate)
root.order.add_edge(BatteryIntegrate, FlightSimulate)
root.order.add_edge(DurabilityCheck, QualityInspect)
root.order.add_edge(QualityInspect, ComplianceReview)
root.order.add_edge(ComplianceReview, PackagingPrep)
root.order.add_edge(PackagingPrep, LogisticsPlan)
root.order.add_edge(LogisticsPlan, ClientFeedback)

print(root)