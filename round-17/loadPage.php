<?php
	$file = fopen($_GET["filename"], "r") or die("Unable to open file!");
	$content = fread($file,filesize($_GET["filename"]));
	echo $content;
	fclose($file);
?>