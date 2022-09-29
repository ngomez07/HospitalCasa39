<template>
<body>
<div class="boton">
    <button></button>
    <button></button>
</div>
    <main>
    <div class="contenedor__caja__form">
        <div class="caja__trasera">
            <div class="caja_trasera-register">
                <!--<button @click="$router.push('Registro')">Registrarse</button>-->
            </div>
        <div class="contenedor__formu">
            <form action="" class="formulario">
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
                <button @click="regis">Registrarse</button>
            </form>
        </div>
        </div>
    </div>
    </main>
</body>
</template>

<script>
export default {
  methods: {
    regis() {
      alert('Usuario Inscrito');
    },
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
    /*background: url("fondo1.jpg");*/
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

.contenedor__caja__form{
    width: 100%;
    max-width: 800px;
    margin: auto;
    position: relative;
}

.caja__trasera{
    width: 100%;
    padding: 10px 80px;
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


/*formulario*/
.contenedor__formu{
    display: flex;
    align-items: center;
    height: 0hv;
    width: 100%;
    max-width: 380px;
    position: absolute;
    top: -185px;
    left: 150px;
    transition: left 500ms cubic-bezier(0.175, 0.885, 0.320, 1.275);
}

.contenedor__formu form{
    width: 100%;
    padding: 80px 20px;
    margin-top: 550px;
    background: #fff;
    position: absolute;
    right: 0;
    border-radius: 20px;
}

.contenedor__formu form h2{
    font-size: 30px;
    text-align: center;
    margin-bottom: 20px;
    color: #46A2FD;
}

.contenedor__formu form input{
    width: 100%;
    margin-top: 10px;
    padding: 10px;
    border: none;
    background: #F2F2F2;
    font-size: 16px;
    outline: none;
}

.contenedor__formu form select{
    width: 100%;
    margin-top: 10px;
    padding: 10px;
    border: none;
    background: #F2F2F2;
    font-size: 16px;
    outline: none;
}

.contenedor__formu form p{
    margin-top: 15px;
    margin-bottom: 5px;
    margin-left: 5px;
}

.contenedor__formu form button{
    padding: 10px 40px;
    margin-top: 30px;
    border: none;
    font-size: 14px;
    background: #46A2FD;
    color: white;
    cursor: pointer;
    outline: none;
}

.formulario{
    display: block;
}

</style>