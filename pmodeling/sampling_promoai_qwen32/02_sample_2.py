import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Identify_need_for_new_hire = Transition(label='Identify need for new hire')
Create_job_description = Transition(label='Create job description')
Post_job_description = Transition(label='Post job description')
Collect_resumes = Transition(label='Collect resumes')
Screen_resumes = Transition(label='Screen resumes')
Conduct_initial_phone_interviews = Transition(label='Conduct initial phone interviews')
Invite_candidates_for_interviews = Transition(label='Invite candidates for interviews')
Conduct_in_person_interview = Transition(label='Conduct an in-person interview')
Conduct_virtual_interview = Transition(label='Conduct a virtual interview')
Choose_candidate = Transition(label='Choose candidate')
Extend_offer = Transition(label='Extend offer')
Negotiate_salary = Transition(label='Negotiate salary')
Begin_onboarding_process = Transition(label='Begin onboarding process')
Complete_paperwork = Transition(label='Complete paperwork')
Complete_orientation = Transition(label='Complete orientation')
Complete_training = Transition(label='Complete training')

# Define the loop for virtual or in-person interview choice
Interview_loop = OperatorPOWL(operator=Operator.LOOP, children=[Conduct_in_person_interview, Conduct_virtual_interview])

# Define the XOR choice for interviews
Interview_choice = OperatorPOWL(operator=Operator.XOR, children=[Conduct_in_person_interview, Conduct_virtual_interview])

# Define the root node
root = StrictPartialOrder(nodes=[
    Identify_need_for_new_hire, Create_job_description, Post_job_description, Collect_resumes, Screen_resumes,
    Conduct_initial_phone_interviews, Invite_candidates_for_interviews, Interview_loop, Choose_candidate, Extend_offer,
    Negotiate_salary, Begin_onboarding_process, Complete_paperwork, Complete_orientation, Complete_training
])

# Define the partial order
root.order.add_edge(Identify_need_for_new_hire, Create_job_description)
root.order.add_edge(Create_job_description, Post_job_description)
root.order.add_edge(Post_job_description, Collect_resumes)
root.order.add_edge(Collect_resumes, Screen_resumes)
root.order.add_edge(Screen_resumes, Conduct_initial_phone_interviews)
root.order.add_edge(Conduct_initial_phone_interviews, Invite_candidates_for_interviews)
root.order.add_edge(Invite_candidates_for_interviews, Interview_loop)
root.order.add_edge(Interview_loop, Choose_candidate)
root.order.add_edge(Choose_candidate, Extend_offer)
root.order.add_edge(Extend_offer, Negotiate_salary)
root.order.add_edge(Negotiate_salary, Begin_onboarding_process)
root.order.add_edge(Begin_onboarding_process, Complete_paperwork)
root.order.add_edge(Complete_paperwork, Complete_orientation)
root.order.add_edge(Complete_orientation, Complete_training)