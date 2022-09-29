<template>
    <div class="wrapper">
    <div class="left">
        <img src="https://i.imgur.com/cMy8V5j.png" alt="user" width="270">
        <h4>Alex William</h4>
         <p>Paciente</p>
    </div>
    <div class="right">
        <div class="info">
            <h3>Información</h3>
            <div class="info_data">
                 <div class="data">
                    <h3>Email</h3>
                    <p>alex@gmail.com</p>
                </div>
                 <div class="data">
                   <h3>Teléfono</h3>
                    <p>0001-213-998761</p>
                    <h3>Contacto Familiar</h3>
                    <p>Pedro Cifuentes</p>
                    <p>Padre</p>
                    <p>0001-458-566546</p>
                </div>
            </div>
        </div>
      
      <div class="projects">
            <h2>Historia Clínica</h2>
            <div class="projects_data">
                 <div class="data">
                    <h4>Sintomas</h4>
                    <p>Gripa muy fuerte y estres.</p>
                 
                   <h2>Signos Vitales</h2>
                    <li>Presion: 50 </li>
                    <li>Saturacion: 90</li>
                    <li>Frecuencia cardiaca: 90</li>
                    <li>Temperatura: 36°</li>
              </div>
            </div>
        </div>
      
        <div class="social_media">
            <ul>
              <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
              <li><a href="#"><i class="fab fa-twitter"></i></a></li>
              <li><a href="#"><i class="fab fa-instagram"></i></a></li>
          </ul>
      </div>
    </div>
</div>
</template>

<style>
    *{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  list-style: none;
  font-family: 'Josefin Sans', sans-serif;
}

body{
   background-color: #f3f3f3;
   display: flex;
   align-items: center;
   justify-content: center;
   height: 100%;
}

.wrapper{
  position: absolute;
  top: 300%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 100%;
  height: 400%;
  display: flex;
  box-shadow: 0 1px 20px 0 rgba(69,90,100,.08);
}

.wrapper .left{
  width: 35%;
  background: linear-gradient(to right,#01a9ac,#01dbdf);
  padding: 30px 25px;
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
  text-align: center;
  color: #fff;
}

.wrapper .left img{
  border-radius: 5px;
  margin-bottom: 10px;
}

.wrapper .left h4{
  margin-bottom: 10px;
  font-size: 40px;
}

.wrapper .left p{
  font-size: 30px;
}

.wrapper .right{
  width: 65%;
  background: #fff;
  padding: 30px 25px;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
}

.wrapper .right .info,
.wrapper .right .projects{
  margin-bottom: 25px;
}

.wrapper .right .info h3,
.wrapper .right .projects h3{
    margin-bottom: 15px;
    padding-bottom: 5px;
    border-bottom: 1px solid #e0e0e0;
    color: #353c4e;
  text-transform: uppercase;
  letter-spacing: 5px;
}

.wrapper .right .info_data,
.wrapper .right .projects_data{
  display: flex;
  justify-content: space-between;
}

.wrapper .right .info_data .data,
.wrapper .right .projects_data .data{
  width: 45%;
}

.wrapper .right .info_data .data h4,
.wrapper .right .projects_data .data h4{
    color: #04060a;
    margin-bottom: 5px;
    font-size: 18px;
}

.wrapper .right .info_data .data p,
.wrapper .right .projects_data .data p{
  font-size: 16px;
  margin-bottom: 10px;
  color: #000407;
}

.wrapper .social_media ul{
  display: flex;
}

.wrapper .social_media ul li{
  width: 45px;
  height: 45px;
  background: linear-gradient(to right,#01a9ac,#01dbdf);
  margin-right: 10px;
  border-radius: 5px;
  text-align: center;
  line-height: 45px;
}

.wrapper .social_media ul li a{
  color :#fff;
  display: block;
  font-size: 18px;
}

</style>