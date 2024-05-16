<template>
  <Header />
  <carousel :items-to-show="0.75" >
    <slide :key="1">
      <img src="../public/1.jpg" alt="">
    </slide>
    <slide :key="2">
      <img src="../public/2.jpg" alt="">
    </slide>
    <slide :key="3">
      <img src="../public/3.jpg" alt="">
    </slide>

    <template #addons>
      <navigation />
      <pagination />
    </template>
  </carousel>

  <div class="services">
    <div class="service">
      <img src="../public/stud.png" alt="">
      <h3>Студентський портал</h3>
    </div>
    <div class="service">
      <img src="../public/science.png" alt="">
      <h3>Наукова діяльність</h3>
    </div>
    <div class="service">
      <img src="../public/library.png" alt="">
      <h3>Бібліотека</h3>
    </div>
    <div class="service">
      <img src="../public/career.png" alt="">
      <h3>Центр Кар'єри та міжнародних зв'язків</h3>
    </div>
  </div>
  <center>
    <h1>Останні новини</h1>
    <div class="news-list">
      <div class="news" v-for="novelty in news">
          <img :src="novelty.img" alt="">
          <a :href="novelty.link">
            <span>{{ novelty.title }}</span>
          </a>
      </div>
    </div>
  </center>
  <Footer />
</template>

<script>
// If you are using PurgeCSS, make sure to whitelist the carousel CSS classes
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
    Header,
    Footer,
  },
  data() {
    return {
      news: [
        {
          title: 'ЗБІРНА КОМАНДА ЧЕРКАСЬКОГО ДЕРЖАВНОГО БІЗНЕС-КОЛЕДЖУ ЗДОБУЛА ІІ МІСЦЕ НА ЗМАГАННЯХ З ФУТЗАЛУ!',
          link: '#',
          img: '../public/news/1.jpg',
        },
        {
          title: 'НАВЧАЛЬНА ПРАКТИКА СТУДЕНТІВ Кафедри комп\'ютерної інженерії та інформаційних технологій ',
          link: '#',
          img: '../public/news/2.jpg',
        },
        {
          title: 'БІЗНЕС-КОЛЕДЖ УВІЙШОВ ДО 100 КРАЩИХ НАУКОВИХ УСТАНОВ УКРАЇНИ',
          link: '#',
          img: '../public/news/3.jpg',
        },
      ],
    }
  },
}
</script>

<style>



.services {
  display: flex;
  justify-content: space-around;
  padding: 20px;
}

.service {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #464B79;
  width: 200px;
  height: 200px;
  color: white;
  border-radius: 15px;
  padding: 20px;
  transition: all 0.2s; 
  text-align: center;
  /* box-sizing: border-box; */
}

.service:hover {
  transform: scale(1.1);
}

.news-list {
  display: flex;
  justify-content: space-around;
  padding: 20px;
}

.news {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #DADADA;
  width: 360px;
  height: 400px;
  color: white;
  border-radius: 15px;
  /* padding: 20px; */
  transition: all 0.2s; 
  /* text-align: center; */
  /* box-sizing: border-box; */
}

.news:hover {
  transform: scale(1.05);
}

.news a {
  width: 100%;
  height: 100%;
  text-decoration: none;
  color: black;
  padding: 20px;
  box-sizing: border-box;
  text-align:start;
  font-weight: 500;
  font-size: 20px;
}

.news img {
  width: 100%;
  max-height: 300px;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  /* height: 200px; */
}

</style>