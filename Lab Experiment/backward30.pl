
% Backward Chaining Program

% Facts
parent(john, mary).
parent(mary, alice).
parent(john, peter).

% Rule: Grandparent
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

% Rule: Ancestor
ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
