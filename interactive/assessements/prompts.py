
engagement = """An engaging system actively encourages user to engage and explore a topic, using the right tools and interactions (e.g., asking follow-up questions and providing a high-level overview of a topic). 
To what extent does the system encourage the user to engage with it within this subtopic? 
Engagement is rated with an integer score betwen 1-5. Each score has the following meanings:

Score 5: True Collaborative Partner
• Feels like a proactive, intelligent, and helpful conversation partner, not just a tool. 
• Re-frames or deepens the topic in a helpful way. 
• Makes the user feel that what they say is synthesized and understood. 
• If the user provides a correction, immediately and perfectly incorporates the correction and demonstrates a complete understanding of why the correction was needed. 

Score 4: Effective Collaborator 
• Interacts effectively to help the user but not beyond what the user asked it to do. 
• Moves the conversation forward. 
• Reliably accounts for the user's input in its next turn. 
• If the user provides a correction, immediately incorporates the correction, but not showing a complete understanding of why the correction was needed. 


Score 3: Functional Tool 
• The interaction is functional but not truly collaborative. 
• It answers questions directly but as if it had said everything on the topic and had nothing further to add, thus not encouraging the user to engage more. 
• If the user provides a correction, acknowledges the feedback but applies it incompletely (e.g., fixes only a part of an error). 


Score 2: Clumsy Assistant 
• The interaction feels clunky and disjointed. 
• If it provides help, it is too generic, ill-timed, or off-topic. 
• The user has to work hard to keep the conversation on track. 
• If the user provides a correction, acknowledges the feedback but does not really react to it, perhaps only making a trivial wording change. 



Score 1: Passive Obstacle 
• The system is passive, obstructive, or creates conversational dead-ends. 
• It feels as if the user is interrogating the system to squeeze information out of it. 
• If the user provides a correction, ignores it completely. 


# Guidance for Borderline Cases: 
- Score 4 vs. 5: A '5' elevates the conversation; you might think, "That's a great question, I hadn't thought of that." A '4' competently continues the conversation. The presence of insightful brilliance is the mark of a '5'. 
- Score 3 vs. 4: A '4' feels like a two-way street. A '3' feels like a one-way street where the user is doing all the driving. 
- Score 2 vs. 3: A '3' is helpful if you direct it perfectly. A '2' is actively unhelpful, and its attempts to "help" (e.g., bad questions) make the task harder. 
- Score 2 vs. 1: A '2' at least signals an attempt to converse with the user. A '1' is like talking to a wall. 
"""

relevance_and_usefulness = """Given the conversation history, user’s latest request, and user’s PTKB, how would you assess the relevance and usefulness of the generated response to the user’s request?
The relevance and usefulness of the generated response is rated with an integer score betwen 1-5. Each score has the following meanings:

Score 5: Fully Meets 
• The response is a ‘perfect’ response to the utterance. It contains a complete answer to the utterance and doesn’t contain anything extraneous. 

Score 4: Highly meets 
• The response answers the utterance and is focused on the answer (i.e., what a system should deliver). 

Score 3: Moderately Meets 
• The response answers the utterance to some extent, but focuses on other topics related to the request as well (i.e., it might initially be unclear why a system generated this answer but somehow contains the answer). 

Score 2: Slightly meets 
• The answer can be inferred from the generated response with reasonable effort (i.e., better than nothing). 

Score 1: Fails to meet 
• Not relevant. No useful or relevant information is given. 

# Guidance for Borderline Cases: 
- Score 4 vs. 5: A '5' makes an extra effort to cover multiple aspects of the topic, and to provide a complete and comprehensive response. A '4' provides a relevant and acceptable response, but fails to cover multiple aspects and is not as comprehensive as a ‘5’. 
- Score 3 vs. 4: A '4' is the relevant but not complete, while a '3' feels like a somewhat relevant and related response, but not exactly on the topic.  
- Score 2 vs. 3: A '3' is helpful in finding the right response, even though it’s not exactly what the user is looking for. A '2' is barely providing a relevant response to the question. It could give some hints or useful tips but generally does not give the right response. 
"""

