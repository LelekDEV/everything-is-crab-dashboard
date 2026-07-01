<?php

// components.php:
// Stores reusable functions for generating basic site components.
// TextComponent only generates HTML display, character images have to be generated separately (see scripts/generate_text.py)

function TextComponent($classname, $text)
{
	printf('<div class = "%s">', $classname);

	$delay = 0;
	foreach (str_split($text) as $char)
	{
		if ($char === ' ')
		{
			echo '<span></span>';
		}
		elseif ($char === 'y' || $char === 'g' || $char === 'Y' || $char === 'G')
		{
			$file = ctype_upper($char) ? sprintf("%s_u.png", $char) : sprintf("%s.png", $char);
			printf(
				'<img class = "tall-char" style = "animation-delay: %ss" src = "%s/%s">', 
				$delay, CHAR_PATH, $file
			);
		}
		else
		{
			$file = ctype_upper($char) ? sprintf("%s_u.png", $char) : sprintf("%s.png", $char);
			printf(
				'<img style = "animation-delay: %ss" src = "%s/%s">', 
				$delay, CHAR_PATH, $file
			);
		}

		$delay += 1 / strlen($text);
	}

	echo '</div>';
}

function ImgComponent($classname)
{
	printf('<div class = "%s">', $classname);

	foreach (scandir(IMG_PATH) as $file)
	{
		if ($file !== '.' && $file !== '..')
		{
			printf('<div onmouseover = "toggleEvo(\'%s\', 1)" onmouseleave = "toggleEvo(\'%s\', 0)"><img src = "%s/%s"></div>', $file, $file, IMG_PATH, $file);
		}
	}

	echo '</div>';
}

function EvoComponent($classname, $dirname)
{
	$scan = scandir(sprintf('%s/%s', EVO_PATH, $dirname));
	$width = 4 * 4 * 37;
	$speed = (count($scan) - 2) * 0.65;

	printf('<div id = "%s" class = "%s" style = "width: %spx"><div style = "animation-duration: %ss">', $dirname, $classname, $width, $speed);

	for ($i = 0; $i < 2; $i++)
	{ 
		foreach ($scan as $file)
		{
			if ($file !== '.' && $file !== '..')
			{
				printf('<img src = "%s/%s/%s">', EVO_PATH, $dirname, $file);
			}
		}
	}
	
	echo '</div></div>';
}

function AllEvoComponents($classname)
{
	echo '<div class = "evolution-wrapper">';

	foreach (scandir(EVO_PATH) as $dir)
	{
		if ($dir !== '.' && $dir !== '..')
		{
			EvoComponent($classname, $dir);
		}
	}

	echo '</div>';
}

?>