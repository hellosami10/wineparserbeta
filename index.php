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

				<div class="heading">
					<small>Million News, One Place</small>
				</div>





				<div>
					<p>
						



						Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
					</p>
				</div>

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