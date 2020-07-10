<?php include '_inc/_header.php'; ?>

<!--

kalerkontho
bdnews, barta24
 -->
<body>
	<div class="header">
		<h1>Wine Parser <sup>BETA</sup></h1>
	</div>
	<div class="wraper">
		<?php include '_inc/header_nav.php'; ?>

		<div class="container">
			<h1>Are you missing what’s important?</h1>
			<p>
				Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
			</p>
		</div>

	</div>
</body>
<!-- -->

<textarea id="demo" aria-hidden="true"></textarea>

<script>
function copy(text) {
	var t = document.getElementById("demo");
	t.value = text;
	t.select();
	document.execCommand("copy");
}

function ittefaqGetPgNo() {
	var url_string = window.location.href;
	var url = new URL(url_string);
	var pg = url.searchParams.get("pg");

	pg = parseInt(pg) + 1;
	window.location.href = 'crawl.php?str=ittefaq&&pg=' + pg;
}
</script>




</body>

</html>