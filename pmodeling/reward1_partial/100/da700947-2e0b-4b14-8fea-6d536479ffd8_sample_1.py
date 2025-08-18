import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
Climate_Design = Transition(label='Climate Design')
Lighting_Setup = Transition(label='Lighting Setup')
Irrigation_Plan = Transition(label='Irrigation Plan')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Install = Transition(label='Sensor Install')
AI_Calibration = Transition(label='AI Calibration')
Pest_Scan = Transition(label='Pest Scan')
Energy_Audit = Transition(label='Energy Audit')
Renewable_Sync = Transition(label='Renewable Sync')
Data_Modeling = Transition(label='Data Modeling')
Staff_Briefing = Transition(label='Staff Briefing')
Compliance_Check = Transition(label='Compliance Check')
Community_Meet = Transition(label='Community Meet')
Yield_Review = Transition(label='Yield Review')
Feedback_Loop = Transition(label='Feedback Loop')

# Define the partial order model
root = StrictPartialOrder(
    nodes=[
        Site_Survey,
        Structural_Audit,
        Climate_Design,
        Lighting_Setup,
        Irrigation_Plan,
        Nutrient_Mix,
        Sensor_Install,
        AI_Calibration,
        Pest_Scan,
        Energy_Audit,
        Renewable_Sync,
        Data_Modeling,
        Staff_Briefing,
        Compliance_Check,
        Community_Meet,
        Yield_Review,
        Feedback_Loop
    ]
)

# Define the dependencies between activities
root.order.add_edge(Site_Survey, Structural_Audit)
root.order.add_edge(Site_Survey, Climate_Design)
root.order.add_edge(Site_Survey, Lighting_Setup)
root.order.add_edge(Site_Survey, Irrigation_Plan)
root.order.add_edge(Site_Survey, Nutrient_Mix)
root.order.add_edge(Site_Survey, Sensor_Install)
root.order.add_edge(Site_Survey, AI_Calibration)
root.order.add_edge(Site_Survey, Pest_Scan)
root.order.add_edge(Site_Survey, Energy_Audit)
root.order.add_edge(Site_Survey, Renewable_Sync)
root.order.add_edge(Site_Survey, Data_Modeling)
root.order.add_edge(Site_Survey, Staff_Briefing)
root.order.add_edge(Site_Survey, Compliance_Check)
root.order.add_edge(Site_Survey, Community_Meet)
root.order.add_edge(Site_Survey, Yield_Review)
root.order.add_edge(Site_Survey, Feedback_Loop)

root.order.add_edge(Structural_Audit, Climate_Design)
root.order.add_edge(Structural_Audit, Lighting_Setup)
root.order.add_edge(Structural_Audit, Irrigation_Plan)
root.order.add_edge(Structural_Audit, Nutrient_Mix)
root.order.add_edge(Structural_Audit, Sensor_Install)
root.order.add_edge(Structural_Audit, AI_Calibration)
root.order.add_edge(Structural_Audit, Pest_Scan)
root.order.add_edge(Structural_Audit, Energy_Audit)
root.order.add_edge(Structural_Audit, Renewable_Sync)
root.order.add_edge(Structural_Audit, Data_Modeling)
root.order.add_edge(Structural_Audit, Staff_Briefing)
root.order.add_edge(Structural_Audit, Compliance_Check)
root.order.add_edge(Structural_Audit, Community_Meet)
root.order.add_edge(Structural_Audit, Yield_Review)
root.order.add_edge(Structural_Audit, Feedback_Loop)

root.order.add_edge(Climate_Design, Lighting_Setup)
root.order.add_edge(Climate_Design, Irrigation_Plan)
root.order.add_edge(Climate_Design, Nutrient_Mix)
root.order.add_edge(Climate_Design, Sensor_Install)
root.order.add_edge(Climate_Design, AI_Calibration)
root.order.add_edge(Climate_Design, Pest_Scan)
root.order.add_edge(Climate_Design, Energy_Audit)
root.order.add_edge(Climate_Design, Renewable_Sync)
root.order.add_edge(Climate_Design, Data_Modeling)
root.order.add_edge(Climate_Design, Staff_Briefing)
root.order.add_edge(Climate_Design, Compliance_Check)
root.order.add_edge(Climate_Design, Community_Meet)
root.order.add_edge(Climate_Design, Yield_Review)
root.order.add_edge(Climate_Design, Feedback_Loop)

root.order.add_edge(Lighting_Setup, Irrigation_Plan)
root.order.add_edge(Lighting_Setup, Nutrient_Mix)
root.order.add_edge(Lighting_Setup, Sensor_Install)
root.order.add_edge(Lighting_Setup, AI_Calibration)
root.order.add_edge(Lighting_Setup, Pest_Scan)
root.order.add_edge(Lighting_Setup, Energy_Audit)
root.order.add_edge(Lighting_Setup, Renewable_Sync)
root.order.add_edge(Lighting_Setup, Data_Modeling)
root.order.add_edge(Lighting_Setup, Staff_Briefing)
root.order.add_edge(Lighting_Setup, Compliance_Check)
root.order.add_edge(Lighting_Setup, Community_Meet)
root.order.add_edge(Lighting_Setup, Yield_Review)
root.order.add_edge(Lighting_Setup, Feedback_Loop)

