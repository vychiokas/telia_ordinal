# telia_ordinal

## Background

We are given paths to go from one point to another. The paths are &quot;NORTH&quot;, &quot;SOUTH&quot;, &quot;WEST&quot;, &quot;EAST&quot;.
Clearly &quot;NORTH&quot; and &quot;SOUTH&quot; are opposite, &quot;WEST&quot; and &quot;EAST&quot; too. Going one path and coming back the
opposite path is a wasted effort, so let&#39;s concise these paths to go the shortest route.
For example, given the following paths:
You can immediately see that going &quot;NORTH&quot; and then &quot;SOUTH&quot; is not reasonable, better stay to the same
place!
So the task is to reduce a simplified version of the plan. A better plan in this case is simply:
Other examples:
In [&quot;NORTH&quot;, &quot;SOUTH&quot;, &quot;EAST&quot;, &quot;WEST&quot;], the path &quot;NORTH&quot; + &quot;SOUTH&quot; is going north and coming back right
away. What a waste of time! Better to do nothing. The path becomes [&quot;EAST&quot;, &quot;WEST&quot;],
now &quot;EAST&quot; and &quot;WEST&quot; annihilate each other, therefore, the final result is [] .
In [&quot;NORTH&quot;, &quot;EAST&quot;, &quot;WEST&quot;, &quot;SOUTH&quot;, &quot;WEST&quot;, &quot;WEST&quot;], &quot;NORTH&quot; and &quot;SOUTH&quot; are not directly
opposite but they become directly opposite after the reduction of &quot;EAST&quot; and &quot;WEST&quot; so the whole path is
reducible to [&quot;WEST&quot;, &quot;WEST&quot;].