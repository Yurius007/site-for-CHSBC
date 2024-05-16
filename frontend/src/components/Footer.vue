<template>
    <footer>
        
        <div class="upper">
            <img src="../../public/logo.png" alt="">
            <div class="contacts">
                <h2>Контакти</h2>
                <p>Черкаський державний бізнес коледж</p>
                <p>вул. Хрещатик, 1, м. Черкаси, 18000</p>
                <p>тел. (0472) 37-37-37</p>
                <p>email:</p>
            </div>
            <div class="socials">
                <h2>Соціальні мережі</h2>
                <div class="socials__inner">
                    <a href="#"><img src="../../public/Telegram_logo.png" alt=""></a>
                    <a href="#"><img src="../../public/Facebook_Logo_(2019).png.webp" alt=""></a>
                    <a href="#"><img src="../../public/Instagram_icon.png.webp" alt=""></a>
                </div>
            </div>
        </div>
        <p>© 2003-2024 Черкаський державний бізнес коледж</p>
    </footer>
</template>

<script>
</script>

<style scoped>
footer {
    margin-top: 50px;
    background-color: #3A3A3A;
    color: white;
    display: flex;
    padding: 10px 35px;
    justify-content: center;
    display: flex;
    flex-direction: column;
}

.upper {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

footer img {
    height: 100px;
    padding: 10px;
}

.socials {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.socials__inner img {
    height: 50px;
    padding: 10px;
}

</style>