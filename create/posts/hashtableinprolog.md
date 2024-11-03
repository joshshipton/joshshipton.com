ID="99491"
TITLE="hash table from scratch in prolog (boo)"
LINK="hashtable-in-prolog"
IS_DRAFT=F
IS_POPULAR=T
----------

i'm currently taking [knowledge representation](https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning) at university, a core part of this unit is logic programming for which we use [Prolog](https://en.wikipedia.org/wiki/Prolog). i seriously dislike Prolog as a programming language. i find it unnatural to work with and it's quirks irritate me. but this definitely a skill issue (see below image) in an attempt to try to mend my broken relationship with the language i decided to build a data structure from scratch in it (aka procrastinate from actually studying for my exams). i chose hash maps because theyre easy to understand, i like them and O(1) insertion and retrieval time is sexy.

<img class="center" src="https://rdxhiwxfooidvexdrgxs.supabase.co/storage/v1/object/public/images/skill-issue-always.jpg" alt="everything is a skill issue"></img>

before i dive into my hash table here are some of my FAVORITE Prolog quirks /s

### "=" is different

```prolog
% = is for unification, not assignment
X = 5.         % Unifies X with 5

% is is for arithmetic evaluation
Sum is 2 + 3.  % Evaluates 2 + 3 and unifies Sum with 5

% =:= for arithmetic equality
5 =:= 2 + 3.   % true
5 = 2 + 3.     % false! Because it doesnt evaluate 2 + 3
```

### no loops, everything is recursive (this one is my least favorite)

```prolog
print_numbers(0).
print_numbers(N) :-
    N > 0,
    write(N), nl,
    N1 is N - 1,
    print_numbers(N1).
```


### negation as failure

```prolog
% Let's define some simple facts
likes(john, pizza).
likes(mary, sushi).
likes(john, sushi).

% You might think this would work to find who doesn't like pizza:
find_pizza_hater(Person) :-
    \+ likes(Person, pizza). % "\+" is the negation operator

% But this fails:
% ?- find_pizza_hater(mary).
% false    <-- confusion??

% You need this thing instead:
find_pizza_hater(Person) :-
    likes(Person, _),         % first find a person that exists
    \+ likes(Person, pizza).  % then check if they don't like pizza

% This works:
% ?- find_pizza_hater(mary).
% true
```

<br>

# <div class="center"> ~~~ hash table time ~~~ </div>
<br>

ok now lets start with the hashtable, i think this will be easiest if we break the code down into it's main parts.

### the basics of our hash table

```prolog
:- dynamic hash_bucket/3.  % stores (hash value, key, value)
:- dynamic table_size/1.   % keeps track of table size
:- dynamic item_count/1.   % counts our stuff
```

this tells prolog "hey, these things are gonna change while we run". think of it like creating variables that can actually change (which is weird in prolog). the /3 and /1 just mean how many parameters each one takes.


### initialization (setting up our table)
```prolog
init_hash_table(size) :-
    retractall(hash_bucket(_, _, _)),    % clear any old junk
    retractall(table_size(_)),           % out with the old size
    retractall(item_count(_)),           % reset our counter
    assertz(table_size(size)),           % set new size
    assertz(item_count(0)).              % start fresh at 0
```

this is like our constructor. retractall is basically "delete everything matching this pattern" and assertz is "add this new fact". the _ is prolog for "i don't care what this value is".

### the hash function (where the magic happens)

```prolog
hash_function(key, size, hashvalue) :-
    string_codes(key, codes),            % convert string to ascii numbers
    sum_codes(codes, sum),               % add them up
    a is 0.69420,                        % completely arbitrary constant...
    product is sum * a,                  % multiply
    fractional is product - floor(product), % get decimal part
    hashvalue is floor(size * fractional). % scale to table size
```

this is our hash function - nothing too fancy, just:
converts string to ascii numbers -> adds them up -> multiplies them by a completely random constant -> takes the decimal part and scales it to fit our table size


### handling collisions

prolog actually makes this super easy. when multiple items hash to the same spot, they just... exist there. the backtracking system handles it automatically. when we look something up:

```prolog
get(key, value) :-
    table_size(size),
    hash_function(key, size, hashvalue),
    hash_bucket(hashvalue, key, value).  % magic happens here
prolog will find the right one automatically by matching both the hash AND the key.
```

### load factor and resizing

```prolog
check_load_factor :-
    item_count(count),
    table_size(size),
    loadfactor is count / size,
    (loadfactor > 0.7 ->                 % if too full
        resize_table                     % make it bigger
    ;   true                            % else do nothing
    ).
```
when the table gets too full (>70%), we: double the size, grab all our current items and  rehash everything into the bigger table

### the recursive parts (because prolog)

```prolog
rehash_all([]).                          % base case: empty list = done
rehash_all([key-value|rest]) :-          % for each item:
    table_size(size),
    hash_function(key, size, newhash),   % get new position
    assertz(hash_bucket(newhash, key, value)),
    rehash_all(rest).                    % do the rest
```
this is classic prolog recursion:

base case: empty list? doneski
otherwise: handle first item, then recurse on the rest

testing it out:

```prolog
main :-
    init_hash_table(10),
    insert("key1", value1),
    insert("meaning_of_life", 42),
    % ... more insertions ...
    print_stats.
```

and that's our hash table!

here's the implementation in it's entirety. is it the most efficient implementation ever? probably not. but its cool how working with prolog can lead to a decent outcome.

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


cool prolog features that make this work:

- automatic backtracking: helps with collisions
- dynamic predicates: lets us modify the table
- pattern matching: makes lookups clean
- recursion: because prolog loves recursion
- fact-based storage: using prolog's database-like features


