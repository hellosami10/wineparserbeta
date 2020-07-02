<?php 

?>
<div class="nav">
	<ul>
		<a href="crawl.php?str=activist"><li class="<?php if($_GET['str'] == 'activist') echo 'active';?>">JAGONEWS24</li></a>
		<a href="crawl.php?str=chipmunk" class="<?php if($_GET['str'] == 'chipmunk') echo 'active';?>"><li>PROTHOM ALO</li></a>
		<a href="crawl.php?str=thunder" class="<?php if($_GET['str'] == 'thunder') echo 'active';?>"><li>BD PRATIDIN</li></a>
		<a href="crawl.php?str=bdnews24"><li>BDNEWS24</li></a>
		<a href="crawl.php?str=kalerkantho"><li>KALER KANTHO</li></a>
		<a href="crawl.php?str=barta24"><li>BARTA24</li></a>
		<a href="crawl.php?str=banglatribune"><li>Bangla Tribune</li></a>
	</ul>
</div>
