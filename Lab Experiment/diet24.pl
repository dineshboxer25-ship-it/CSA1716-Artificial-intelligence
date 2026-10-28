
% Diet Suggestion Based on Disease

diet(diabetes, 'Balanced meals with controlled carbohydrates').
diet(hypertension, 'Limit excess salt in food').
diet(anemia, 'Include iron-rich foods').
diet(obesity, 'Choose balanced portions and nutritious foods').

% Rule to suggest diet
suggest_diet(Disease, Advice) :-
    diet(Disease, Advice).
