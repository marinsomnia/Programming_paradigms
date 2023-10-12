% Правило для вычисления суммы элементов пустого списка
sum_list([], 0).

% Правило для вычисления суммы элементов непустого списка
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.