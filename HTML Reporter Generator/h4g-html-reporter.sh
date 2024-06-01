#!/bin/bash

cat << EOF
<style>
@media print {
    .pagebreak { page-break-before: always; }
      div { break-inside: avoid; }
}
</style>
EOF

ls -1d */ | cut -d/ -f1 | sort -n | while read activity; do
   echo "<h1 class=\"pagebreak\">Atividade $activity</h1>"
   ls -1 $activity/ | sort -n | while read screen; do
   screenName="$(echo $screen | cut -d. -f1)"
      echo "<div>"   
      echo "<h2>Passo $screenName</h2>"
      echo "<img src=\"$activity/$screen\" width=\"100%\" />"
      echo "</div>"
   done
done
