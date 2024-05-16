<template>
  <header>
    <!-- <h1>Read the Docs</h1> -->
    <img src="../../public/logo.png" alt="">
    <ul>
      <li><a href="index.html">Головна</a></li>
      <li><a>Про нас</a></li>
      <li><a>Абітурієнту</a></li>
      <li><a>Студенетові</a></li>
      <li><a>Викладачу</a></li>
      <li><a>Конференції</a></li>
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
