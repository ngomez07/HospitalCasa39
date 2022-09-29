<template>
<head>
    <meta charset="UFT-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casa Salud 39 Login</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="recursos/css/styles.css">
</head>
<body>

    <main>    
    <div class="contenedor__todo">
        <div class="caja__trasera">
            <div class="caja_trasera-login">
                <h3>¿Ya tienes una cuenta?</h3>
                <p>Inicia sesión para entrar en la página</p>
                <button id="btn__iniciar-sesion">Iniciar Sesión</button>
            </div>
            <div class="caja_trasera-register">
                <h3>¿Aún no tienes cuenta?</h3>
                <p>Registrate para que puedas iniciar sesión</p>
                <button id="btn__registrarse">Registrarse</button>
            </div>
        </div>
        <!--Formularios para ingresar-->
        <div class="contenedor__ini-reg">
            <!--Ingreso-->
            <form action="" class="formulario__inicio">
                <h2>Iniciar Sesión</h2>
                <input type="text" placeholder="Id User">
                <input type="password" placeholder="Contraseña">
                <button>Entrar</button>
            </form>
            <form action="" class="formulario_reg">
                <!--Registro-->
                <h2>Registrarse</h2>
                <input type="text" placeholder="ID">
                <input type="text" placeholder="Nombre">
                <input type="text" placeholder="Apellido">
                <p>Fecha de nacimiento</p>
                <input type="date" id="start" name="trip-start">
                <input type="text" placeholder="Edad">
                <input type="text" placeholder="RH">
                <input type="text" placeholder="Correo Electronico">
                <input type="text" placeholder="Celular">
                <input type="text" placeholder="Direccion">
                <input type="text" placeholder="Ciudad">
                <input type="text" placeholder="Familiar Responsable">
                <input type="text" placeholder="Parentesco">
                <input type="text" placeholder="Correo Responsable">
                <input type="text" placeholder="Celular Responsable">
                <input type="text" placeholder="ID Usuario">
                <input type="text" placeholder="Contraseña">
                <button>Registrarse</button>
            </form>
        </div>
    </div>
    </main>
</body>
</template>

<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
    font-family: 'Roboto', sans-serif;
}
body{
    background-image: url(../imagenes/fondo1.jpg);
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
}

main{
    width: 100%;
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
    width: 100%;
    max-width: 380px;
    position: relative;
    top: -185px;
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

.formulario__inicio{
    margin-bottom: 500px;
    height: 400px;
    opacity: 1;
    display: block;
}

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