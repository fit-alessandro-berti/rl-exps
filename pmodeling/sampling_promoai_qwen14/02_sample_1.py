import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Begin_onboarding_process = Transition(label='Begin onboarding process')
Choose_candidate = Transition(label='Choose candidate')
Collect_resumes = Transition(label='Collect resumes')
Complete_orientation = Transition(label='Complete orientation')
Complete_paperwork = Transition(label='Complete paperwork')
Complete_training = Transition(label='Complete training')
Conduct_a_virtual_interview = Transition(label='Conduct a virtual interview')
Conduct_an_in_person_interview = Transition(label='Conduct an in-person interview')
Conduct_initial_phone_interviews = Transition(label='Conduct initial phone interviews')
Create_job_description = Transition(label='Create job description')
Extend_offer = Transition(label='Extend offer')
Identify_need_for_new_hire = Transition(label='Identify need for new hire')
Invite_candidates_for_interviews = Transition(label='Invite candidates for interviews')
Negotiate_salary = Transition(label='Negotiate salary')
Post_job_description = Transition(label='Post job description')
Screen_resumes = Transition(label='Screen resumes')

# Define the choice of virtual or in-person interview
Interview_choice = OperatorPOWL(operator=Operator.XOR, children=[Conduct_a_virtual_interview, Conduct_an_in_person_interview])

# Define the loop for conducting initial phone interviews
Initial_interview_loop = OperatorPOWL(operator=Operator.LOOP, children=[Conduct_initial_phone_interviews])

# Define the loop for negotiating salary
Salary_negotiation_loop = OperatorPOWL(operator=Operator.LOOP, children=[Negotiate_salary])

# Define the root of the process
root = StrictPartialOrder(nodes=[Identify_need_for_new_hire, Create_job_description, Post_job_description, Collect_resumes, Screen_resumes, Initial_interview_loop, Interview_choice, Choose_candidate, Invite_candidates_for_interviews, Extend_offer, Salary_negotiation_loop, Begin_onboarding_process, Complete_paperwork, Complete_orientation, Complete_training])

# Define the order of the activities
root.order.add_edge(Identify_need_for_new_hire, Create_job_description)
root.order.add_edge(Create_job_description, Post_job_description)
root.order.add_edge(Post_job_description, Collect_resumes)
root.order.add_edge(Collect_resumes, Screen_resumes)
root.order.add_edge(Screen_resumes, Initial_interview_loop)
root.order.add_edge(Initial_interview_loop, Interview_choice)
root.order.add_edge(Interview_choice, Choose_candidate)
root.order.add_edge(Choose_candidate, Invite_candidates_for_interviews)
root.order.add_edge(Invite_candidates_for_interviews, Extend_offer)
root.order.add_edge(Extend_offer, Salary_negotiation_loop)
root.order.add_edge(Salary_negotiation_loop, Begin_onboarding_process)
root.order.add_edge(Begin_onboarding_process, Complete_paperwork)
root.order.add_edge(Complete_paperwork, Complete_orientation)
root.order.add_edge(Complete_orientation, Complete_training)