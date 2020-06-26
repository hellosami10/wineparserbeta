<?php
									date_default_timezone_set("Asia/Dhaka");


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
								case 'activist':
									$date = date("d/m/Y");

									$str = $str . ".py";
									$output = shell_exec("python '{$str}' '{$date}' '{$pg}'");
									
									echo "<div class='fadeInDown'>". $output ."</div>";




									$str = $str . "-pagi.py";
									$output = shell_exec("python '{$str}' '{$date}'");
									echo "<div class='pagination'>";
									for($i = 2; $i <= $count; $i++) {
										echo "<a href=''><span>$i</span></a>";
									}
									echo "</div>";


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