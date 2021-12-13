<main>
<h2>--- Day 9: Smoke Basin ---</h2><p>These caves seem to be <a href="https://en.wikipedia.org/wiki/Lava_tube" target="_blank">lava tubes</a>. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly <span title="This was originally going to be a puzzle about watersheds, but we're already under water.">settles like rain</span>.</p>
<p>If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).</p>
<p>Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:</p>
<pre><code>2<b>1</b>9994321<b>0</b>
3987894921
98<b>5</b>6789892
8767896789
989996<b>5</b>678
</code></pre>
<p>Each number corresponds to the height of a particular location, where <code>9</code> is the highest and <code>0</code> is the lowest a location can be.</p>
<p>Your first goal is to find the <em>low points</em> - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)</p>
<p>In the above example, there are <em>four</em> low points, all highlighted: two are in the first row (a <code>1</code> and a <code>0</code>), one is in the third row (a <code>5</code>), and one is in the bottom row (also a <code>5</code>). All other locations on the heightmap have some lower adjacent location, and so are not low points.</p>
<p>The <em>risk level</em> of a low point is <em>1 plus its height</em>. In the above example, the risk levels of the low points are <code>2</code>, <code>1</code>, <code>6</code>, and <code>6</code>. The sum of the risk levels of all low points in the heightmap is therefore <code><em>15</em></code>.</p>
<p>Find all of the low points on your heightmap. <em>What is the sum of the risk levels of all low points on your heightmap?</em></p>
</article>

<!--
<p>Your puzzle answer was <code>603</code>.</p><article class="day-desc">
-->

<h2 id="part2">--- Part Two ---</h2><p>Next, you need to find the largest basins so you know what areas are most important to avoid.</p>
<p>A <em>basin</em> is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height <code>9</code> do not count as being in any basin, and all other locations will always be part of exactly one basin.</p>
<p>The <em>size</em> of a basin is the number of locations within the basin, including the low point. The example above has four basins.</p>
<p>The top-left basin, size <code>3</code>:</p>
<pre><code><b>21</b>99943210
<b>3</b>987894921
9856789892
8767896789
9899965678
</code></pre>
<p>The top-right basin, size <code>9</code>:</p>
<pre><code>21999<b>43210</b>
398789<b>4</b>9<b>21</b>
985678989<b>2</b>
8767896789
9899965678
</code></pre>
<p>The middle basin, size <code>14</code>:</p>
<pre><code>2199943210
39<b>878</b>94921
9<b>85678</b>9892
<b>87678</b>96789
9<b>8</b>99965678
</code></pre>
<p>The bottom-right basin, size <code>9</code>:</p>
<pre><code>2199943210
3987894921
9856789<b>8</b>92
876789<b>678</b>9
98999<b>65678</b>
</code></pre>
<p>Find the three largest basins and multiply their sizes together. In the above example, this is <code>9 * 14 * 9 = <em>1134</em></code>.</p>
<p><em>What do you get if you multiply together the sizes of the three largest basins?</em></p>
</article>

<!--
<p>Your puzzle answer was <code>786780</code>.</p><p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
<p>At this point, you should <a href="/2021">return to your Advent calendar</a> and try another puzzle.</p>
<p>If you still want to see it, you can <a href="9/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Smoke+Basin%22+%2D+Day+9+%2D+Advent+of+Code+2021&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2021%2Fday%2F9&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' && mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=I%27ve+completed+%22Smoke+Basin%22+%2D+Day+9+%2D+Advent+of+Code+2021+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2021%2Fday%2F9'}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
-->

</main>