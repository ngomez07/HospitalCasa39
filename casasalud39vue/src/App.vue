<template>

  <head>
      <meta charset='UTF-8'>
      <meta http-equiv='X-UA-Compatible' content='IE=edge'>
      <meta name='viewport' content='width=device-width, initial-scale=1.0'>
      <title>Pagina de inicio</title>
  </head>

  <body>
      <header>
          <div class='header__superior'>
            <div class='logo'>
              <img src="./assets/logoCS39.jpg" alt="" @load="loadImage">
            </div>
              <div class = 'search' >             
                  <input type='search' placeholder='¿Que desea buscar?' >
              </div>
          </div>
          <div class='contenedor__menu'>

              <div class='menu'>
                  <nav>
                      <ul>
                         <li><router-link to="/" class="nav-link"></router-link></li>
                         <li><router-link to="/LoginPaciente" class="nav-link">Ingreso Pacientes</router-link></li>
                         <li><router-link to="/LoginPersonal" class="nav-link">Ingreso Personal</router-link></li> 
                         <li><router-link to="/PagUser" class="nav-link">Pagina Usuario</router-link></li>  
                         <li><router-link to="/regisPa" class="nav-link"></router-link></li> 
                      </ul>
                  </nav>
              </div>
          </div>
          <div class="main-component">
          <router-view
          v-on:completedLoginpacientes="completedLoginpacientes"
          v-on:completedLoginPersonal="completedLoginPersonal"
          v-on:completedHome="completedHome"
          v-on:logOut="logOut"
          >
          </router-view>
          </div>
      </header>
      <div class="otra">
      <div class="Contenido">
      <br>
      <h2>Nuestros servicios</h2>
      <br>
      <p>
        La salud de una persona abarca muchos aspectos y cada uno tiene sus particularidades.
        Por eso los servicios médicos están especializados. 
      <br>
      Las especialidades clínicas se corresponden a:
      </p>
      <br>
      <ul>
      <li>Cardiología</li>
      <li>Gastroenterología</li>
      <li>Neumología</li>
      <li>Neurología</li>
      <li>Pediatría</li>
      <li>Medicina interna</li>
      <br>
      </ul>
      </div>

      <div class="Imagen">
      <h3>Imagen</h3>
      <img src="./assets/med.jpg" alt="" @load="loadImage">
      </div>
      <div class="Conclusión">
      <h3>Nuestro Proposito</h3>
      <p>
        Queremos preservar tu salud, para ello contamos con todas las especialidades
        necesarias y de la mano de los mejores especialistas para 
        que puedas estar tranquilo. Nos hacemos eco de que prevenir 
        es mejor que curar, y por ello mediante diferentes pruebas diagnósticas 
        proporcionamos la mejor asistencia médica y seguimiento a nuestros pacientes.
      </p>
    </div>
  </div>
  </body>
</template>

<script>
  export default {
  name: 'App',
  data: function () {
    return {
      is_auth: false
    }
  },
  components: {
  },
  methods: {
    verifyAuth: function() {
    this.is_auth = localStorage.getItem("isAuth") || false;
    if (this.is_auth == false)
    this.$router.push({ name: "LoginPaciente" });
    else
    this.$router.push({ name: "App" });
    },
    logOut: function () {
    localStorage.clear();
    alert("Sesión Cerrada");
    this.verifyAuth();
    },
    completedLogIn: function(data) {
    localStorage.setItem("isAuth", true);
    localStorage.setItem("username", data.username);
    localStorage.setItem("token_access", data.token_access);
    localStorage.setItem("token_refresh", data.token_refresh);
    alert("Autenticación Exitosa");
    this.verifyAuth();
    },
    completedLoginPersonal: function(data) {
    alert("Registro Exitoso");
    this.completedLoginPaciente(data);
    },
    completedInicio: function (data) { },
  },
  created: function () {
    this.verifyAuth()
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  text-decoration: none;
  font-family: 'Roboto', sans-serif;
  /*añadido para index*/
  text-decoration: none;
}

/*añadido para index*/
header {
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background-color: rgb(255, 255, 255);
}

.header__superior {
  max-width: 1200px;
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
}

.logo img {
  width: 150px;
}

.search input {
  width: 300px;
  padding: 10px;
  border: 2px solid rgb(57, 68, 165);
}

/*Barra menu*/
.contenedor__menu {
  width: 100%;
  height: 70px;
  background: #023877;
  padding: 0px 20px;
}

.menu {
  max-width: 1200px;
  margin: auto;
  height: 100%;
}

nav {
  height: 100%;
}

/*Selector para puntos especificos del menu*/
nav>ul {
  height: 100%;
  display: flex;
}

nav ul li {
  height: 100%;
  list-style: none;
  position: relative;
}

nav>ul>li:first-child>a {
  background: url("../src/assets/home.png");
  background-size: 24px;
  background-repeat: no-repeat;
  background-position: center center;
  padding: 20px 40px;
}

/*Para evitar que se desaparezca el icono*/
nav>ul>li:first-child>a {
  background: url("../src/assets/home-white.png");
  background-size: 24px;
  background-repeat: no-repeat;
  background-position: center center;
  padding: 20px 40px;
}

nav>ul>li>a {
  /*Para validar lo del texto de inicio*/
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  padding: 14px;
  color: white;
  text-transform: uppercase;
  font-size: 14px;
  transition: all 300ms ease;
}

nav>ul>li>a:hover {
  transform: scale(1.1);
  background: #0074C7;
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
}

#selected {
  transform: scale(1.1);
  background-color: #0074C7;
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
}

/*Submenu*/

