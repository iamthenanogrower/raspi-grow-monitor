<html>
<head>
	<title>raspi-grow-monitor</title>

	<link rel="stylesheet" type="text/css" href="styles/style.css">

	<script src="libs/jquery.min.js"></script>
	<script>
		function update() {
			$.ajax({
				url: "ajax.php",
				cache:false,
				success: function (result) {
					$('#status').html(result);
					setTimeout(function(){update()}, 2000);
				}
			});
		}
		update();
        </script>
</head>
<body>
	<div class="divtl">
		<div id="status"></div>
	</div>
</body>
</html>
