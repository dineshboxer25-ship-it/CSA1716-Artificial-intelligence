
% Best First Search Algorithm

% Graph connections
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, g).
edge(e, g).

% Heuristic values
heuristic(a, 5).
heuristic(b, 3).
heuristic(c, 2).
heuristic(d, 2).
heuristic(e, 1).
heuristic(g, 0).

% Best First Search
best_first(Start, Goal, Path) :-
    search(Start, Goal, [Start], RevPath),
    reverse(RevPath, Path).

search(Goal, Goal, Path, Path).

search(Current, Goal, Visited, Path) :-
    Current \= Goal,
    edge(Current, Next),
    \+ member(Next, Visited),
    heuristic(Next, _),
    search(Next, Goal, [Next | Visited], Path).
