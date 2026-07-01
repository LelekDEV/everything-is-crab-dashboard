<?php

require 'components.php';

const CHAR_PATH = 'dynamic_assets/chars';
const IMG_PATH = 'dynamic_assets/creatures';
const EVO_PATH = 'dynamic_assets/evolutions';

const REM_IMG_PATH = 'C:/Users/Euro/Pictures/Everything is Crab';

$localSum = array_map(fn($item) => substr(explode('.', $item)[0], 2), array_slice(scandir(IMG_PATH), 2));
$remoteSum = array_map(fn($item) => explode('#', $item)[1], array_slice(scandir(REM_IMG_PATH), 2));

sort($localSum);
sort($remoteSum);

if ($localSum !== $remoteSum)
{
	$output = [];
	$code = 0;

	exec('python scripts/main.py', $code, $output);
}

?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset = "utf-8">
		<meta name = "viewport" content = "width=device-width, initial-scale=1">

		<link rel = "stylesheet" type = "text/css" href = "assets/style.css?lorem=ipsum">
		<link rel = "icon" type = "image/x-icon" href = "assets/favicon.ico">

		<title>Creature dashboard</title>
	</head>

	<body>
		<?php

		TextComponent('title-container backdrop', 'Everything is Crab - creature dashboard');
		ImgComponent('image-container backdrop');
		AllEvoComponents('evolution-container');

		?>

		<script>

		function toggleEvo(src, state)
		{
			document.getElementById('e_' + src.split('.')[0].slice(2)).style.opacity = state;
		}

		</script>
	</body>
</html>