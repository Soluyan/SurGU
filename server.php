<!DOCTYPE html>
<html>
<head>
<title></title>
<meta charset="utf-8" />
</head>
<body>
<h2>Долги</h2>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
<?php


$conn = new SQLite3('base.db');

$sql = "SELECT id, Name, Value, Date FROM Dolgi";
$result = $conn -> query($sql);


While($data = $result->fetchArray(SQLITE3_ASSOC)){
    $array[] = $data;

}
echo "<table class='table table-striped, table-bordered, align-middle'>
<thead>
<tr>
  <th valign='top' width='7%'>Id</th>
  <th valign='top' width='20%'>Имя</th>
  <th valign='top' width='20%'>Сумма</th>
  <th valign='top' width='20%'>Дата</th>
</tr>
</thead>";
echo "</table>";

foreach($array as $row){
    echo "<table class='table table-striped, table-bordered, align-middle'>";
    echo "<tbody>";
    echo "<tr class='align-bottom'>";
        echo "<td valign='top' width='7%'>" . $row["id"] . "</td>";
        echo "<td valign='top' width='20%'>" . $row["Name"] . "</td>";
        echo "<td valign='top' width='20%'>" . $row["Value"] . "</td>";
        echo "<td valign='top' width='20%'>" . $row["Date"] . "</td>";
    echo "</tr>";
    echo "</tbody>";
    
    echo "</table>";
    $result->fetchArray();
}

$conn->close();
?>
</body>
</html>