root.order.add_edge(Irrigation_Plan, Nutrient_Mix)
root.order.add_edge(Irrigation_Plan, Sensor_Install)
root.order.add_edge(Irrigation_Plan, AI_Calibration)
root.order.add_edge(Irrigation_Plan, Pest_Scan)
root.order.add_edge(Irrigation_Plan, Energy_Audit)
root.order.add_edge(Irrigation_Plan, Renewable_Sync)
root.order.add_edge(Irrigation_Plan, Data_Modeling)
root.order.add_edge(Irrigation_Plan, Staff_Briefing)
root.order.add_edge(Irrigation_Plan, Compliance_Check)
root.order.add_edge(Irrigation_Plan, Community_Meet)
root.order.add_edge(Irrigation_Plan, Yield_Review)
root.order.add_edge(Irrigation_Plan, Feedback_Loop)

root.order.add_edge(Nutrient_Mix, Sensor_Install)
root.order.add_edge(Nutrient_Mix, AI_Calibration)
root.order.add_edge(Nutrient_Mix, Pest_Scan)
root.order.add_edge(Nutrient_Mix, Energy_Audit)
root.order.add_edge(Nutrient_Mix, Renewable_Sync)
root.order.add_edge(Nutrient_Mix, Data_Modeling)
root.order.add_edge(Nutrient_Mix, Staff_Briefing)
root.order.add_edge(Nutrient_Mix, Compliance_Check)
root.order.add_edge(Nutrient_Mix, Community_Meet)
root.order.add_edge(Nutrient_Mix, Yield_Review)
root.order.add_edge(Nutrient_Mix, Feedback_Loop)

root.order.add_edge(Sensor_Install, AI_Calibration)
root.order.add_edge(Sensor_Install, Pest_Scan)
root.order.add_edge(Sensor_Install, Energy_Audit)
root.order.add_edge(Sensor_Install, Renewable_Sync)
root.order.add_edge(Sensor_Install, Data_Modeling)
root.order.add_edge(Sensor_Install, Staff_Briefing)
root.order.add_edge(Sensor_Install, Compliance_Check)
root.order.add_edge(Sensor_Install, Community_Meet)
root.order.add_edge(Sensor_Install, Yield_Review)
root.order.add_edge(Sensor_Install, Feedback_Loop)

root.order.add_edge(AI_Calibration, Pest_Scan)
root.order.add_edge(AI_Calibration, Energy_Audit)
root.order.add_edge(AI_Calibration, Renewable_Sync)
root.order.add_edge(AI_Calibration, Data_Modeling)
root.order.add_edge(AI_Calibration, Staff_Briefing)
root.order.add_edge(AI_Calibration, Compliance_Check)
root.order.add_edge(AI_Calibration, Community_Meet)
root.order.add_edge(AI_Calibration, Yield_Review)
root.order.add_edge(AI_Calibration, Feedback_Loop)

root.order.add_edge(Pest_Scan, Energy_Audit)
root.order.add_edge(Pest_Scan, Renewable_Sync)
root.order.add_edge(Pest_Scan, Data_Modeling)
root.order.add_edge(Pest_Scan, Staff_Briefing)
root.order.add_edge(Pest_Scan, Compliance_Check)
root.order.add_edge(Pest_Scan, Community_Meet)
root.order.add_edge(Pest_Scan, Yield_Review)
root.order.add_edge(Pest_Scan, Feedback_Loop)

root.order.add_edge(Energy_Audit, Renewable_Sync)
root.order.add_edge(Energy_Audit, Data_Modeling)
root.order.add_edge(Energy_Audit, Staff_Briefing)
root.order.add_edge(Energy_Audit, Compliance_Check)
root.order.add_edge(Energy_Audit, Community_Meet)
root.order.add_edge(Energy_Audit, Yield_Review)
root.order.add_edge(Energy_Audit, Feedback_Loop)

root.order.add_edge(Renewable_Sync, Data_Modeling)
root.order.add_edge(Renewable_Sync, Staff_Briefing)
root.order.add_edge(Renewable_Sync, Compliance_Check)
root.order.add_edge(Renewable_Sync, Community_Meet)
root.order.add_edge(Renewable_Sync, Yield_Review)
root.order.add_edge(Renewable_Sync, Feedback_Loop)

root.order.add_edge(Data_Modeling, Staff_Briefing)
root.order.add_edge(Data_Modeling, Compliance_Check)
root.order.add_edge(Data_Modeling, Community_Meet)
root.order.add_edge(Data_Modeling, Yield_Review)
root.order.add_edge(Data_Modeling, Feedback_Loop)

root.order.add_edge(Staff_Briefing, Compliance_Check)
root.order.add_edge(Staff_Briefing, Community_Meet)
root.order.add_edge(Staff_Briefing, Yield_Review)
root.order.add_edge(Staff_Briefing, Feedback_Loop)

root.order.add_edge(Compliance_Check, Community_Meet)
root.order.add_edge(Compliance_Check, Yield_Review)
root.order.add_edge(Compliance_Check, Feedback_Loop)

root.order.add_edge(Community_Meet, Yield_Review)
root.order.add_edge(Community_Meet, Feedback_Loop)

root.order.add_edge(Yield_Review, Feedback_Loop)

# Print the root model
print(root)