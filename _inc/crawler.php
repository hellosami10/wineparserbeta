<?php
			/*
				prothomalo=chipmunk
				jago=activist
				kaler konto=leftover
				bdpratidin=thunder
			*/
$str = $_GET['str'];


$pg = $_GET['pg'];
if(!isset($pg)) {
	$pg = 1;
} else { }


if(isset($str)) {
	switch($str) {
		// prothomalo=chipmunk
		case 'chipmunk':
			$str = $str . ".py";
			$output = shell_exec("python '{$str}'");
			echo "<div class='fadeInDown'>". $output ."</div>";
			break;
		case 'thunder':
			$str = $str . ".py";
			$output = shell_exec("python '{$str}'");
			echo "<div class='fadeInDown'>". $output ."</div>";
			break;
		case 'bdnews24':
			$str = $str . ".py";
			$output = shell_exec("python '{$str}'");
			echo "<div class='fadeInDown'>". $output ."</div>";
			break;
		case 'kalerkantho':
			$str = $str . ".py";
			$output = shell_exec("python '{$str}'");
			echo "<div class='fadeInDown'>". $output ."</div>";
			break;
		case 'barta24':
			$str = $str . ".py";
			$output = shell_exec("python '{$str}'");
			echo "<div class='fadeInDown'>". $output ."</div>";
			break;
		case 'banglatribune':
			$str = $str . ".py";
			$output = shell_exec("python '{$str}'");
			echo "<div class='fadeInDown'>". $output ."</div>";
			break;
		case 'ittefaq':
			$str = $str . ".py";
			$url = "<script>ittefaqGetPgNo();</script>";
			$output = shell_exec("python '{$str}' '{$url}'");
			echo "<div class='fadeInDown'>". $output ."</div>";
			break;	
		case 'activist':
			$date = date("d/m/Y");

			$str = $str . ".py";
			$output = shell_exec("python '{$str}' '{$date}' '{$pg}'");

			echo "<div class='fadeInDown'>". $output ."</div>";




			$str = "activist-pagi.py";
			$count = shell_exec("python '{$str}' '{$date}'");
			echo "<div class='pagination'>";
			for($i = 1; $i <= $count; $i++) {
				echo "<a href='crawl.php?str=activist&pg=$i'><span>$i</span></a>";
			}
			echo "</div>";


			break;

		default:
			echo "<script>alert('404 NOT FOUND!');</script>";
	}
}

?>