ID="99491"
TITLE="hash table from scratch in prolog (boo)"
LINK="hashtable-in-prolog"
IS_DRAFT=F
IS_POPULAR=F
----------

I'm currently [knowledge representation](https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning) at university, a part of this unit is logic programming for which we use [Prolog](https://en.wikipedia.org/wiki/Prolog). I seriously dislike Prolog as a programming language. i find it unnatural to work with and it's quirks irritate me. but this definitely a skill issue (see below image) in an attempt to try to mend my broken relationship with the language i decided to build a data structure from scratch in it (aka procrastinate from actually studying for my exams). i chose hash maps because theyre easy to understand, i like them and O(1) insertion and retrieval time is sexy.

<img class="center" src="https://rdxhiwxfooidvexdrgxs.supabase.co/storage/v1/object/public/images/skill-issue-always.jpg" alt="everything is a skill issue"></img>

before I dive into my hash table here are some of my FAVORITE Prolog quirks /s

1. = is different
```prolog
% = is for unification, not assignment
X = 5.         % Unifies X with 5

% is is for arithmetic evaluation
Sum is 2 + 3.  % Evaluates 2 + 3 and unifies Sum with 5

% =:= for arithmetic equality
5 =:= 2 + 3.   % true
5 = 2 + 3.     % false! Because it doesn't evaluate 2 + 3
```

2. order matters a lot
```prolog
% This will work fine
good_factorial(0, 1).
good_factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    good_factorial(N1, SubResult),
    Result is N * SubResult.

% This will cause infinite recursion
bad_factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    bad_factorial(N1, SubResult),
    Result is N * SubResult.
bad_factorial(0, 1).
```

3. no loops, everything is recursive (this one is my least favorite)

```prolog
print_numbers(0).
print_numbers(N) :-
    N > 0,
    write(N), nl,
    N1 is N - 1,
    print_numbers(N1).
```


The implementation leverages several unique features of Prolog's logical programming paradigm. Dynamic predicates are used to create mutable state, which isn't typically associated with Prolog's declarative nature. The collision handling is particularly elegant in Prolog - it uses the language's built-in backtracking mechanism to naturally handle multiple items at the same hash position. Memory management takes advantage of Prolog's database-like structure with assertz for adding facts and retractall for cleaning up old entries. The dynamic resizing implementation showcases how Prolog can maintain complex data structures, growing the table when the load factor exceeds 0.7 and using recursive predicates to rehash all items to their new positions. Performance monitoring is implemented through Prolog's fact-based system, tracking the number of items and calculating statistics. This combination of logical programming concepts with traditional data structure implementation demonstrates how Prolog, despite its quirks, can be used to create efficient and maintainable data structures.

AND HERE IT IS.

```prolog
% tell prolog these predicates will change during runtime
:- dynamic hash_bucket/3.  % stores triplets of (hash value, key, value)
:- dynamic table_size/1.   % keeps track of how big our table is
:- dynamic item_count/1.   % counts how many items we've stored

% sets up a fresh hash table with a given size
init_hash_table(size) :-
    retractall(hash_bucket(_, _, _)),    % clear out any old data
    retractall(table_size(_)),           % remove old size
    retractall(item_count(_)),           % reset item counter
    assertz(table_size(size)),           % set new table size
    assertz(item_count(0)).              % start with zero items

% our hash function - converts keys into table positions
hash_function(key, size, hashvalue) :-
    string_codes(key, codes),            % convert string to ascii numbers
    sum_codes(codes, sum),               % add up all the ascii values
    a is 0.69420,                        % pick a fun decimal number
    product is sum * a,                  % multiply sum by our number
    fractional is product - floor(product), % get just the decimal part
    hashvalue is floor(size * fractional). % scale to fit table size

% adds up a list of ascii codes recursively
sum_codes([], 0).                        % empty list sums to zero
sum_codes([code|rest], sum) :-           % for non-empty list:
    sum_codes(rest, restsum),            % sum up the rest
    sum is code + restsum.               % add current code to sum

% puts a new key-value pair into the hash table
insert(key, value) :-
    table_size(size),                    % get current table size
    hash_function(key, size, hashvalue), % calculate where to put it
    retractall(hash_bucket(hashvalue, key, _)), % remove old value if any
    assertz(hash_bucket(hashvalue, key, value)), % store new value
    update_count(1),                     % increment item counter
    check_load_factor.                   % see if table needs to grow

% finds the value associated with a key
get(key, value) :-
    table_size(size),                    % get table size
    hash_function(key, size, hashvalue), % calculate position
    hash_bucket(hashvalue, key, value).  % look up the value

% removes a key-value pair from the table
remove(key) :-
    table_size(size),                    % get table size
    hash_function(key, size, hashvalue), % find where it should be
    retract(hash_bucket(hashvalue, key, _)), % remove it
    update_count(-1).                    % decrease item count

% updates the count of items in the table
update_count(delta) :-
    retract(item_count(count)),          % get current count
    newcount is count + delta,           % adjust it
    assertz(item_count(newcount)).       % store new count

% checks if the table is getting too full
check_load_factor :-
    item_count(count),                   % get number of items
    table_size(size),                    % get table size
    loadfactor is count / size,          % calculate fullness
    (loadfactor > 0.7 ->                 % if more than 70% full
        resize_table                     % make table bigger
    ;   true                            % otherwise do nothing
    ).

% makes the table bigger when it gets too full
resize_table :-
    table_size(oldsize),                 % get current size
    newsize is oldsize * 2,              % double it
    findall(key-value,                   % collect all current items
            (hash_bucket(_, key, value)),
            pairs),
    retractall(hash_bucket(_, _, _)),    % clear the table
    retractall(table_size(_)),           % update size
    assertz(table_size(newsize)),
    rehash_all(pairs).                   % put items back in new spots

% puts all items back after resizing
rehash_all([]).                          % done if no items left
rehash_all([key-value|rest]) :-          % for each item:
    table_size(size),                    % get new table size
    hash_function(key, size, newhash),   % calculate new position
    assertz(hash_bucket(newhash, key, value)), % store it
    rehash_all(rest).                    % handle remaining items

% shows current table statistics
print_stats :-
    item_count(count),                   % get number of items
    table_size(size),                    % get table size
    loadfactor is count / size,          % calculate fullness
    format('table size: ~w~n', [size]),
    format('item count: ~w~n', [count]),
    format('load factor: ~2f~n', [loadfactor]).

% prints all items in the table
print_all :-
    hash_bucket(hash, key, value),       % find each item
    format('hash: ~w, key: ~w, value: ~w~n',
           [hash, key, value]),          % print it
    fail.                                % backtrack to find more
print_all.                               % succeed when done

% test the implementation
main :-
    init_hash_table(10),
    insert("key1", value1),
    insert("meaning_of_life", 42),
    insert("first_prime", 2),
    insert("random", 3498),
    remove("key1"),
    print_all,
    print_stats,
    remove("first_prime"),
    print_all,
    print_stats.

% tell prolog to run main when loaded
:- initialization(main).
```