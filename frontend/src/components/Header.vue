<template>
  <header>
    <!-- <h1>Read the Docs</h1> -->
    <img src="../../public/logo.png" alt="">
    <ul>
      <li><a href="/">Головна</a></li>
      <li><a href="about">Про нас</a></li>
      <li><a href="http://csbc.edu.ua/documents/enrollee/obsyag18.pdf">Абітурієнту</a></li>
      <li><a href="http://csbc.edu.ua/student.php?student=7">Студенетові</a></li>
      <li><a href="http://csbc.edu.ua/teacher.php?teacher=2">Викладачу</a></li>
      <li><a href="studrada">Студрада</a></li>
    </ul>
  </header>
</template>

<script></script>

<style scoped>
header {
  background-color: #2F324D;
  color: white;
  display: flex;
  /* padding: 10px; */
  /* height: 30px; */
  padding: 0 20px;
}

header img {
  height: 40px;
  padding: 10px;
}

ul {
  display: flex;
  list-style: none;
  padding: 0;
  margin-left: auto;
}

li {
  font-size: 18px;
  padding: 5px 10px;
  margin: 0 20px;
  cursor: pointer;
}

li:hover {
  transform: scale(1.1);
}

li a {
  
  text-decoration: none;
  color: white;
}
</style>
