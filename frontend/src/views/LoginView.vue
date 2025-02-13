<template>
  <div class="min-h-screen flex items-center justify-center bg-[#13161c]">
    <div class="bg-[#172635] p-8 rounded-lg shadow-md w-96">
      <h2 class="text-2xl font-bold mb-6 text-center text-[#0791E6]">Login</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label for="username" class="block text-sm font-medium text-[#f7f7f7]">Username:</label>
          <input
            type="text"
            v-model="username"
            required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-[#f7f7f7]">Password:</label>
          <input
            type="password"
            v-model="password"
            required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
          />
        </div>
        <button
          type="submit"
          class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        >
          Login
        </button>
        <!-- Mensaje de error -->
        <p v-if="errorMessage" class="mt-4 text-center text-red-500">
          {{ errorMessage }}
        </p>
        
      </form>
      <p class="mt-4 text-center text-sm text-[#f7f7f7]">
        Don't have an account?
        <router-link to="/register" class="text-indigo-600 hover:text-indigo-500">Register</router-link>
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';

export default {
  setup() {
    const username = ref('');
    const password = ref('');
    const errorMessage = ref('');
    const router = useRouter();

    const login = async () => {
      errorMessage.value = ''; // Limpiar el mensaje de error antes de cada intento

      try {
        const response = await api.post('/token/', {
          username: username.value,
          password: password.value,
        });

        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        router.push('/tasks');
      } 
      catch (error: any) { // 👈 Declaramos error como "any" para evitar problemas de tipado
        if (error.response?.status === 401) { // 👈 Usamos "?" para evitar errores si response es undefined
          errorMessage.value = 'Usuario o contraseña incorrectos';
        } else {
          errorMessage.value = 'Error al iniciar sesión. Inténtalo de nuevo.';
        }
      }
    };


    return { username, password, errorMessage, login };
  },
};
</script>
