import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';
import LoginPaciente from './components/LoginPaciente.vue'
import LoginPersonal from './components/LoginPersonal.vue'
import regisPa from './components/regisPa.vue'
import PagUser from './components/PagUser.vue'

const routes = [{
path: '/Inicio',
name: 'Inicio',
component: App
},
{
path: '/LoginPaciente',
name: 'LoginPaciente',
component: LoginPaciente
},
{
path: '/LoginPersonal',
name: 'LoginPersonal',
component: LoginPersonal
},
{
path: '/regisPa',
name: 'regisPa',
component: regisPa
},
{
    path: '/PagUser',
    name: 'PagUser',
    component: PagUser
    },
];
const router = createRouter({
history: createWebHistory(),
routes,
});
export default router;