overall_subtopic_quality = """ Considering all factors (relevance, engagement, and other factors that were not covered by our questions), what is the overall quality and utility of the system's performance for this subtopic? 
The overall quality and utility of system is rated with an integer score betwen 1-5. Each score has the following meanings:


Score 5: Exceptional 
• The system's contribution to this subtopic was flawless: accurate, fully relevant, and highly collaborative. You cannot think of a better system. 
• It fully resolved this part of the user's information need. 

Score 4: Good 
• The system's contribution was helpful and effective, despite minor flaws in one area (e.g., a slightly clumsy question).  
• It largely resolved this part of the need. 

Score 3: Acceptable 
• The system provided some useful information, but the system exhibited some flaws (e.g., incompleteness, poor engagement). 
• A mixed bag. 

Score 2: Poor 
• The system's contribution was mostly unhelpful due to major and significant flaws. 
• The small amount of useful information was outweighed by the negatives. 

Score 1: Unacceptable 
• The system's contribution to this subtopic was useless, irrelevant, or counter-productive. 
• It failed completely on this part of the task. 
"""

rater_confidence = """ How confident are you in the scores you provided for this sub-topic? 

Score 3: High Confidence 
The interaction was clear and my scores felt unambiguous. 

Score 2: Medium Confidence
The interaction had some ambiguity that required significant interpretation. 

Score 1: Low Confidence
The interaction was very confusing, making it difficult to apply the rubric with certainty. 
"""

mixed_initiative_strategies = """An effective proactive system employs a variety of strategies while interacting with the user, e.g., it asks clarifying questions, or tries to elicit the user’s preference by asking questions and would ask follow-up questions to make user more engaged in the dialogue. 
How well does the system employ a portfolio of different proactive actions (e.g., asking clarifying questions, asking follow-up questions, asking for feedback, etc.) throughout the conversation?


Score 5: Masterfully proactive assistant 
• Deploys the right proactive strategy (asking the user to clarify, eliciting preferences proactively, offering alternatives, suggesting what to ask next, etc.) at the right time.  
• Adapts its approach to the user and conversation as the conversation evolves. 
• Uses a set of proactive actions that help the user reach their goal more effectively. 

Score 4: Competent & Proactive 
• Effectively uses some strategies but sometimes at the wrong time. 
• The system is clearly proactive and makes a consistent effort to guide the conversation. 

Score 3: Limited but Functional 
• The system is mostly reactive (e.g., only answers to the user’s questions) with one or two notable exceptions in which the system applied a strategy effectively. 
• In some cases, it tries to use some strategies but not as effectively (e.g., it tries to ask a clarifying question, but the user already provided the requested information). 
• It chooses to always do a proactive action (e.g., ask clarifying questions) even though there is clearly no need for them to be asked. 

Score 2: Attempted but Flawed 
• Attempts to use a strategy, but the execution is poor (e.g., asks a question that confuses or misleads the user). 
• An attempt is visible but not helpful and may hinder the conversation. 

Score 1: Purely Reactive 
• The system provides only answers. 
• It never asks a question, elicits a preference, or suggests a next step. 

# Guidance for Borderline Cases: 

Score 4 vs. 5: A '5' demonstrates variety and adaptivity; it might start with elicitating preferences and then move to specific suggestions. A '4' might use the same strategy (e.g., clarifying questions) well throughout, but doesn't show that adaptive range. 
Score 3 vs. 4: A '4' feels like the system is trying to share the conversational load. A '3' places almost all of the load on the user. 
Score 1 vs. 2: A '2' at least tries to be proactive, even if it fails. A '1' never even makes the attempt. 
"""