nav ul li ul {
  width: 200px;
  display: flex;
  flex-direction: column;
  /*Para q aparezca uno debajo del otro*/
  background: #fff;
  position: absolute;
  top: 90px;
  left: -5px;
  padding: 14px 0px;
  visibility: hidden;
  opacity: 0;
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
  z-index: 10;
  transition: all 300ms ease;
}

nav ul li ul:hover {
  visibility: visible;
  opacity: 1;
  top: 70px;
}

nav ul li ul:before {
  content: '';
  width: 0;
  height: 0;
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-bottom: 12px solid white;
  position: absolute;
  top: -12px;
  left: 20px;
}

nav ul li ul li a {
  display: block;
  color: #0099E9;
  padding: 6px;
  padding-left: 14px;
  margin-top: 10px;
  font-size: 14px;
  text-transform: uppercase;
  transition: all 300ms ease;
}

nav ul li ul li a:hover {
  background: #0074C7;
  color: #fff;
  transform: scale(1.1);
  padding-left: 30px;
  font-size: 14px;
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
}

/*Elementos responsivos*/
.icon__menu {
  font-size: 26px;
  color: #fff;
  cursor: pointer;
  width: 26px;
  height: 100%;
  display: none;
  align-items: center;
}

#check__menu {
  display: none;
}

/*Para la parte responsive*/
@media screen and (max-width:720px) {
  .search input {
      display: none;
  }

  .header__superior {
      padding: 10px;
  }

  .logo img {
      width: 200px;
  }

  nav>ul {
      flex-direction: column;
      background-color: #023877;
      position: fixed;
      left: 0;
      top: 158px;
      width: 100%;
      height: 0px;
      transition: all 300ms ease;
      z-index: 100;
      opacity: 0;
      visibility: hidden;
  }

  nav>ul>li>a:hover {
      transform: scale(1);
  }

  nav ul li ul {
      left: 90px;
  }

  nav>ul>li:hover ul {
      top: 50px;
  }

  nav>ul>li:first-child a {
      background-position: 20px;
  }

  #selected {
      transform: scale(1);
  }

  #label__check {
      display: block;
  }

  .icon__menu {
      display: flex;
  }

}

body {
  background: url("../src/assets/fondo1.jpg");
  /*background-size: cover;*/
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
}

main {
  width: 100%;
  padding: 20px;
  margin: auto;
  margin-top: 100px;
}

.contenedor__todo {
  width: 100%;
  max-width: 800px;
  margin: auto;
  position: relative;
}

.caja__trasera {
  width: 100%;
  padding: 10px 20px;
  display: flex;
  justify-content: center;
  backdrop-filter: blur(10px);
  background-color: rgba(0, 128, 255, 0.5);
}

.caja__trasera div {
  margin: 100px 40px;
  color: white;
  transition: all 500ms;
}

.caja__trasera div p,
.caja__trasera div button {
  margin-top: 30px;
}

.caja__trasera div h3 {
  font-weight: 400;
  font-size: 26px;
}

.caja__trasera button {
  padding: 10px 40px;
  border: 2px solid #fff;
  background: transparent;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  color: white;
  outline: none;
  transition: all 300ms;
}

.caja__trasera button:hover {
  background: #fff;
  color: #46A2FD;
}

/*formulario*/
.contenedor__ini-reg {
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 380px;
  position: relative;
  top: -185px;
  left: 10px;
  transition: left 500ms cubic-bezier(0.175, 0.885, 0.320, 1.275);
}

.contenedor__ini-reg form {
  width: 100%;
  padding: 80px 20px;
  margin-top: 500px;
  background: #fff;
  position: absolute;
  border-radius: 20px;
}


.contenedor__ini-reg form h2 {
  font-size: 30px;
  text-align: center;
  margin-bottom: 20px;
  color: #46A2FD;
}

.contenedor__ini-reg form input {
  width: 100%;
  margin-top: 10px;
  padding: 10px;
  border: none;
  background: #F2F2F2;
  font-size: 16px;
  outline: none;
}

.contenedor__ini-reg form p {
  margin-top: 15px;
  margin-bottom: 5px;
  margin-left: 5px;
}

.contenedor__ini-reg form button {
  padding: 10px 40px;
  margin-top: 30px;
  border: none;
  font-size: 14px;
  background: #46A2FD;
  color: white;
  cursor: pointer;
  outline: none;
}

.formulario__inicio {
  margin-bottom: 500px;
  height: 400px;
  opacity: 1;
  display: block;
}

.formulario_reg {
  display: none;
}

/*Responsive Design*/
@media screen and (max-width: 850px) {

  main {
      margin-top: 50px;
  }

  .caja__trasera {
      max-width: 350px;
      height: 300px;
      flex-direction: column;
      margin: auto;
  }

  .caja__trasera div {
      margin: 0px;
      position: absolute;
  }

  /*formulario*/
  .contenedor__ini-reg {
      top: -10px;
      left: -5px;
      margin: auto;
  }

  .contenedor__ini-reg form {
      position: relative;
  }
}

.Contenido {
color: #5E1C36;
border-radius: 10px;
margin: 0px 40px 0px 40px;
padding: 10px 40px 10px 40px;
background-color: #c7f2e7;
}

.Contenido h2{
  text-align: center;
  font-size: 30px;
}

.Contenido p{
  text-align: center;
  font-size: 20px;
}

.Contenido li{
  font-size: 18px;
}

.Conclusión {
color: #e1e3ec;
font-size: 20px;
text-align: center;
border-radius: 10px;
margin: 0px 40px 0px 40px;
padding: 5px 40px 5px 40px;
background-color: #5C85D5;
}

.Imagen h3 {
display: none;
}

.Imagen img {
height: 300px;
display: block;
border-radius: 100px;
border: 3px solid white;
margin: 20px auto 20px auto;
}

.otra{
margin-top: 220px;
}
</style>