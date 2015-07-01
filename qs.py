Questions:

	Questions:
		1.  - Given a well-formed binary tree, implement an iterator that
		iterates over it in in-order fashion. The idea is not to print the
		complete inorder traversal in one go, but to be able to call next() like
		in STL iterators to get the next node.
		2.  -  Do (1) for Post-order.
		3.  - Longest Path in a Binary Tree. - 
		4.  - Lowest Common Ancestor of a _Binary_ Tree (not BST).
		5.  - Given a binary tree made of these nodes, convert it, in-place
		(i.e. don't allocate new Nodes), into a circular doubly linked list in
		the same order. That is, a traversal of the linked list and an inorder
		traversal of the tree should yield the elements in the same order. You
		should return the head of the linked list.
		The Node looks like:
		struct Node {
			  int data;
			    struct Node *left;
				   struct Node *right;
		}
		6. COULD NOT DO - Implement a non-blocking circular queue of bytes.
		Reads can be of arbitrary length (but should return the max available),
		writes can be of arbitrary length (but should return the bytes actually
		written). More or less, the API is exactly the same as a non-blocking
		queue. 
		7.  - Given a sequence of positive integers 'seq' and an integer
		'total', return whether a contiguous sequence of 'seq' sums up to
		'total'.
		8.  - An address book contains a list of contacts which were imported
		from different sources (i.e. Facebook, LinkedIn). Each contact has 1 or
		more email addresses. Write a function to group all contacts which share
		any email together.
		Input
		  C1: shuw@oo.com, shu@gmail.com
		    C2: bob@oo.com
			   C3: shu@gmail.com, shuwu@yahoo.com
				  C4: shuwu@yahoo.com
				    C5: bob@oo.com
					   C6: jamie@oo.com
						[edit] Output
						  ((C1, C3, C4), (C2, C5), (C6))
						    (C1, C3, C4) are in the same subset because they likely
							 represent the same person. Ditto for the other subsets.
							   Notice that each contact can appear in only one
								subset.
								9.  - We have a coding system from alphabets to
								numbers where a=1, b=2, ...z=26. You are given a
								string of digits as an input. Write a function that
								will compute the number of valid interpretations of
								the input.
								10. VAGUE - Compare two dates.
								11.  - Write a method called drawCircle(r) which draws
								a circle of radius 'r', given a method called plot(x,
								y), which plots a dot at (x, y).
								12.  - You have an array of values. Each value in the
								array can be described as falling into one of three
								categories: "low", "medium", and "high". You want to
								sort the array using these categories. How do you do
								it? Assume methods like 'islow(x)', 'ismedium(x)',
								'ishigh(x)' etc.
								13.  - Given a class representing a sequence, write a
								function that takes two sequences and returns true if
								the sequences differ in exactly one way: one has an
								added value, one has a removed value, or the same
								position in both sequences is different. You can only
								ask for the next value of a sequence once, cannot
								backtrack, and don't have enough memory to buffer
								either sequence. It is valid to track current and
								previous values.
								Eg. f({1,2,3,0}, {1,2,3,4,0}) == true
								f({1,2,3,0}, {1,2,4,5,0}) == false
								14. Write a function in C that distinguishes the
								endianess of the architecture. It should return true
								in one case and false in the other.
								15. -  Implement a function to output the nth value in
								the fibanocci sequence.
								16.  - You have an array with N elements and you
								should find two elements with given sum K.
								 

								 There might be duplicate questions. If yes, then say
								 which previous question that you have  is this new
								 question a copy of.

								 1.  In a game where you can score 2 points, 3 points
								 or 7 points at a time, write a function that turns an
								 arbitrary score into the list of possible ways the
								 score could have been reached.
								 2.  Given a number like 1212, translate it into the
								 English string "One thousand two hundred and twelve".
								 3.  Your code is stored in a revision control system
								 (e.g. svn). You see a bug in your code, and you know
								 it wasn't there before. Write a function to find the
								 revision that introduced the bug.
								 For example:
								 revision 123 <-- good
								 revision 124
								 ...
								 revision ??? <-- introduced the bug
								 ...
								 revision 544
								 revision 545 <-- bad
								 You are given a known good revision and a known bad
								 revision. In addition, you have a function that can
								 tell you whether a specified revision is good or bad.
								 (In C, it would be something like: bool
								 isBad(unsigned int revision).)
								 4. Iterate over a singly linked list backwards. Call
								 print on each node.
								 5.  Determine if any 3 integers in an array sum to 0.
								 6.  A VARIATION 
								 https://github.com/priyanka-m/programming_practice/blob/master/minJumps.cpp
								 Write a function that returns the minimum number of
								 jumps the knight must make to reach the destination.

								 - - - - - - - -
								  - - - - - - D -
								   - - - p 1 - - -
									 - - - - - p - -
									  - - - N - - - -
									   - - - - - - - -
										 - - - - - - - -
										  - - - - - - - -
										  N: knight
										  p: obstacle/pawn
										  1: reachable in 1 jump
										  D: destination, reachable in 2 jumps
										  7.  Given a list of n (where n ≈ 1,000,000)
										  points in 3D space, return the k (where k ≈
										  1,000) closest points to the origin.
										  8. The problem is to flatten a linked list
										  where the elements can be either atomic types
										  or other lists. 
										  In other words, the return value should be the
										  atomic values found through a DFS traversal of
										  the original list. 
										  Eg.,
										  Input: 1->(2.1->2.2->2.3)->3->(4.1->4.2)
										  Output: 1->2.1->2.2->2.3->3->4.1->4.2
										  (The second and fourth elements in the list
										  are lists themselves.)

										  First think how this problem can be  if you
										  could allocate new memory. Then do it
										  'in-place' (without allocating new memory).
										  9. Implement the following function:
										  vector<string> listPattern(const string&
										  pattern);
										  where "pattern" is a unix file system pathname
										  with wildcats, e.g., "/a/*/b/*/c". Each
										  component in the path is either a fully
										  qualified name e.g., "a", or a single wildcat
										  "*". No need to worry about combinations of
										  wildcats and non wildcats, e.g., "a*b".
										  Returns the list of file or directory names in
										  the file system that match the given pattern.
										  Available library functions to use (in
										  addition to the common string processing
										  functions):
										  vector<string> listPath(const string& path);
										  where "path" must be a fully qualified
										  pathname. Returns a vector with only "path" in
										  it if "path" is the name of a file. Returns a
										  vector with the names of child files or
										  directories if "path" is the name of a
										  directory. Returns an empty vector if no file
										  or directory with the name "path" exists in
										  the file system.
										  bool exists(const string& path);
										  Returns true iff a file or directory with the
										  name "path" exists in the file system.
										  10.  Implement a function to output the
										  look_and_say sequence.
										  1
										  11
										  21
										  1211
										  111221
										  312211
										  13112221
										  1113213211
										  31131211131221
										  13211311123113112211

										  -> Also, what is the only starting sequence
										  that never grows in length
										  11.  Given two input strings representing
										  arbitrary large (positive) integers, how to
										  compute the result of their multiplication?
										  For instance, the result of
										  "12345678987654321" multiplied by
										  "123456789123456789" is
										  "1524157887364730998475842112635269".
										   1524157777364730998475842112635269
											12. 
											i) Given 2 interval ranges, create a function
											to tell me if these ranges intersect. Both
											start and end are inclusive: [start, end]
											ii) Given 2 interval ranges that intersect,
											now create a function to merge the 2 ranges
											into a single continuous range.
											iii) Now create a function that takes a group
											of unsorted, unorganized intervals, merge any
											intervals that intersect and sort them. The
											result should be a group of sorted,
											non-intersecting intervals.
											iv) Now create a function to merge a new
											interval into a group of sorted,
											non-intersecting intervals. After the merge,
											all intervals should remain non-intersecting.
											You are given the function definition below.
											void merge(vector<Range> & existing, Range
											newInterval);
											13.  Given an integer n, determine if there
											is some arrangement of n queens on an n-by-n
											chessboard such that no queens attacks
											another queen.
											14. Write a comparator function that can be
											used to sort an array of strings in natural
											order.
											For example:
											["a1", "a2", "a11", "a10"] should sort to
											["a1", "a2", "a10", "a11"] andnot the default
											lexicographical ["a1", "a10", "a11", "a2"] 
											15. Given a dictionary, find all pairs of
											words that, when concatenated together, form
											a palindrome. For instance, in English we
											would be looking for pairs like (cigar,
											tragic); (none, xenon); (warrener, raw);
											(rotatively, levitator); (redrawer;
											rewarder).

											,
											1. Check if a string is a palindrome where
											strings are almost the same (cases might be
											different, there might be punctuations etc.)
											Eg. "A man, a plan, a canal, Panama!" is a
											palindrome.
											2. Did not understand Write a function thats
											takes an input string and returns the minimum
											substring which contains every letter of the
											alphabet at least once.
											Example:
											Input: "aaccbc"
											Alphabet: "abc"
											Output: "accb"
											3.  Implement atof. For example, "-12.82e-2L"
											is parsed to the appropriate float.
											4.  Imagine a robot sitting on the upper left
											hand corner of an NxN grid. The robot can
											only move in two directions: right and down.
											How many possible paths are there for the
											robot to (N,N)? Then imagine certain cells to
											be off limits.
											5.  Describe and then write a function ththe
											method would generate this (in no particular
											order):at generates the permutations of the
											characters in a string. For example, if the
											input is:
											abc
											the method would generate this (in no
											particular order):
											abc
											acb
											bac
											bca
											cab
											cba
											6.  You overhear someone say their password
											out loud (such as "myspace") but you know
											they are clever enough to use some
											substitutions. Any letter could be
											capitalized or replaced with it's l337 speak
											equivalent (y => 4, a => @, e => 3). Print
											all possible password permutations to screen
											7. You are given n integer intervals [a_i,
													b_i] on the real axes, and the absolute
											value of the coordinates is bounded by M.
											Determine a point that belongs to the maximum
											number of intervals. Point x belongs to the
											interval [a, b] iff a <= x <= b.
											8.  You are given an array of unique prime
											numbers, e.g. [2,11,3]. Write a function to
											print out all possible products that you can
											make from these numbers (including the
													individual numbers themselves). Order
											doesn't matter. In this case, you'd print out
											the numbers: 2, 11, 3, 22, 66, 33, 6

											Then also handle the case when the array has
											non-unique elements like [2, 11, 3, 2].
											Ensure that you don't print duplicates. 
											9.  Given an array of integers, return the
											position of the maximum element. If the
											maximum element occurs multiple times, use a
											random number generator to choose one of the
											positions uniformly at random.
											10.  
											Part 1
											For a given a binary tree, print paths from
											root to all leaf nodes, one path per line.
											This is basically a depth-first-traversal
											with "seen-so-far" memory. For example, for
											this tree:
											         A
														        / \
																		         B   C
																					      /   / \
																									     D
																										  E
																										  F
																										  The
																										  expected
																										  output
																										  is:
																										  ABD
																										  ACE
																										  ACF

																										  Part
																										  2
																										  could
																										  not
																										  do
																											  Code
																											  the
																											  question
																											  when
																											  given
																											  a
																											  directed
																											  graph
																											  that
																											  may
																											  include
																											  cycles,
																											  and
																											  to
																											  print
																											  all
																											  paths
																											  from
																											  a
																											  starting
																											  node
																											  to
																											  terminal
																											  nodes
																											  (i.e.
																											  nodes
																											  with
																											  an
																											  empty
																											  set
																											  of
																											  exiting
																											  edges).
																											  The
																											  important
																											  part
																											  at
																											  this
																											  stage
																											  is
																											  to
																											  ask
																											  them
																											  to
																											  think
																											  about
																											  time
																											  complexity
																											  correctly,
																											  to
																											  probe
																											  their
																											  data
																											  structure
																											  decisions,
																											  and
																											  to
																											  identify
																											  a
																											  worst
																											  case
																											  directed
																											  graph,
																											  which
																											  may
																											  look
																											  like
																											  this:
																											      A
																													   /
																														\
																																  B
																																  C
																																     \
																																			  /
																																			      D
																																					   /
																																						\
																																								  E
																																								  F
																																								     \
																																											  /
																																											      G

																																													11.
																																													You
																																													are
																																													given
																																													an
																																													array
																																													of
																																													strings
																																													(a
																																													dictionary).
																																													The
																																													task
																																													is
																																													to
																																													implement
																																													two
																																													functions.
																																													The
																																													first
																																													is
																																													setup(),
																																													which
																																													preprocesses
																																													the
																																													dictionary
																																													to
																																													your
																																													liking.
																																													The
																																													second
																																													is
																																													isMember(),
																																													that,
																																													given
																																													a
																																													word,
																																													returns
																																													whether
																																													or
																																													not
																																													the
																																													word
																																													exists
																																													in
																																													the
																																													dictionary.
																																														[edit]
																																														Setting
																																														up
																																														the
																																														question

																																															Example:
																																																setup({"foo",
																																																"bar",
																																																"baz",
																																																NULL});
																																																	isMember("foo");
																																																	//returns
																																																	//true
																																																		isMember("garply");
																																																		//returns
																																																		//false
																																																		12.
																																																		select
																																																		the
																																																		kth
																																																		largest/smallest
																																																		element
																																																		in
																																																		an
																																																		unsorted
																																																		array
																																																		of
																																																		elements.
																																																		13.
																																																		You
																																																		have
																																																		an
																																																		array
																																																		of
																																																		N
																																																		integers.
																																																		There
																																																		are
																																																		M
																																																		contiguous
																																																		segments
																																																		that
																																																		are
																																																		sorted
																																																		within
																																																		the
																																																		segment,
																																																		but
																																																		the
																																																		whole
																																																		array
																																																		is
																																																		not
																																																		sorted.
																																																		N
																																																		>> M.
																																																		>> How
																																																		>> to
																																																		>> produce
																																																		>> a
																																																		>> sorted
																																																		>> version
																																																		>> of
																																																		>> this
																																																		>> array?
																																																		[1,3,5,2,4,6,10,20,30,11,12,23]
																																																		14.
																																																		You
																																																		have
																																																		N
																																																		arrays
																																																		of
																																																		sorted
																																																		integers.
																																																		On
																																																		average
																																																		each
																																																		array
																																																		has
																																																		M
																																																		elements.
																																																		How
																																																		to
																																																		find
																																																		the
																																																		median
																																																		of
																																																		all
																																																		these
																																																		numbers
																																																		[[1,3,5],
																																																		[2,4,6],
																																																		[10,20,30],
																																																		[11,12,23]]
																																																		15.
																																																		Given
																																																		a
																																																		linked
																																																		list,
																																																		write
																																																		a
																																																		function
																																																		to
																																																		reverse
																																																		every
																																																		alternate
																																																		k
																																																		nodes
																																																		(where
																																																		k
																																																		is
																																																		an
																																																		input
																																																		to
																																																		the
																																																		function)
																																																		in
																																																		an
																																																		efficient
																																																		way.
																																																		Give
																																																		the
																																																		complexity
																																																		of
																																																		your
																																																		algorithm.

																																																		Example:
																																																		Inputs:
																																																		1->2->3->4->5->6->7->8->9->NULL
																																																		and
																																																		k
																																																		=
																																																		3
																																																		Output:
																																																		3->2->1->4->5->6->9->8->7->NULL. 
																																																		16.
																																																		Given
																																																		a
																																																		string
																																																		and
																																																		a
																																																		dictionary
																																																		of
																																																		valid
																																																		words,
																																																		determine
																																																		if
																																																			you
																																																			could
																																																			insert
																																																			zero
																																																			or
																																																			more
																																																			spaces
																																																			into
																																																			the
																																																			string
																																																			such
																																																			that
																																																			the
																																																			resulting
																																																			string
																																																			would
																																																			be
																																																			composed
																																																			entirely
																																																			of
																																																			valid
																																																			words.

																																																			Example:
																																																			bedbathandbeyond
																																																			=>
																																																			breakable
																																																			since
																																																			["bed",
																																																			"bath",
																																																			"and",
																																																			"beyond"]
																																																			or
																																																			["bed",
																																																			"bat",
																																																			"hand",
																																																			"beyond"]
																																																			17.
																																																			You
																																																			are
																																																			given
																																																			a
																																																			search
																																																			trie
																																																			that
																																																			represents
																																																			an
																																																			arbitrary
																																																			block
																																																			of
																																																			text.
																																																			In
																																																			the
																																																			trie,
																																																			each
																																																			node
																																																			represents
																																																			exactly
																																																			one
																																																			character.
																																																			Implement
																																																			a
																																																			function
																																																			that,
																																																			given
																																																			a
																																																			word,
																																																			returns
																																																			whether
																																																			or
																																																			not
																																																			the
																																																			word
																																																			exists
																																																			in
																																																			the
																																																			trie.
																																																			Your
																																																			function
																																																			must
																																																			support
																																																			a
																																																			wildcard
																																																			character,
																																																			which
																																																			represents
																																																			any
																																																			single
																																																			character.
																																																			Example:
																																																			"peak"
																																																			matches
																																																			"peak"
																																																			"p**k"
																																																			matches
																																																			"peak",
																																																			"perk",
																																																			"park",
																																																			etc.

																																																			Here
																																																			is
																																																			a
																																																			struct
																																																			definition
																																																			for
																																																				a
																																																				node
																																																				that
																																																				works
																																																				for
																																																					both
																																																					binary
																																																					trees
																																																					and
																																																					doubly-linked
																																																					lists:
																																																					struct
																																																					Node
																																																					{
																																																						  int
																																																						  data;
																																																						    struct
																																																							 Node
																																																							 *left;
																																																							   struct
																																																								Node
																																																								*right;
																																																					}
																																																					18.
																																																					before
																																																					Given
																																																					a
																																																					binary
																																																					tree
																																																					made
																																																					of
																																																					these
																																																					nodes,
																																																					convert
																																																					it,
																																																					in-place
																																																					(i.e.
																																																					don't
																																																					allocate
																																																					new
																																																					Nodes),
																																																					into
																																																					a
																																																					circular
																																																					doubly
																																																					linked
																																																					list
																																																					in
																																																					the
																																																					same
																																																					order.
																																																					That
																																																					is,
																																																					a
																																																					traversal
																																																					of
																																																					the
																																																					linked
																																																					list
																																																					and
																																																					an
																																																					inorder
																																																					traversal
																																																					of
																																																					the
																																																					tree
																																																					should
																																																					yield
																																																					the
																																																					elements
																																																					in
																																																					the
																																																					same
																																																					order.
																																																					You
																																																					should
																																																					return
																																																				the
																																																				head
																																																				of
																																																				the
																																																				linked
																																																				list.
																																																				[edit]
																																																				19.
																																																				/**
																																																				 * Given
																																																				 * a
																																																				 * string,
																																																				 * returns
																																																				 * a
																																																				 * string
																																																				 * with
																																																				 * the
																																																				 * order
																																																				 * of
																																																				 * the
																																																				 * words
																																																				 * reversed.
																																																				  * For
																																																				  * example,
																																																				  * "dog
																																																				  * bites
																																																				  * man"
																																																				  * becomes
																																																				  * "man
																																																				  * bites
																																																				  * dog"
																																																				   */
																																																					20.
																																																					Write
																																																					a
																																																					simple
																																																					regex
																																																					verifier.
																																																					The
																																																					regex
																																																					patterns
																																																					to
																																																					match
																																																					are
																																																					a-z
																																																					.
																																																					* Where
																																																					* <dot>
																																																					* stands
																																																					* for
																																																					* any
																																																					* character,
																																																					* and
																																																					* <star>
																																																					* means
																																																					* the
																																																					* previous
																																																					* rule
																																																					* 0
																																																					* or
																																																					* more
																																																					* times.
																																																					* The
																																																					* regex
																																																					* must
																																																					* match
																																																					* the
																																																					* entire
																																																					* string,
																																																					* not
																																																					* a
																																																					* substring.
																																																					21.
																																																					Given
																																																					a
																																																					set
																																																					of
																																																					basic
																																																					operations,
																																																					the
																																																					Minimum
																																																					Edit
																																																					Distance
																																																					between
																																																					two
																																																					strings
																																																					is
																																																					defined
																																																					as
																																																					the
																																																					minimum
																																																					number
																																																					of
																																																					operations
																																																					you
																																																					have
																																																					to
																																																					perform
																																																					on
																																																					one
																																																					string
																																																					to
																																																					get
																																																					the
																																																					other.
																																																					Set
																																																					of
																																																					basic
																																																					operations
																																																					is:
																																																					Add
																																																					a
																																																					character
																																																					Remove
																																																					a
																																																					character
																																																					Replace
																																																					a
																																																					character

																																																					eg.
																																																					minEditDistance("abcd",
																																																					"abd")
																																																					=
																																																					1 
																																																					22.
																																																					The
																																																					question:
																																																						Given
																																																						predicted
																																																						stock
																																																						prices
																																																						for
																																																							next
																																																							n
																																																							days
																																																							for
																																																								a
																																																								stock
																																																								e.g
																																																								:
																																																									20,
																																																									40,
																																																									52,
																																																									15,
																																																									30,
																																																									50,
																																																									10,
																																																									25
																																																									find
																																																									the
																																																									maximum
																																																									profit
																																																									that
																																																									can
																																																									be
																																																									made
																																																									with
																																																									a
																																																									single
																																																									buy-sell
																																																									transaction.
																																																									If
																																																									no
																																																									profit
																																																									can
																																																									be
																																																									made
																																																									return
																																																								0.
																																																								In
																																																								the
																																																								example
																																																								buying
																																																								at
																																																								15
																																																								and
																																																								selling
																																																								at
																																																								50
																																																								gives
																																																								maximum
																																																								profit.
																																																								Note
																																																								that
																																																								the
																																																								two
																																																								prices
																																																								are
																																																								neither
																																																								minimum
																																																								nor
																																																								maximum
																																																								in
																																																								the
																																																								array.
																																																								23.
																																																								Given
																																																								a
																																																								Roman
																																																								numeral,
																																																								eg
																																																								"MCMVIII",
																																																								write
																																																								a
																																																								function
																																																								which
																																																								outputs
																																																								the
																																																								integer
																																																								equivalent,
																																																								eg
																																																								1908.
																																																								('M'
																																																								=>
																																																								1000,
																																																								'C'
																																																								=>
																																																								100,
																																																								'L'
																																																								=>
																																																								50,
																																																								'X'
																																																								=>
																																																								10,
																																																								'I'
																																																								=>
																																																								1,
																																																								'V'
																																																								=>
																																																								5)

																																																								  1.
																																																								  Part
																																																								  I
																																																								  (5
																																																										  min):
																																																									  For
																																																									  a
																																																									  DAG
																																																									  with
																																																									  unweighted
																																																									  edges,
																																																									  design
																																																									  a
																																																									  minimal
																																																									  API
																																																									  for
																																																										  the
																																																										  graph
																																																										  that
																																																										  enables
																																																										  you
																																																										  to
																																																										  traverse
																																																										  it.
																																																										  Part
																																																										  II
																																																										  (15
																																																												  min):
																																																											  Using
																																																											  the
																																																											  API
																																																											  from
																																																											  Part
																																																											  I,
																																																											  implement
																																																											  a
																																																											  function
																																																											  that
																																																											  takes
																																																											  a
																																																											  graph
																																																											  and
																																																											  prints
																																																											  out
																																																											  each
																																																											  node.
																																																											  Part
																																																											  III
																																																											  (20
																																																													  min):
																																																												  Using
																																																												  the
																																																												  API
																																																												  from
																																																												  Part
																																																												  I,
																																																												  implement
																																																												  a
																																																												  function
																																																												  that
																																																												  takes
																																																												  a
																																																												  graph,
																																																												  a
																																																												  start
																																																												  node,
																																																												  and
																																																												  a
																																																												  goal
																																																												  node,
																																																												  and
																																																												  returns
																																																												  a
																																																												  list
																																																												  of
																																																												  nodes
																																																												  that
																																																												  corresponds
																																																												  to
																																																												  the
																																																												  shortest
																																																												  path
																																																												  from
																																																												  the
																																																												  start
																																																												  node
																																																												  to
																																																												  the
																																																												  goal
																																																												  node.
																																																												  2. 
																																																												  Part
																																																												  I:
																																																													  Reverse
																																																													  the
																																																													  digits
																																																													  of
																																																													  a
																																																													  decimal
																																																													  number.
																																																													  Part
																																																													  II:
																																																														  Be
																																																														  able
																																																														  to
																																																														  do
																																																															  this
																																																															  for
																																																																  a
																																																																  number
																																																																  of
																																																																  any
																																																																  base
																																																																  between
																																																																  2-10.
																																																																  3.
																																																																  Given
																																																																  an
																																																																  array
																																																																  of
																																																																  integers,
																																																																  find
																																																																  the
																																																																  maximum
																																																																  contiguous
																																																																  sum
																																																																  that
																																																																  you
																																																																  can
																																																																  find
																																																																  in
																																																																  that
																																																																  array.
																																																																  4.
																																																																  Given
																																																																  a
																																																																  well
																																																																  formed
																																																																  binary
																																																																  tree,
																																																																  implement
																																																																  an
																																																																  iterator
																																																																  that
																																																																  iterates
																																																																  over
																																																																  it
																																																																  in
																																																																  in-order
																																																																  fashion.
																																																																  5.
																																																																  Given
																																																																  a
																																																																  series
																																																																  of
																																																																  intervals
																																																																  one
																																																																  at
																																																																  a
																																																																  time,
																																																																  output
																																																																  the
																																																																  total
																																																																  range
																																																																  after
																																																																  each
																																																																  one.
																																																																  Eg.,
																																																																  assume
																																																																  that
																																																																  the
																																																																  intervals
																																																																  are
																																																																  the
																																																																  time
																																																																  a
																																																																  user
																																																																  has
																																																																  been
																																																																  online.

																																																																  Input:
																																																																  [5,
																																																																  9]
																																																																  Output:
																																																																	  5

																																																																	  The
																																																																	  user
																																																																	  has
																																																																	  been
																																																																	  active
																																																																	  for
																																																																		  seconds
																																																																		  5,
																																																																		  6,
																																																																		  7,
																																																																		  8,
																																																																		  and
																																																																		  9,
																																																																		  for
																																																																			  a
																																																																			  total
																																																																			  of
																																																																			  5
																																																																			  seconds.

																																																																			  Input:
																																																																				  [1,
																																																																						  3]
																																																																				  Output:
																																																																					  8

																																																																					  We
																																																																					  now
																																																																					  log
																																																																					  seconds
																																																																					  1,
																																																																					  2,
																																																																					  and
																																																																					  3
																																																																					  for
																																																																						  a
																																																																						  a
																																																																						  total
																																																																						  of
																																																																						  8
																																																																						  seconds.

																																																																						  Input:
																																																																							  [13,
																																																																									  15]
																																																																							  Output:
																																																																								  11

																																																																								  We
																																																																								  log
																																																																								  seconds
																																																																								  13,
																																																																								  14,
																																																																								  and
																																																																								  15.

																																																																								  Input:
																																																																									  [11,
																																																																											  14]
																																																																									  Output:
																																																																										  13

																																																																										  But
																																																																										  now
																																																																										  the
																																																																										  only
																																																																										  new
																																																																										  seconds
																																																																										  are
																																																																										  11
																																																																										  and
																																																																										  12,
																																																																										  bringing
																																																																										  the
																																																																										  total
																																																																										  to
																																																																										  13
																																																																										  seconds.
																																																																										  6.
																																																																										  Given
																																																																										  an
																																																																										  integer
																																																																										  n,
																																																																										  find
																																																																										  the
																																																																										  greatest
																																																																										  integer
																																																																										  less
																																																																										  than
																																																																										  n
																																																																										  and
																																																																										  has
																																																																										  the
																																																																										  same
																																																																										  digits.
																																																																										  For
																																																																										  example,
																																																																										  n
																																																																										  =
																																																																										  681,
																																																																										  so
																																																																										  the
																																																																										  output
																																																																										  would
																																																																										  be
																																																																										  618,
																																																																										  and
																																																																										  the
																																																																										  ones
																																																																										  before
																																																																										  that
																																																																										  would
																																																																										  be
																																																																										  186
																																																																										  and
																																																																										  168.
																																																																										  7.
																																																																										  Part
																																																																										  2
																																																																										  of
																																																																										  Question
																																																																										  6.
																																																																										  Find
																																																																										  the
																																																																										  number
																																																																										  of
																																																																										  numbers
																																																																										  less
																																																																										  than
																																																																										  n
																																																																										  which
																																																																										  have
																																																																										  the
																																																																										  same
																																																																										  digits.
																																																																										  for
																																																																											  n
																																																																											  =
																																																																											  681,
																																																																											  it
																																																																											  is
																																																																											  3
																																																																											  (618,
																																																																													  186
																																																																													  and
																																																																													  168).
																																																																											  8.
																																																																											  Given
																																																																											  a
																																																																											  string
																																																																											  with
																																																																											  alpha-numeric
																																																																											  characters
																																																																											  and
																																																																											  parentheses,
																																																																											  return
																																																																										  a
																																																																										  string
																																																																										  with
																																																																										  balanced
																																																																										  parentheses
																																																																										  by
																																																																										  removing
																																																																										  the
																																																																										  fewest
																																																																										  characters
																																																																										  possible.
																																																																										  You
																																																																										  cannot
																																																																										  add
																																																																										  anything
																																																																										  to
																																																																										  the
																																																																										  string.
																																																																										  balance("()")
																																																																										  ->
																																																																										  "()"
																																																																										  balance("a(b)c)")
																																																																										  ->
																																																																										  "a(b)c"
																																																																										  balance(")(")
																																																																										  ->
																																																																										  ""
																																																																										  balance("(((((")
																																																																										  ->
																																																																										  ""
																																																																										  balance("(()()(")
																																																																										  ->
																																																																										  "()()"
																																																																										  balance(")(())(")
																																																																										  ->
																																																																										  "(())"

																																																																										  9.
																																																																										  Let's
																																																																										  recall
																																																																										  from
																																																																										  math
																																																																										  the
																																																																										  definition
																																																																										  of
																																																																										  dot
																																																																										  product.
																																																																										  (This
																																																																												  is
																																																																												  not
																																																																												  part
																																																																												  of
																																																																												  the
																																																																												  interview,
																																																																												  but
																																																																												  it's
																																																																												  good
																																																																												  to
																																																																												  have
																																																																												  the
																																																																												  candidate
																																																																												  say
																																																																												  it
																																																																												  if
																																																																												  they
																																																																												  know
																																																																												  it:
																																																																												  given
																																																																												  two
																																																																												  vectors
																																																																												  a
																																																																												  and
																																																																												  b,
																																																																												  the
																																																																												  dot
																																																																												  product
																																																																												  is
																																																																												  a1b1
																																																																												  +
																																																																												  a2b2
																																																																												  +
																																																																												  ...
																																																																												  +
																																																																												  anbn.)
																																																																										  This
																																																																										  is
																																																																										  a
																																																																										  simple
																																																																										  algorithm,
																																																																										  but
																																																																										  what
																																																																										  makes
																																																																										  it
																																																																										  interesting
																																																																										  is
																																																																										  application
																																																																										  to
																																																																										  sparse
																																																																										  vectors.
																																																																										  A
																																																																										  sparse
																																																																										  vector
																																																																										  is
																																																																										  a
																																																																										  vector
																																																																										  with
																																																																										  most
																																																																										  elements
																																																																										  equal
																																																																										  to
																																																																										  zero
																																																																										  - imagine
																																																																											 a
																																																																											 vector
																																																																											 with
																																																																											 millions
																																																																											 of
																																																																											 elements
																																																																											 (or
																																																																													 even
																																																																													 infinite,
																																																																													 as
																																																																													 is
																																																																													 the
																																																																													 case
																																																																													 for
																																																																													 e.g.
																																																																													 the
																																																																													 Fourier
																																																																													 Transform),
																																																																											 but
																																																																											 only
																																																																											 ten
																																																																											 thousand
																																																																											 or
																																																																											 so
																																																																											 are
																																																																											 nonzero.
																																																																											 Now,
																																																																											 a
																																																																											 machine
																																																																											 learning
																																																																											 application
																																																																											 loads
																																																																											 many
																																																																											 such
																																																																											 vectors
																																																																											 in
																																																																											 memory
																																																																											 (from
																																																																													 a
																																																																													 file
																																																																													 or
																																																																													 a
																																																																													 database)
																																																																											 and
																																																																											 computes
																																																																											 many
																																																																											 such
																																																																											 dot
																																																																											 products.
																																																																											 The
																																																																											 question
																																																																											 is
																																																																											 twofold.
																																																																											 First,
																																																																											 what
																																																																											 is
																																																																											 a
																																																																											 good
																																																																											 storage
																																																																											 strategy
																																																																											 for
																																																																												 sparse
																																																																												 vectors
																																																																												 such
																																																																												 that
																																																																												 we
																																																																												 get
																																																																												 fast
																																																																												 dot
																																																																												 product?
																																																																												 We
																																																																												 are
																																																																												 looking
																																																																												 for
																																																																													 something
																																																																													 compact
																																																																													 that
																																																																													 optimizes
																																																																													 for
																																																																														 dot
																																																																														 product
																																																																														 but
																																																																														 not
																																																																														 any
																																																																														 other
																																																																														 operation
																																																																														 (e.g.
																																																																																 we
																																																																																 don't
																																																																																 care
																																																																																 for
																																																																																	 insertion
																																																																																	 or
																																																																																	 removal).
																																																																																	 Second,
																																																																																	 implement
																																																																																	 the
																																																																																	 dot
																																																																																	 product
																																																																																	 function.
																																																																																	 10.
																																																																																	 In
																																																																																	 a
																																																																																	 game
																																																																																	 where
																																																																																	 you
																																																																																	 can
																																																																																	 score
																																																																																	 2
																																																																																	 points,
																																																																																	 3
																																																																																	 points
																																																																																	 or
																																																																																	 7
																																																																																	 points
																																																																																	 at
																																																																																	 a
																																																																																	 time,
																																																																																	 write
																																																																																	 a
																																																																																	 function
																																																																																	 that
																																																																																	 turns
																																																																																	 an
																																																																																	 arbitrary
																																																																																	 score
																																																																																	 into
																																																																																	 the
																																																																																	 list
																																																																																	 of
																																																																																	 possible
																																																																																	 ways
																																																																																	 the
																																																																																	 score
																																																																																	 could
																																																																																	 have
																																																																																	 been
																																																																																	 reached.

