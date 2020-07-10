<?php 
	function chk_active($str) {

		if($_GET['str'] == $str)
			echo 'active';

	}
?>

<div class="nav">
	<ul>
		<a href="crawl.php?str=activist"><li class="<?php chk_active('activist');?>">JAGONEWS24</li></a>
		<a href="crawl.php?str=chipmunk"><li class="<?php chk_active('chipmunk');?>">PROTHOM ALO</li></a>
		<a href="crawl.php?str=thunder"><li class="<?php chk_active('thunder');?>">BD PRATIDIN</li></a>
		<a href="crawl.php?str=bdnews24"><li class="<?php chk_active('bdnews24');?>">BDNEWS24</li></a>
		<a href="crawl.php?str=kalerkantho"><li class="<?php chk_active('kalerkantho');?>">KALER KANTHO</li></a>
		<a href="crawl.php?str=barta24"><li class="<?php chk_active('barta24');?>">BARTA24</li></a>
		<a href="crawl.php?str=banglatribune"><li class="<?php chk_active('banglatribune');?>">Bangla Tribune</li></a>
		<a href="crawl.php?str=ittefaq"><li class="<?php chk_active('banglatribune');?>">Bangla Tribune</li></a>
	</ul>
</div>