personalization = """An effective personalized system should appropriately tailor its responses to the user persona when necessary. The personalization aspects have two dimensions: style and content. Style refers to the tone, detail and vocabulary that is familiar to the user, while content refers to understanding the user’s interest and constraints while providing the answer (e.g., if the user is vegan, avoid suggesting cow’s milk to them). 
How well does the system tailor the dialogue to the specific user persona provided?


Score 5: Deeply Personalized 
• Consistently and accurately tailors responses to the user persona throughout. 
• Remembers and applies user preferences and constraints (e.g., budget, diet, interests). 
• The tone, vocabulary, and level of detail are perfectly matched to the persona. 
• Explicitly references the persona in responses to enhance relevance (e.g., “Because you’re vegan, I’m recommending …”).  

Score 4: Successfully Personalized 
• Clearly attempts to personalize responses for the user persona. 
• The responses are highly personalized, but may not explicitly reference the persona in every instance. 
• May occasionally overlook a minor preference or apply a constraint inconsistently once, but overall demonstrates helpful and intentional personalization. 

Score 3: Superficially Personalized 
• Mentions a persona constraint at least once, but fails to consistently apply it in subsequent responses. 
• The personalization is present but unreliable and feels "tacked on." 
• Lacks a coherent strategy for personalization, leading to largely generic suggestions. 

Score 2: Incorrectly Personalized 
• Provides suggestions that directly contradict the persona's stated preferences or constraints (e.g., suggesting an expensive option to a budget user). 
• Attempts at personalization are counterproductive, making the response less relevant or helpful. 

Score 1: Entirely Generic 
• Provides generic responses with no awareness of the user persona, even when constraints are explicitly mentioned in the dialogue. 

# Guidance for Borderline Cases: 

Score 4 vs. 5: A '5' feels like it was built just for this user. A '4' feels like a generic system that has been competently adapted for this user. The difference is in the seamlessness. 
Score 3 vs. 4: Consistency is key. A '4' remembers the persona constraints across multiple turns and sub-topics. A '3' will remember for one turn and forget in the next. 
Score 1 vs. 2: A '2' tries and fails (e.g., "I know you're a beginner, so here's a complex explanation..."). A '1' shows no evidence of even trying. 
"""

information_flow_and_coherence = """An effective information flow refers to a reasonable information rate while providing the response to the user. An effective system would try to scaffold the information and provide the response in hierarchical order (i.e., start with high-level concepts and then go in more detail with the more specific aspects of the topic). It would also try to adapt the information rate to the user’s understanding of the topic, i.e., to avoid throwing a lot of information to the user all at once. Moreover, the system should avoid unnecessary verbosity, contradiction, repetition, and abrupt topic shifts in different turns. 

Score 5: Seamless & Logical 
• The dialogue is perfectly coherent and exceptionally easy to follow. 
• The system scaffolds the complex information into multiple digestible steps. 
• It remembers context and user history flawlessly across all turns. 
• Transitions between subtopics are smooth and well-motivated. 

Score 4: Coherent with Minor Flaws 
• The conversation is largely coherent. 
• The system attempts to do scaffolding but it’s not doing it perfectly. 
• It may briefly forget a minor detail but quickly gets back on track. 
• One transition between topics might feel slightly abrupt, but doesn't break the dialogue. 

Score 3: Functional but Clunky 
• The dialogue is generally understandable but has noticeable flaws. 
• The system’s attempt to scaffolding is unsuccessful. 
• The system ‍ or requires the user to periodically remind it of context. 
• You can follow it, but it requires effort. 

Score 2: Disjointed & Confusing 
• The conversation is hard to follow due to frequent contradictions or contextual "amnesia."  
• The system jumps between topics illogically. 

Score 1: Incoherent 
• The dialogue is nonsensical. Each turn feels disconnected from the last. 
• Contextual memory is effectively zero, making a productive conversation impossible. 

# Guidance for Borderline Cases: 

Score 4 vs. 5: A '5' has zero contradictions or context drops. A '4' might have one that is minor and quickly recovered from. 
Score 3 vs. 4: A '4' requires almost no effort to follow. A '3' requires the rater to actively work to connect the dots and overlook clumsy parts. 
Score 2 vs. 3: A '3' is a difficult conversation. A '2' is a barely-a-conversation; it feels more like a series of disconnected exchanges. 
"""

