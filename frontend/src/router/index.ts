import { createRouter, createWebHistory } from 'vue-router'
/* import HomeView from '../views/HomeView.vue' */
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import TasksView from '@/views/TasksView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: LoginView },
    { path: '/register', component: RegisterView },
    { path: '/tasks', component: TasksView },
  ],
});

export default router;