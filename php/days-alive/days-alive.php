<?php
$date_format = 'm/d/Y';
$today = new DateTime();
$today = $today->format($date_format);
$your_birthday = readline("Your birthday (Example: 07/11/1997): ");
$a = DateTime::createFromFormat($date_format, $your_birthday);
$b = DateTime::createFromFormat($date_format, $today);
$delta = $b->diff($a);
echo "As of today you are " . $delta->days . " days old.";
