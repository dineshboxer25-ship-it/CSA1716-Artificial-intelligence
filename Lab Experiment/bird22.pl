
% Bird facts and flying rules

bird(sparrow).
bird(parrot).
bird(penguin).
bird(ostrich).

can_fly(X) :-
    bird(X),
    not(flightless(X)).

flightless(penguin).
flightless(ostrich).