trustworthiness = """After examining the whole dialog, how likely would you be to believe that past and future answers of this system are factually correct? A trustworthy system is transparent about its source of knowledge (e.g., where was conveyed knowledge obtained from), refer to domain expert on sensible topics (e.g., physicians on medical topics), and transports appropriate levels of confidence. 
Please also consider other factors that contribute to your perceived trustworthiness in your rating. 


Score 5: Exemplary 
• Fully transparent about where the knowledge was obtained from 
• Proactively refers to domain experts or refuses to answer on sensible topics (e.g., medical, financial). 
• Explicitly acknowledges when it cannot find information or has low confidence. 

Score 4: Reliable 
• Mostly transparent about where the knowledge was obtained from 
• May not refer to domain experts but does not give potentially harmful advice on sensible topics (e.g., medical, financial). 

Score 3: Inconsistent 
• Untransparent about where the knowledge was obtained from 
• May not refer to domain experts but does not give potentially harmful advice on sensible topics (e.g., medical, financial). 
• No obvious factually incorrect claim  

Score 2: Unreliable 
• Untransparent about where the knowledge was obtained from 
• May not refer to domain experts but does not give potentially harmful advice on sensible topics (e.g., medical, financial). 
• Contains at least one factually incorrect or unverifiable claim 

Score 1: Actively Misleading 
• Untransparent about where the knowledge was obtained from 
• Provides potentially harmful advice on sensible topics (e.g., medical, financial). 
• Contains multiple factually incorrect or unverifiable claim 

# Guidance for Borderline Cases: 

Score 4 vs. 5: Systems assigned a '5' demonstrates proactive responsibility (e.g., "This articles says..., but you should consult a doctor on this topic."). A '4' is simply not irresponsible (e.g., "This articles says..."). The presence of explicit, well-handled referrals to domain experts earns a '5'. 
Score 3 vs. 4: For systems assigned a '4' users would typically not do an external verification. Users of systems assigned a '3' will probably verify the responses externally. The default state for a '3' is skepticism. 
Score 1 vs. 2: Systems assigned a  '2' is unreliable due to incompetence (it makes errors). Systems assigned a '1' feels maliciously or dangerously unreliable (it presents dangerous advice as fact). 
"""

overall_user_satisfaction = """Considering the entire dialogue, how satisfied would you be as the user and how successful was the interaction? Would you use this system yourself? 
Bear in mind that the current user is a simulated user, and therefore its language might not reflect actual user satisfaction and system performance (e.g., “Thank you very much for your great answer”).


Score 5: Task Perfected 
• The user's information goal was fully met, and the process was efficient and enjoyable. 
• The system may have provided additional, serendipitously useful information, that the user wouldn’t have thought of but that helped him understand his/her own need. 
• The conversation is unambiguous and an exemplary success. 

Score 4: Task Accomplished 
• The user's primary goal was clearly met. You would be satisfied as a user and re-use the system. 
• The interaction was helpful and positive, despite minor inefficiencies along the way. 

Score 3: Task Partially Met 
• The user got some useful information, but the overall goal was not fully met. 
• The process may have been unnecessarily complex but was not a complete failure. 
 
Score 2: Task Failed 
• The user's primary goal was not met. 
• The interaction was frustrating, confusing, or misleading. The user would need to start over elsewhere. 

Score 1: Task Undermined 
• The system was completely useless or counter-productive. 
• It wasted the user's time or left them more confused than when they started. 
"""

rubric_level_prompt = """Your task is to assess the given dialogue on a set of rubrics.
You will be given the user persona (PTKB) and dialogue history. You should assess the given aspects about the 'system' in the conversation.

##  The aspect is: Engagement
Aspect description: {engagement}

##  The aspect is: Relevance and Usefulness
Aspect description: {relevance_and_usefulness}

##  The aspect is: Overall subtopic quality
Aspect description: {overall_subtopic_quality}

##  The aspect is: Confidence
Aspect description: {rater_confidence}

##  The user persona: 
{PTKB}

##  The dialogue history: 
{history}

Please provide your answer in the json format like this:
{{
  engagement: score (an integer number in the given range) ,
  relevance_and_usefulness: score (an integer number in the given range) ,
  overall_subtopic_quality: score (an integer number in the given range) ,
  confidence: score (an integer number in the given range) 
}}
"""

