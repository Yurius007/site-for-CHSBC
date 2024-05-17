<template>
    <Header />
    <center>
        <h1>Студентська рада</h1>
        <p>Студентське самоврядування —  самостійна громадська діяльність студентів, що забезпечує виконання студентами своїх обов’язків і захист їх прав,  а також їх участь в управлінні вищим навчальним закладом задля всебічного розвитку особистості членів студентської громади.</p>
        <form method="post">
            <h2>Залишити заявку</h2>
            <input type="text" name="name" placeholder="Ім'я" required>
            <input type="text" name="group" placeholder="Група" required>
            <input type="text" name="contact" placeholder="Email або телеграм юзернейм" required>
            <!-- <input type="textarea" name="text" placeholder="Чому ви хочете приєднатися до студентської ради?" required> -->
            <textarea name="text" id="" cols="30" rows="10" placeholder="Чому ви хочете приєднатися до студентської ради?"></textarea>
            <input type="submit" value="Відправити">
        </form>
    </center>
    

    <Footer />
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'Studrada',
  components: {
    Header,
    Footer,
  },
}
</script>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    width: 30%;
    margin: 0 auto;
    padding: 10px 40px 40px 40px;
    border-radius: 15px;
    background-color: #2F324D;
    color: white;
}

input, textarea {
    margin: 7px;
    padding: 10px;
    border-radius: 5px;
    border: none;
    background-color: #656B99;
    font-size: 18px;
    font-weight: 600;
    font-family: inherit;
    color: rgba(0, 0, 0, 0.84);
    
}

input[type="submit"] {
    background-color: white;
    color: black;
    cursor: pointer;
}

p {
    width: 70%;
    margin: 0 auto;
    padding: 10px;
    font-weight: 500;
    text-align: center;
    margin-bottom: 75px;
}

</style>