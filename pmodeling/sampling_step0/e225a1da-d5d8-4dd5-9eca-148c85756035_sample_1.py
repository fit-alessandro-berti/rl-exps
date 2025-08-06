import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
SelectCrops = Transition(label='Select Crops')
InstallModules = Transition(label='Install Modules')
SetupSensors = Transition(label='Setup Sensors')
CalibrateClimate = Transition(label='Calibrate Climate')
ConfigureLighting = Transition(label='Configure Lighting')
IntegrateIoT = Transition(label='Integrate IoT')
TrainStaff = Transition(label='Train Staff')
RunTrials = Transition(label='Run Trials')
AnalyzeData = Transition(label='Analyze Data')
OptimizeYield = Transition(label='Optimize Yield')
CheckCompliance = Transition(label='Check Compliance')
PlanMarketing = Transition(label='Plan Marketing')
LaunchFacility = Transition(label='Launch Facility')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_survey = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, DesignLayout])
loop_layout = OperatorPOWL(operator=Operator.LOOP, children=[SelectCrops, InstallModules])
loop_sensors = OperatorPOWL(operator=Operator.LOOP, children=[SetupSensors, CalibrateClimate])
loop_lighting = OperatorPOWL(operator=Operator.LOOP, children=[ConfigureLighting, IntegrateIoT])
loop_training = OperatorPOWL(operator=Operator.LOOP, children=[TrainStaff, RunTrials])
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[AnalyzeData, OptimizeYield])
loop_compliance = OperatorPOWL(operator=Operator.LOOP, children=[CheckCompliance, PlanMarketing])

xor_survey_layout = OperatorPOWL(operator=Operator.XOR, children=[loop_survey, loop_layout])
xor_sensors_lighting = OperatorPOWL(operator=Operator.XOR, children=[loop_sensors, loop_lighting])
xor_training_data = OperatorPOWL(operator=Operator.XOR, children=[loop_training, loop_data])
xor_compliance_launch = OperatorPOWL(operator=Operator.XOR, children=[loop_compliance, LaunchFacility])

root = StrictPartialOrder(nodes=[xor_survey_layout, xor_sensors_lighting, xor_training_data, xor_compliance_launch])
root.order.add_edge(xor_survey_layout, xor_sensors_lighting)
root.order.add_edge(xor_sensors_lighting, xor_training_data)
root.order.add_edge(xor_training_data, xor_compliance_launch)

print(root)