dialog_level_prompt = """Your task is to assess the given dialogue on a set of rubrics.
You will be given the user persona (PTKB) and dialogue history. You should assess the given aspects about the 'system' in the conversation.

##  The aspect is: Mixed initiative strategies
Aspect description: {mixed_initiative_strategies}

##  The aspect is: Personalization
Aspect description: {personalization}

##  The aspect is: Information flow and coherence
Aspect description: {information_flow_and_coherence}

##  The aspect is: Trustworthiness
Aspect description: {trustworthiness}

##  The aspect is: Overall user satisfaction
Aspect description: {overall_user_satisfaction}

##  The aspect is: Confidence
Aspect description: {rater_confidence}

##  The user persona: 
{PTKB}

##  The dialogue history: 
{history}

Please provide your answer in the json format like this:
{{ 
  mixed_initiative_strategies: score (an integer number in the given range) ,
  personalization: score (an integer number in the given range) ,
  information_flow_and_coherence: score (an integer number in the given range) ,
  trustworthiness: score (an integer number in the given range) , 
  overall_user_satisfaction: score (an integer number in the given range) , 
  confidence: score (an integer number in the given range) 
}}
"""

rubric_level_single_prompt = """Your task is to assess the given dialogue on a given rubric.
You will be given the user persona (PTKB) and dialogue history. You should assess the given aspect about the 'system' in the conversation.

##  The aspect is: {aspect_name}
Aspect description: {aspect_description}

##  The user persona: 
{PTKB}

##  The dialogue history: 
{history}

Please provide your answer in the json format like this:
{{
  "{aspect_name}": score (an integer number in the given range)
}}
"""

dialog_level_single_prompt = """Your task is to assess the given dialogue on a given rubric.
You will be given the user persona (PTKB) and dialogue history. You should assess the given aspect about the 'system' in the conversation.

## The aspect is: {aspect_name}
Aspect description: {aspect_description}

## The user persona: 
{PTKB}

## The dialogue history: 
{history}

Please provide your answer in the json format like this:
{{ 
  "{aspect_name}": score (an integer number in the given range)
}}
"""

rubric_scores = { 'engagement': {'Functional Tool': 3,
                                'Effective Collaborator': 4,
                                'Clumsy Assistant': 2,
                                'True Collaborative Partner': 5,
                                'Passive Obstacle': 1},
 
 'relevance-and-usefulness': { 'Fully Meets': 5,
                               'Highly meets': 4,
                               'Slightly meets': 2,
                               'Moderately Meets': 3,
                               'Fails to meet':1},

 'overall-subtopic-quality': {'Exceptional': 5,
                               'Good': 4,
                               'Acceptable': 3,
                                'Unacceptable': 1,
                                'Poor': 2},

 'rater-confidence': {'High confidence': 3,
                      'Low confidence': 1,
                       'Medium confidence': 2}
}

dialog_scores = { 'mixed-initiative-strategies': {'Purely Reactive': 1,
                                   'Limited but Functional': 3,
                                   'Masterful & Adaptive': 5,
                                   'Competent & Proactive': 4,
                                   'Attempted but Flawed': 2},
                                   
    'personalization': {'Superficially Personalized': 3,
                                   'Entirely Generic': 1,
                                   'Successfully Personalized': 4,
                                   'Deeply Personalized': 5,
                                   'Incorrectly Personalized': 2},

     'information-flow-and-coherence': {'Seamless & Logical': 5,
                                        'Coherent with Minor Flaws': 4,
                                        'Functional but Clunky': 3,
                                        'Disjointed & Confusing': 2, 
                                        'Incoherent':1},
      'trustworthiness':{'Reliable': 4,
                                   'Inconsistent': 3,
                                   'Exemplary': 5,
                                   'Unreliable': 2,
                                   'Actively Misleading': 1},

       'overall-user-satisfaction': {'Task Partially Met': 3,
                                   'Task Accomplished': 4,
                                   'Task Perfected': 5,
                                   'Task Failed': 2,
                                   'Task Undermined': 1},

        'rater-confidence': {'High confidence': 3,
                        'Low confidence': 1,
                             'Medium confidence': 2} 
                }









engagement_short = """An engaging system actively encourages user to engage and explore a topic, using the right tools and interactions (e.g., asking follow-up questions and providing a high-level overview of a topic). 
To what extent does the system encourage the user to engage with it within this subtopic? 
Engagement is rated with an integer score betwen 1-5. Each score has the following meanings:

Score 5: True Collaborative Partner
Score 4: Effective Collaborator 
Score 3: Functional Tool 
Score 2: Clumsy Assistant 
Score 1: Passive Obstacle 

"""

