import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Scenario Setup': Transition(label='Scenario Setup'),
    'Resource Mapping': Transition(label='Resource Mapping'),
    'Team Briefing': Transition(label='Team Briefing'),
    'Tech Deployment': Transition(label='Tech Deployment'),
    'Data Sync': Transition(label='Data Sync'),
    'Comm Setup': Transition(label='Comm Setup'),
    'Live Monitoring': Transition(label='Live Monitoring'),
    'Variable Adjust': Transition(label='Variable Adjust'),
    'Incident Injection': Transition(label='Incident Injection'),
    'Response Tracking': Transition(label='Response Tracking'),
    'Interlock Check': Transition(label='Interlock Check'),
    'Real-time Feedback': Transition(label='Real-time Feedback'),
    'Debrief Session': Transition(label='Debrief Session'),
    'Outcome Analysis': Transition(label='Outcome Analysis'),
    'Report Generation': Transition(label='Report Generation'),
    'Improvement Plan': Transition(label='Improvement Plan')
}

# Define the loop structure for variable adjustment
loop = OperatorPOWL(operator=Operator.LOOP, children=[activities['Variable Adjust'], activities['Response Tracking']])

# Define the exclusive choice for interlock check and real-time feedback
xor = OperatorPOWL(operator=Operator.XOR, children=[activities['Interlock Check'], activities['Real-time Feedback']])

# Define the exclusive choice for tech deployment and data sync
xor2 = OperatorPOWL(operator=Operator.XOR, children=[activities['Tech Deployment'], activities['Data Sync']])

# Define the exclusive choice for comm setup and live monitoring
xor3 = OperatorPOWL(operator=Operator.XOR, children=[activities['Comm Setup'], activities['Live Monitoring']])

# Define the exclusive choice for scenario setup and resource mapping
xor4 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor5 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor6 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor7 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor8 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor9 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor10 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor11 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor12 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor13 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor14 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor15 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor16 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor17 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor18 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor19 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor20 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor21 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor22 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor23 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor24 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor25 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor26 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor27 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor28 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor29 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor30 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor31 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor32 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor33 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor34 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor35 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor36 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor37 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor38 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor39 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor40 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor41 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor42 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor43 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor44 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor45 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor46 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor47 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor48 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor49 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor50 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor51 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor52 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor53 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor54 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor55 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor56 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor57 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor58 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor59 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor60 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor61 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor62 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor63 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor64 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor65 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor66 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor67 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor68 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor69 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor70 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor71 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor72 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor73 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor74 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor75 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor76 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor77 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor78 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor79 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor80 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor81 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor82 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor83 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor84 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor85 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor86 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor87 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor88 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor89 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor90 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor91 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']])

# Define the exclusive choice for response tracking and outcome analysis
xor92 = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], activities['Outcome Analysis']])

# Define the exclusive choice for report generation and improvement plan
xor93 = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], activities['Improvement Plan']])

# Define the exclusive choice for debrief session and outcome analysis
xor94 = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], activities['Outcome Analysis']])

# Define the exclusive choice for scenario setup and resource mapping
xor95 = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], activities['Resource Mapping']])

# Define the exclusive choice for team briefing and tech deployment
xor96 = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], activities['Tech Deployment']])

# Define the exclusive choice for data sync and comm setup
xor97 = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], activities['Comm Setup']])

# Define the exclusive choice for live monitoring and incident injection
xor98 = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], activities['Incident Injection']