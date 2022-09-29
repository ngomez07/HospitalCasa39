<template>
<head>
    <meta charset="UFT-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casa Salud 39 Login</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
</head>
<body>
<div class="boton">
    <button></button>
    <button></button>
</div>
    <main>
    <div class="contenedor__todo">
        <div class="caja__trasera">
            <div class="caja_trasera-login">
                <h3>¿Ya tienes una cuenta?</h3>
                <p>Inicia sesión para entrar en la página</p>
                <button @click="btn__iniciar-sesion">Iniciar Sesión</button>
            </div>
            <div class="caja_trasera-register">
                <h3>¿Aún no tienes cuenta?</h3>
                <p>Registrate para que puedas iniciar sesión</p>
                <button @click="$router.push('regisPa')">Registrarse</button>
            </div>
        </div>
        <!--Formularios para ingresar-->
        <div class="contenedor__ini-reg">
            <!--Ingreso-->
            <form action="" class="formulario__inicio">
                <h2>Iniciar Sesión</h2>
                <select name="tipo" id="tipo">
                    <option value="0">Seleccione tipo de usuario</option>
                    <option value="1">Medico</option>
                    <option value="2">Enfermera</option>
                    <option value="3">Auxiliar</option>
                  </select>
                <input type="text" placeholder="Id User" minlength="4" maxlength="4">
                <input type="password" placeholder="Contraseña" minlength="8" maxlength="8">
                <button @click="btn__iniPer">Entrar</button>
            </form>
            <form action="" class="formulario_reg">
                <!--Registro-->
                <h2>Registrarse</h2>
                <input type="text" placeholder="ID_PS" minlength="8" maxlength="8">
                <input type="text" placeholder="Nombre">
                <input type="text" placeholder="Especialidad">
                <select name="tipo" id="tipo">
                    <option value="0">Seleccione tipo de usuario</option>
                    <option value="1">Medico</option>
                    <option value="2">Enfermera</option>
                    <option value="3">Auxiliar</option>
                  </select>
                <input type="text" placeholder="ID Usuario" minlength="4" maxlength="4">
                <input type="password" placeholder="Contraseña" minlength="8" maxlength="8">
                <button>Registrarse</button>
            </form>
        </div>
    </div>
    </main>
</body>
</template>

<script>
    import axios from 'axios';
    export default {
    name: "LoginPersonal",
    data: function(){
    return {
    user: {
    username:"",
    password:""
    }
    }
    },
    methods:{
    btn__iniPer() {
    alert('Clave incorrecta');
    },
    processLoginPersonalUser: function(){
    axios.post(
    "https://mision-tic-bank-be.herokuapp.com/login/",
    this.user,
    {headers: {}}
    )
    .then((result) => {
    let dataLoginPersonal = {
    username: this.user.username,
    token_access: result.data.access,
    token_refresh: result.data.refresh,
    }
    
    this.$emit('completedLoginPersonal', dataLoginPersonal)
    
    })
    .catch((error) => {
    if (error.response.status == "401")
    alert("ERROR 401: Credenciales Incorrectas.");
    });
    }
    }
    }
    </script>

<style>
    *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
    font-family: 'Roboto', sans-serif;
    }
    body{
    background: url("../assets/fondo1.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
}

.boton button{
    display: inline-block;
    margin: 0 10px;
    padding: 8px 30px;
    border-bottom: 2px solid rgb(0, 128, 255, 0.5);
    border-top: transparent;
    border-left: transparent;
    border-right: transparent;
    background: transparent;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    color: rgb(0, 128, 255, 0.5);
    outline: none;
    transition: all 300ms;
}


main{
    width: 100%;
    height: 100vh;
    padding: 20px;
    margin: auto;
    margin-top: 100px;
}

.contenedor__todo{
    width: 100%;
    max-width: 800px;
    margin: auto;
    position: relative;
}

.caja__trasera{
    width: 100%;
    padding: 10px 20px;
    display: flex;
    justify-content: center;
    backdrop-filter: blur(10px);
    background-color: rgba(0, 128, 255, 0.5);
}

.caja__trasera div{
    margin: 100px 40px;
    color: white;
    transition: all 500ms;
}

.caja__trasera div p,
.caja__trasera div button{
    margin-top: 30px;
}

.caja__trasera div h3{
    font-weight: 400;
    font-size: 26px;
}

.caja__trasera button{
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

.caja__trasera button:hover{
    background: #fff;
    color: #46A2FD;
}

/*formulario*/
.contenedor__ini-reg{
    display: flex;
    align-items: center;
    height: 0hv;
    width: 100%;
    max-width: 380px;
    position: relative;
    top: -440px;
    left: 10px;
    transition: left 500ms cubic-bezier(0.175, 0.885, 0.320, 1.275);
}

.contenedor__ini-reg form{
    width: 100%;
    padding: 80px 20px;
    margin-top: 500px;
    background: #fff;
    position: absolute;
    border-radius: 20px;
}


.contenedor__ini-reg form h2{
    font-size: 30px;
    text-align: center;
    margin-bottom: 20px;
    color: #46A2FD;
}

.contenedor__ini-reg form input{
    width: 100%;
    margin-top: 10px;
    padding: 10px;
    border: none;
    background: #F2F2F2;
    font-size: 16px;
    outline: none;
}

.contenedor__ini-reg form select{
    width: 100%;
    margin-top: 10px;
    padding: 10px;
    border: none;
    background: #F2F2F2;
    font-size: 16px;
    outline: none;
}

.contenedor__ini-reg form p{
    margin-top: 15px;
    margin-bottom: 5px;
    margin-left: 5px;
}

.contenedor__ini-reg form button{
    padding: 10px 40px;
    margin-top: 30px;
    border: none;
    font-size: 14px;
    background: #46A2FD;
    color: white;
    cursor: pointer;
    outline: none;
}

/*.formulario__inicio{
    opacity: 1;
    display: block;
}*/

.formulario_reg{
    display: none;
}

/*Responsive Design*/
@media screen and (max-width: 850px){

    main{
        margin-top: 50px;    
    }

    .caja__trasera{
        max-width: 350px;
        height: 300px;
        flex-direction: column;
        margin: auto;
    }

    .caja__trasera div{
        margin: 0px;
        position: absolute;
    }

    /*formulario*/
    .contenedor__ini-reg{
        top: -10px;
        left: -5px;
        margin: auto;
    }

    .contenedor__ini-reg form{
        position: relative;
    }
}

    </style>