relevance_and_usefulnesst_short = """Given the conversation history, user’s latest request, and user’s PTKB, how would you assess the relevance and usefulness of the generated response to the user’s request?
The relevance and usefulness of the generated response is rated with an integer score betwen 1-5. Each score has the following meanings:

Score 5: Fully Meets 
Score 4: Highly meets 
Score 3: Moderately Meets 
Score 2: Slightly meets 
Score 1: Fails to meet 

"""

overall_subtopic_qualityt_short = """ Considering all factors (relevance, engagement, and other factors that were not covered by our questions), what is the overall quality and utility of the system's performance for this subtopic? 
The overall quality and utility of system is rated with an integer score betwen 1-5. Each score has the following meanings:

Score 5: Exceptional 
Score 4: Good 
Score 3: Acceptable 
Score 2: Poor 
Score 1: Unacceptable 

"""

rater_confidencet_short = """ How confident are you in the scores you provided for this sub-topic? 

Score 3: High Confidence 
Score 2: Medium Confidence
Score 1: Low Confidence
"""

mixed_initiative_strategiest_short = """An effective proactive system employs a variety of strategies while interacting with the user, e.g., it asks clarifying questions, or tries to elicit the user’s preference by asking questions and would ask follow-up questions to make user more engaged in the dialogue. 
How well does the system employ a portfolio of different proactive actions (e.g., asking clarifying questions, asking follow-up questions, asking for feedback, etc.) throughout the conversation?


Score 5: Masterfully proactive assistant 
Score 4: Competent & Proactive 
Score 3: Limited but Functional 
Score 2: Attempted but Flawed 
Score 1: Purely Reactive 
"""

personalizationt_short = """An effective personalized system should appropriately tailor its responses to the user persona when necessary. The personalization aspects have two dimensions: style and content. Style refers to the tone, detail and vocabulary that is familiar to the user, while content refers to understanding the user’s interest and constraints while providing the answer (e.g., if the user is vegan, avoid suggesting cow’s milk to them). 
How well does the system tailor the dialogue to the specific user persona provided?


Score 5: Deeply Personalized 
Score 4: Successfully Personalized 
Score 3: Superficially Personalized 
Score 2: Incorrectly Personalized 
Score 1: Entirely Generic 
"""

information_flow_and_coherencet_short = """An effective information flow refers to a reasonable information rate while providing the response to the user. An effective system would try to scaffold the information and provide the response in hierarchical order (i.e., start with high-level concepts and then go in more detail with the more specific aspects of the topic). It would also try to adapt the information rate to the user’s understanding of the topic, i.e., to avoid throwing a lot of information to the user all at once. Moreover, the system should avoid unnecessary verbosity, contradiction, repetition, and abrupt topic shifts in different turns. 

Score 5: Seamless & Logical 
Score 4: Coherent with Minor Flaws 
Score 3: Functional but Clunky 
Score 2: Disjointed & Confusing 
Score 1: Incoherent 
"""

trustworthinesst_short = """After examining the whole dialog, how likely would you be to believe that past and future answers of this system are factually correct? A trustworthy system is transparent about its source of knowledge (e.g., where was conveyed knowledge obtained from), refer to domain expert on sensible topics (e.g., physicians on medical topics), and transports appropriate levels of confidence. 
Please also consider other factors that contribute to your perceived trustworthiness in your rating. 


Score 5: Exemplary 
Score 4: Reliable 
Score 3: Inconsistent 
Score 2: Unreliable 
Score 1: Actively Misleading 
"""

overall_user_satisfactiont_short = """Considering the entire dialogue, how satisfied would you be as the user and how successful was the interaction? Would you use this system yourself? 
Bear in mind that the current user is a simulated user, and therefore its language might not reflect actual user satisfaction and system performance (e.g., “Thank you very much for your great answer”).


Score 5: Task Perfected 
Score 4: Task Accomplished 
Score 3: Task Partially Met 
Score 2: Task Failed 
Score 1: Task Undermined 
"""


