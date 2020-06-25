<?php
// $output = shell_exec("python bdp.py");
// echo "output: " . $output;


?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Red Wine</title>
<link href="https://fonts.googleapis.com/css2?family=Teko&display=swap" rel="stylesheet"> 

<link rel="stylesheet" href="css/style.css">


</head>
<body>
	
	<div class="wraper">
		<?php
			include '_inc/header_nav.php';
		?>

		<div class="content-wrap">
			<div class="content">
				<span class="latest-news-text">সর্বশেষ</span>
				<ul >
					<?php
					/*
						prothomalo=chipmunk
						jago=activist
						kaler konto=leftover
						bdpratidin=thunder
					*/
						$str = $_GET['str'];
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
								case 'activist':
									$str = $str . ".py";
									$output = shell_exec("python '{$str}'");
									echo "<div class='fadeInDown'>". $output ."</div>";
									break;

								default:
									echo "<script>alert('404 NOT FOUND!');</script>";
							}
						}
				
					?>

				</ul>
			</div>
		</div>

	</div>


<textarea id="demo" aria-hidden="true"></textarea>

<script>


function copy(text) {
	var t = document.getElementById("demo");
	t.value = text;
	t.select();
	document.execCommand("copy");
}
</script>
</body>

</html>